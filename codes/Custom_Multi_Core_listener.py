from default_codes.ast import AST
from default_codes.make_ast_subtree import make_ast_subtree
from gen.Multi_Core_GrammarListener import Multi_Core_GrammarListener

class Custom_Multi_Core_listener(Multi_Core_GrammarListener):
    def __init__(self, rule_names):
        self.overridden_rules = [
            'program', 'threadsNumber', 'threadST', 'time', 'code',
            'forLoop', 'variable', 'iterable', 'range', 'threads_no',
            'bool', 'otherCode', 'from', 'to'
        ]
        self.rule_names = rule_names
        self.ast = AST()

    def exitEveryRule(self, ctx):
        rule_name = self.rule_names[ctx.getRuleIndex()]
        if rule_name not in self.overridden_rules:
            make_ast_subtree(self.ast, ctx, rule_name)

    def exitProgram(self, ctx):
        make_ast_subtree(self.ast, ctx, "program", keep_node=True)

    def exitThreadsNumber(self, ctx):
        make_ast_subtree(self.ast, ctx, "threadsNumber", keep_node=True)

    def exitThreadST(self, ctx):
        make_ast_subtree(self.ast, ctx, "threadST", keep_node=True)

    def exitTime(self, ctx):
        make_ast_subtree(self.ast, ctx, "time", keep_node=True)

    def exitCode(self, ctx):
        make_ast_subtree(self.ast, ctx, "code", keep_node=True)

    def exitForLoop(self, ctx):
        make_ast_subtree(self.ast, ctx, "forLoop", keep_node=True)

    def exitVariable(self, ctx):
        make_ast_subtree(self.ast, ctx, "variable", keep_node=True)

    def exitIterable(self, ctx):
        make_ast_subtree(self.ast, ctx, "iterable", keep_node=True)

    def exitRange(self, ctx):
        make_ast_subtree(self.ast, ctx, "range", keep_node=True)

    def exitThreads_no(self, ctx):
        make_ast_subtree(self.ast, ctx, "threads_no", keep_node=True)

    def exitBool(self, ctx):
        make_ast_subtree(self.ast, ctx, "bool", keep_node=True)

    def exitOtherCode(self, ctx):
        make_ast_subtree(self.ast, ctx, "otherCode", keep_node=True)

    def exitFrom(self, ctx):
        make_ast_subtree(self.ast, ctx, "start", keep_node=True)

    def exitTo(self, ctx):
        make_ast_subtree(self.ast, ctx, "end", keep_node=True)