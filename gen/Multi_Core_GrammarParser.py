# Generated from /home/saba/Git/Multi-core_DLS/Multi_Core_Grammar.g4 by ANTLR 4.13.1
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
        4,1,15,93,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,4,1,
        4,1,5,5,5,46,8,5,10,5,12,5,49,9,5,1,5,3,5,52,8,5,3,5,54,8,5,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,8,1,8,3,8,67,8,8,1,9,1,9,1,9,1,
        9,1,9,3,9,74,8,9,1,9,1,9,1,9,1,10,1,10,1,11,1,11,1,12,1,12,1,13,
        1,13,1,14,5,14,88,8,14,10,14,12,14,91,9,14,1,14,1,89,0,15,0,2,4,
        6,8,10,12,14,16,18,20,22,24,26,28,0,0,83,0,30,1,0,0,0,2,33,1,0,0,
        0,4,37,1,0,0,0,6,40,1,0,0,0,8,42,1,0,0,0,10,53,1,0,0,0,12,55,1,0,
        0,0,14,62,1,0,0,0,16,66,1,0,0,0,18,68,1,0,0,0,20,78,1,0,0,0,22,80,
        1,0,0,0,24,82,1,0,0,0,26,84,1,0,0,0,28,89,1,0,0,0,30,31,3,2,1,0,
        31,32,5,0,0,1,32,1,1,0,0,0,33,34,3,4,2,0,34,35,3,8,4,0,35,36,3,10,
        5,0,36,3,1,0,0,0,37,38,3,6,3,0,38,39,3,24,12,0,39,5,1,0,0,0,40,41,
        5,1,0,0,41,7,1,0,0,0,42,43,3,26,13,0,43,9,1,0,0,0,44,46,3,12,6,0,
        45,44,1,0,0,0,46,49,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,54,1,
        0,0,0,49,47,1,0,0,0,50,52,3,28,14,0,51,50,1,0,0,0,51,52,1,0,0,0,
        52,54,1,0,0,0,53,47,1,0,0,0,53,51,1,0,0,0,54,11,1,0,0,0,55,56,5,
        2,0,0,56,57,3,14,7,0,57,58,5,3,0,0,58,59,3,16,8,0,59,60,5,5,0,0,
        60,61,3,10,5,0,61,13,1,0,0,0,62,63,5,11,0,0,63,15,1,0,0,0,64,67,
        5,11,0,0,65,67,3,18,9,0,66,64,1,0,0,0,66,65,1,0,0,0,67,17,1,0,0,
        0,68,69,5,4,0,0,69,73,5,6,0,0,70,71,3,20,10,0,71,72,5,8,0,0,72,74,
        1,0,0,0,73,70,1,0,0,0,73,74,1,0,0,0,74,75,1,0,0,0,75,76,3,22,11,
        0,76,77,5,7,0,0,77,19,1,0,0,0,78,79,5,10,0,0,79,21,1,0,0,0,80,81,
        5,10,0,0,81,23,1,0,0,0,82,83,5,10,0,0,83,25,1,0,0,0,84,85,5,9,0,
        0,85,27,1,0,0,0,86,88,9,0,0,0,87,86,1,0,0,0,88,91,1,0,0,0,89,90,
        1,0,0,0,89,87,1,0,0,0,90,29,1,0,0,0,91,89,1,0,0,0,6,47,51,53,66,
        73,89
    ]

