# Generated from /home/asa/Code/Git/Multi-core_DLS/Multi_Core_Grammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .Multi_Core_GrammarParser import Multi_Core_GrammarParser
else:
    from Multi_Core_GrammarParser import Multi_Core_GrammarParser

# This class defines a complete listener for a parse tree produced by Multi_Core_GrammarParser.
class Multi_Core_GrammarListener(ParseTreeListener):

    # Enter a parse tree produced by Multi_Core_GrammarParser#start.
    def enterStart(self, ctx:Multi_Core_GrammarParser.StartContext):
        pass

    # Exit a parse tree produced by Multi_Core_GrammarParser#start.
    def exitStart(self, ctx:Multi_Core_GrammarParser.StartContext):
        pass


    # Enter a parse tree produced by Multi_Core_GrammarParser#program.
    def enterProgram(self, ctx:Multi_Core_GrammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by Multi_Core_GrammarParser#program.
    def exitProgram(self, ctx:Multi_Core_GrammarParser.ProgramContext):
        pass


    # Enter a parse tree produced by Multi_Core_GrammarParser#threads_number.
    def enterThreads_number(self, ctx:Multi_Core_GrammarParser.Threads_numberContext):
        pass

    # Exit a parse tree produced by Multi_Core_GrammarParser#threads_number.
    def exitThreads_number(self, ctx:Multi_Core_GrammarParser.Threads_numberContext):
        pass


    # Enter a parse tree produced by Multi_Core_GrammarParser#time.
    def enterTime(self, ctx:Multi_Core_GrammarParser.TimeContext):
        pass

    # Exit a parse tree produced by Multi_Core_GrammarParser#time.
    def exitTime(self, ctx:Multi_Core_GrammarParser.TimeContext):
        pass


    # Enter a parse tree produced by Multi_Core_GrammarParser#code_address.
    def enterCode_address(self, ctx:Multi_Core_GrammarParser.Code_addressContext):
        pass

    # Exit a parse tree produced by Multi_Core_GrammarParser#code_address.
    def exitCode_address(self, ctx:Multi_Core_GrammarParser.Code_addressContext):
        pass



del Multi_Core_GrammarParser