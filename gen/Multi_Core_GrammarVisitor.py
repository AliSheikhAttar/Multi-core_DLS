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


    # Visit a parse tree produced by Multi_Core_GrammarParser#threadsNumber.
    def visitThreadsNumber(self, ctx:Multi_Core_GrammarParser.ThreadsNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Multi_Core_GrammarParser#threadST.
    def visitThreadST(self, ctx:Multi_Core_GrammarParser.ThreadSTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Multi_Core_GrammarParser#time.
    def visitTime(self, ctx:Multi_Core_GrammarParser.TimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Multi_Core_GrammarParser#timeST.
    def visitTimeST(self, ctx:Multi_Core_GrammarParser.TimeSTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Multi_Core_GrammarParser#forLoop.
    def visitForLoop(self, ctx:Multi_Core_GrammarParser.ForLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Multi_Core_GrammarParser#variable.
    def visitVariable(self, ctx:Multi_Core_GrammarParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Multi_Core_GrammarParser#iterable.
    def visitIterable(self, ctx:Multi_Core_GrammarParser.IterableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Multi_Core_GrammarParser#range.
    def visitRange(self, ctx:Multi_Core_GrammarParser.RangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Multi_Core_GrammarParser#from.
    def visitFrom(self, ctx:Multi_Core_GrammarParser.FromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Multi_Core_GrammarParser#to.
    def visitTo(self, ctx:Multi_Core_GrammarParser.ToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Multi_Core_GrammarParser#threads_no.
    def visitThreads_no(self, ctx:Multi_Core_GrammarParser.Threads_noContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Multi_Core_GrammarParser#bool.
    def visitBool(self, ctx:Multi_Core_GrammarParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Multi_Core_GrammarParser#otherCode.
    def visitOtherCode(self, ctx:Multi_Core_GrammarParser.OtherCodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Multi_Core_GrammarParser#pythonFile.
    def visitPythonFile(self, ctx:Multi_Core_GrammarParser.PythonFileContext):
        return self.visitChildren(ctx)



del Multi_Core_GrammarParser