class Multi_Core_GrammarParser ( Parser ):

    grammarFileName = "Multi_Core_Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'threads_number:'", "'for'", "'in'", 
                     "'range'", "':'", "'('", "')'", "','", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'.'", "'\\t'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "FOR", "IN", "RANGE", "COLON", 
                      "LPAREN", "RPAREN", "COMMA", "BOOLEAN", "INTEGER", 
                      "IDENTIFIER", "DOT", "INDENT", "WS", "NEWLINE" ]

    RULE_start = 0
    RULE_program = 1
    RULE_threadsNumber = 2
    RULE_threadST = 3
    RULE_time = 4
    RULE_code = 5
    RULE_forLoop = 6
    RULE_variable = 7
    RULE_iterable = 8
    RULE_range = 9
    RULE_from = 10
    RULE_to = 11
    RULE_threads_no = 12
    RULE_bool = 13
    RULE_otherCode = 14

    ruleNames =  [ "start", "program", "threadsNumber", "threadST", "time", 
                   "code", "forLoop", "variable", "iterable", "range", "from", 
                   "to", "threads_no", "bool", "otherCode" ]

    EOF = Token.EOF
    T__0=1
    FOR=2
    IN=3
    RANGE=4
    COLON=5
    LPAREN=6
    RPAREN=7
    COMMA=8
    BOOLEAN=9
    INTEGER=10
    IDENTIFIER=11
    DOT=12
    INDENT=13
    WS=14
    NEWLINE=15

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
            self.state = 30
            self.program()
            self.state = 31
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

        def threadsNumber(self):
            return self.getTypedRuleContext(Multi_Core_GrammarParser.ThreadsNumberContext,0)


        def time(self):
            return self.getTypedRuleContext(Multi_Core_GrammarParser.TimeContext,0)


        def code(self):
            return self.getTypedRuleContext(Multi_Core_GrammarParser.CodeContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.threadsNumber()
            self.state = 34
            self.time()
            self.state = 35
            self.code()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ThreadsNumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def threadST(self):
            return self.getTypedRuleContext(Multi_Core_GrammarParser.ThreadSTContext,0)


        def threads_no(self):
            return self.getTypedRuleContext(Multi_Core_GrammarParser.Threads_noContext,0)


        def getRuleIndex(self):
            return Multi_Core_GrammarParser.RULE_threadsNumber

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThreadsNumber" ):
                listener.enterThreadsNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThreadsNumber" ):
                listener.exitThreadsNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThreadsNumber" ):
                return visitor.visitThreadsNumber(self)
            else:
                return visitor.visitChildren(self)




    def threadsNumber(self):

        localctx = Multi_Core_GrammarParser.ThreadsNumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_threadsNumber)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.threadST()
            self.state = 38
            self.threads_no()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ThreadSTContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Multi_Core_GrammarParser.RULE_threadST

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThreadST" ):
                listener.enterThreadST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThreadST" ):
                listener.exitThreadST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThreadST" ):
                return visitor.visitThreadST(self)
            else:
                return visitor.visitChildren(self)




    def threadST(self):

        localctx = Multi_Core_GrammarParser.ThreadSTContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_threadST)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(Multi_Core_GrammarParser.T__0)
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

        def bool_(self):
            return self.getTypedRuleContext(Multi_Core_GrammarParser.BoolContext,0)


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
        self.enterRule(localctx, 8, self.RULE_time)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.bool_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def forLoop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Multi_Core_GrammarParser.ForLoopContext)
            else:
                return self.getTypedRuleContext(Multi_Core_GrammarParser.ForLoopContext,i)


        def otherCode(self):
            return self.getTypedRuleContext(Multi_Core_GrammarParser.OtherCodeContext,0)


        def getRuleIndex(self):
            return Multi_Core_GrammarParser.RULE_code

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCode" ):
                listener.enterCode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCode" ):
                listener.exitCode(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCode" ):
                return visitor.visitCode(self)
            else:
                return visitor.visitChildren(self)




    def code(self):

        localctx = Multi_Core_GrammarParser.CodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_code)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 47
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 44
                        self.forLoop() 
                    self.state = 49
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

                pass

            elif la_ == 2:
                self.state = 51
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 50
                    self.otherCode()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(Multi_Core_GrammarParser.FOR, 0)

        def variable(self):
            return self.getTypedRuleContext(Multi_Core_GrammarParser.VariableContext,0)


        def IN(self):
            return self.getToken(Multi_Core_GrammarParser.IN, 0)

        def iterable(self):
            return self.getTypedRuleContext(Multi_Core_GrammarParser.IterableContext,0)


        def COLON(self):
            return self.getToken(Multi_Core_GrammarParser.COLON, 0)

        def code(self):
            return self.getTypedRuleContext(Multi_Core_GrammarParser.CodeContext,0)


        def getRuleIndex(self):
            return Multi_Core_GrammarParser.RULE_forLoop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForLoop" ):
                listener.enterForLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForLoop" ):
                listener.exitForLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForLoop" ):
                return visitor.visitForLoop(self)
            else:
                return visitor.visitChildren(self)




    def forLoop(self):

        localctx = Multi_Core_GrammarParser.ForLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_forLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(Multi_Core_GrammarParser.FOR)
            self.state = 56
            self.variable()
            self.state = 57
            self.match(Multi_Core_GrammarParser.IN)
            self.state = 58
            self.iterable()
            self.state = 59
            self.match(Multi_Core_GrammarParser.COLON)
            self.state = 60
            self.code()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(Multi_Core_GrammarParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return Multi_Core_GrammarParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = Multi_Core_GrammarParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(Multi_Core_GrammarParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IterableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(Multi_Core_GrammarParser.IDENTIFIER, 0)

        def range_(self):
            return self.getTypedRuleContext(Multi_Core_GrammarParser.RangeContext,0)


        def getRuleIndex(self):
            return Multi_Core_GrammarParser.RULE_iterable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIterable" ):
                listener.enterIterable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIterable" ):
                listener.exitIterable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIterable" ):
                return visitor.visitIterable(self)
            else:
                return visitor.visitChildren(self)




    def iterable(self):

        localctx = Multi_Core_GrammarParser.IterableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_iterable)
        try:
            self.state = 66
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.match(Multi_Core_GrammarParser.IDENTIFIER)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.range_()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RANGE(self):
            return self.getToken(Multi_Core_GrammarParser.RANGE, 0)

        def LPAREN(self):
            return self.getToken(Multi_Core_GrammarParser.LPAREN, 0)

        def to(self):
            return self.getTypedRuleContext(Multi_Core_GrammarParser.ToContext,0)


        def RPAREN(self):
            return self.getToken(Multi_Core_GrammarParser.RPAREN, 0)

        def from_(self):
            return self.getTypedRuleContext(Multi_Core_GrammarParser.FromContext,0)


        def COMMA(self):
            return self.getToken(Multi_Core_GrammarParser.COMMA, 0)

        def getRuleIndex(self):
            return Multi_Core_GrammarParser.RULE_range

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRange" ):
                listener.enterRange(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRange" ):
                listener.exitRange(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRange" ):
                return visitor.visitRange(self)
            else:
                return visitor.visitChildren(self)




    def range_(self):

        localctx = Multi_Core_GrammarParser.RangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_range)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(Multi_Core_GrammarParser.RANGE)
            self.state = 69
            self.match(Multi_Core_GrammarParser.LPAREN)
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 70
                self.from_()
                self.state = 71
                self.match(Multi_Core_GrammarParser.COMMA)


            self.state = 75
            self.to()
            self.state = 76
            self.match(Multi_Core_GrammarParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FromContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(Multi_Core_GrammarParser.INTEGER, 0)

        def getRuleIndex(self):
            return Multi_Core_GrammarParser.RULE_from

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFrom" ):
                listener.enterFrom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFrom" ):
                listener.exitFrom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFrom" ):
                return visitor.visitFrom(self)
            else:
                return visitor.visitChildren(self)




    def from_(self):

        localctx = Multi_Core_GrammarParser.FromContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_from)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(Multi_Core_GrammarParser.INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ToContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(Multi_Core_GrammarParser.INTEGER, 0)

        def getRuleIndex(self):
            return Multi_Core_GrammarParser.RULE_to

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTo" ):
                listener.enterTo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTo" ):
                listener.exitTo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTo" ):
                return visitor.visitTo(self)
            else:
                return visitor.visitChildren(self)




    def to(self):

        localctx = Multi_Core_GrammarParser.ToContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_to)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(Multi_Core_GrammarParser.INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Threads_noContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(Multi_Core_GrammarParser.INTEGER, 0)

        def getRuleIndex(self):
            return Multi_Core_GrammarParser.RULE_threads_no

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThreads_no" ):
                listener.enterThreads_no(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThreads_no" ):
                listener.exitThreads_no(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThreads_no" ):
                return visitor.visitThreads_no(self)
            else:
                return visitor.visitChildren(self)




    def threads_no(self):

        localctx = Multi_Core_GrammarParser.Threads_noContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_threads_no)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(Multi_Core_GrammarParser.INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN(self):
            return self.getToken(Multi_Core_GrammarParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return Multi_Core_GrammarParser.RULE_bool

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool" ):
                listener.enterBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool" ):
                listener.exitBool(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool" ):
                return visitor.visitBool(self)
            else:
                return visitor.visitChildren(self)




    def bool_(self):

        localctx = Multi_Core_GrammarParser.BoolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_bool)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(Multi_Core_GrammarParser.BOOLEAN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OtherCodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Multi_Core_GrammarParser.RULE_otherCode

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOtherCode" ):
                listener.enterOtherCode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOtherCode" ):
                listener.exitOtherCode(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOtherCode" ):
                return visitor.visitOtherCode(self)
            else:
                return visitor.visitChildren(self)




    def otherCode(self):

        localctx = Multi_Core_GrammarParser.OtherCodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_otherCode)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 86
                    self.matchWildcard() 
                self.state = 91
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





