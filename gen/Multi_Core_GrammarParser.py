# Generated from /home/asa/Code/Git/Multi-core_DLS/Multi_Core_Grammar.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,5,28,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,1,1,
        3,1,15,8,1,1,1,3,1,18,8,1,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,4,0,
        0,5,0,2,4,6,8,0,0,24,0,10,1,0,0,0,2,14,1,0,0,0,4,21,1,0,0,0,6,23,
        1,0,0,0,8,25,1,0,0,0,10,11,3,2,1,0,11,12,5,0,0,1,12,1,1,0,0,0,13,
        15,3,4,2,0,14,13,1,0,0,0,14,15,1,0,0,0,15,17,1,0,0,0,16,18,3,6,3,
        0,17,16,1,0,0,0,17,18,1,0,0,0,18,19,1,0,0,0,19,20,3,8,4,0,20,3,1,
        0,0,0,21,22,5,2,0,0,22,5,1,0,0,0,23,24,5,1,0,0,24,7,1,0,0,0,25,26,
        5,3,0,0,26,9,1,0,0,0,2,14,17
    ]

class Multi_Core_GrammarParser ( Parser ):

    grammarFileName = "Multi_Core_Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "TIME", "INTEGER", "STRING", "WS", "NEWLINE" ]

    RULE_start = 0
    RULE_program = 1
    RULE_threads_number = 2
    RULE_time = 3
    RULE_code_address = 4

    ruleNames =  [ "start", "program", "threads_number", "time", "code_address" ]

    EOF = Token.EOF
    TIME=1
    INTEGER=2
    STRING=3
    WS=4
    NEWLINE=5

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def program(self):
            return self.getTypedRuleContext(Multi_Core_GrammarParser.ProgramContext,0)


        def EOF(self):
            return self.getToken(Multi_Core_GrammarParser.EOF, 0)

        def getRuleIndex(self):
            return Multi_Core_GrammarParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = Multi_Core_GrammarParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.program()
            self.state = 11
            self.match(Multi_Core_GrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def code_address(self):
            return self.getTypedRuleContext(Multi_Core_GrammarParser.Code_addressContext,0)


        def threads_number(self):
            return self.getTypedRuleContext(Multi_Core_GrammarParser.Threads_numberContext,0)


        def time(self):
            return self.getTypedRuleContext(Multi_Core_GrammarParser.TimeContext,0)


        def getRuleIndex(self):
            return Multi_Core_GrammarParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = Multi_Core_GrammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 13
                self.threads_number()


            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 16
                self.time()


            self.state = 19
            self.code_address()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Threads_numberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(Multi_Core_GrammarParser.INTEGER, 0)

        def getRuleIndex(self):
            return Multi_Core_GrammarParser.RULE_threads_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThreads_number" ):
                listener.enterThreads_number(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThreads_number" ):
                listener.exitThreads_number(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThreads_number" ):
                return visitor.visitThreads_number(self)
            else:
                return visitor.visitChildren(self)




    def threads_number(self):

        localctx = Multi_Core_GrammarParser.Threads_numberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_threads_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.match(Multi_Core_GrammarParser.INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TIME(self):
            return self.getToken(Multi_Core_GrammarParser.TIME, 0)

        def getRuleIndex(self):
            return Multi_Core_GrammarParser.RULE_time

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTime" ):
                listener.enterTime(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTime" ):
                listener.exitTime(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTime" ):
                return visitor.visitTime(self)
            else:
                return visitor.visitChildren(self)




    def time(self):

        localctx = Multi_Core_GrammarParser.TimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_time)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(Multi_Core_GrammarParser.TIME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Code_addressContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(Multi_Core_GrammarParser.STRING, 0)

        def getRuleIndex(self):
            return Multi_Core_GrammarParser.RULE_code_address

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCode_address" ):
                listener.enterCode_address(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCode_address" ):
                listener.exitCode_address(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCode_address" ):
                return visitor.visitCode_address(self)
            else:
                return visitor.visitChildren(self)




    def code_address(self):

        localctx = Multi_Core_GrammarParser.Code_addressContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_code_address)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(Multi_Core_GrammarParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





