# Generated from /home/asa/Code/Git/Multi-core_DLS/Multi_Core_Grammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .Multi_Core_GrammarParser import Multi_Core_GrammarParser
else:
    from Multi_Core_GrammarParser import Multi_Core_GrammarParser

# This class defines a complete generic visitor for a parse tree produced by Multi_Core_GrammarParser.

class Multi_Core_GrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by Multi_Core_GrammarParser#start.
    def visitStart(self, ctx:Multi_Core_GrammarParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Multi_Core_GrammarParser#program.
    def visitProgram(self, ctx:Multi_Core_GrammarParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Multi_Core_GrammarParser#threads_number.
    def visitThreads_number(self, ctx:Multi_Core_GrammarParser.Threads_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Multi_Core_GrammarParser#time.
    def visitTime(self, ctx:Multi_Core_GrammarParser.TimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Multi_Core_GrammarParser#code_address.
    def visitCode_address(self, ctx:Multi_Core_GrammarParser.Code_addressContext):
        return self.visitChildren(ctx)



del Multi_Core_GrammarParser