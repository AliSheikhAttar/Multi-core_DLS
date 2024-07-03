from antlr4 import *
import argparse
from codes.Custom_Multi_Core_listener import Custom_Multi_Core_listener
from default_codes.ast_to_networkx_graph import show_ast
from gen.Multi_Core_GrammarLexer import Multi_Core_GrammarLexer
from gen.Multi_Core_GrammarParser import Multi_Core_GrammarParser
from default_codes.post_order_ast_traverser import PostOrderASTTraverser
from codes.custom_example_dsl_code_generator import CustomExampleDSLCodeGenerator


def main(arguments):
	stream = FileStream(arguments.input, encoding='utf8')
	lexer = Multi_Core_GrammarLexer(stream)
	token_stream = CommonTokenStream(lexer)
	parser = Multi_Core_GrammarParser(token_stream)
	parse_tree = parser.program()
	ast_builder_listener = Custom_Multi_Core_listener(parser.ruleNames)
	walker = ParseTreeWalker()
	walker.walk(t=parse_tree, listener=ast_builder_listener)
	ast = ast_builder_listener.ast
	show_ast(ast.root)
	post_order_ast_traverser = PostOrderASTTraverser()
	post_order_ast_traverser.node_attributes = ['label', 'text', 'number']
	traversal = post_order_ast_traverser.traverse_ast(ast.root)
	code_generator = CustomExampleDSLCodeGenerator()
	generated_code = code_generator.generate_code(traversal)
	with open(arguments.output, 'w') as output_file:
		output_file.write(generated_code)


if __name__ == '__main__':
	argparser = argparse.ArgumentParser()
	argparser.add_argument('-i', '--input', help='Input source', default=r'input.txt')
	argparser.add_argument('-o', '--output', help='Output path', default=r'test_output3.py')
	args = argparser.parse_args()
	main(args)

