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
        4,1,17,102,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,1,0,1,0,1,1,1,1,1,1,1,1,5,1,40,8,1,10,1,
        12,1,43,9,1,1,2,3,2,46,8,2,1,2,1,2,1,3,1,3,1,4,3,4,53,8,4,1,4,1,
        4,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,66,8,6,10,6,12,6,69,9,
        6,1,7,1,7,1,8,1,8,3,8,75,8,8,1,9,1,9,1,9,1,9,1,9,3,9,82,8,9,1,9,
        1,9,1,9,1,10,1,10,1,11,1,11,1,12,1,12,1,13,1,13,1,14,4,14,96,8,14,
        11,14,12,14,97,1,15,1,15,1,15,1,97,0,16,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,0,0,94,0,32,1,0,0,0,2,35,1,0,0,0,4,45,1,0,0,0,
        6,49,1,0,0,0,8,52,1,0,0,0,10,56,1,0,0,0,12,58,1,0,0,0,14,70,1,0,
        0,0,16,74,1,0,0,0,18,76,1,0,0,0,20,86,1,0,0,0,22,88,1,0,0,0,24,90,
        1,0,0,0,26,92,1,0,0,0,28,95,1,0,0,0,30,99,1,0,0,0,32,33,3,2,1,0,
        33,34,5,0,0,1,34,1,1,0,0,0,35,36,3,4,2,0,36,41,3,8,4,0,37,40,3,12,
        6,0,38,40,3,30,15,0,39,37,1,0,0,0,39,38,1,0,0,0,40,43,1,0,0,0,41,
        39,1,0,0,0,41,42,1,0,0,0,42,3,1,0,0,0,43,41,1,0,0,0,44,46,3,6,3,
        0,45,44,1,0,0,0,45,46,1,0,0,0,46,47,1,0,0,0,47,48,3,24,12,0,48,5,
        1,0,0,0,49,50,5,1,0,0,50,7,1,0,0,0,51,53,3,10,5,0,52,51,1,0,0,0,
        52,53,1,0,0,0,53,54,1,0,0,0,54,55,3,26,13,0,55,9,1,0,0,0,56,57,5,
        2,0,0,57,11,1,0,0,0,58,59,5,3,0,0,59,60,3,14,7,0,60,61,5,4,0,0,61,
        62,3,16,8,0,62,67,5,6,0,0,63,66,3,12,6,0,64,66,3,28,14,0,65,63,1,
        0,0,0,65,64,1,0,0,0,66,69,1,0,0,0,67,65,1,0,0,0,67,68,1,0,0,0,68,
        13,1,0,0,0,69,67,1,0,0,0,70,71,5,12,0,0,71,15,1,0,0,0,72,75,5,12,
        0,0,73,75,3,18,9,0,74,72,1,0,0,0,74,73,1,0,0,0,75,17,1,0,0,0,76,
        77,5,5,0,0,77,81,5,7,0,0,78,79,3,20,10,0,79,80,5,9,0,0,80,82,1,0,
        0,0,81,78,1,0,0,0,81,82,1,0,0,0,82,83,1,0,0,0,83,84,3,22,11,0,84,
        85,5,8,0,0,85,19,1,0,0,0,86,87,5,11,0,0,87,21,1,0,0,0,88,89,5,11,
        0,0,89,23,1,0,0,0,90,91,5,11,0,0,91,25,1,0,0,0,92,93,5,10,0,0,93,
        27,1,0,0,0,94,96,9,0,0,0,95,94,1,0,0,0,96,97,1,0,0,0,97,98,1,0,0,
        0,97,95,1,0,0,0,98,29,1,0,0,0,99,100,5,13,0,0,100,31,1,0,0,0,9,39,
        41,45,52,65,67,74,81,97
    ]

class Multi_Core_GrammarParser ( Parser ):

    grammarFileName = "Multi_Core_Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'threads_number:'", "'time:'", "'for'", 
                     "'in'", "'range'", "':'", "'('", "')'", "','", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'.'", "'\\t'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "FOR", "IN", 
                      "RANGE", "COLON", "LPAREN", "RPAREN", "COMMA", "BOOLEAN", 
                      "INTEGER", "IDENTIFIER", "FILEPATH", "DOT", "INDENT", 
                      "WS", "NEWLINE" ]

    RULE_start = 0
    RULE_program = 1
    RULE_threadsNumber = 2
    RULE_threadST = 3
    RULE_time = 4
    RULE_timeST = 5
    RULE_forLoop = 6
    RULE_variable = 7
    RULE_iterable = 8
    RULE_range = 9
    RULE_from = 10
    RULE_to = 11
    RULE_threads_no = 12
    RULE_bool = 13
    RULE_otherCode = 14
    RULE_pythonFile = 15

    ruleNames =  [ "start", "program", "threadsNumber", "threadST", "time", 
                   "timeST", "forLoop", "variable", "iterable", "range", 
                   "from", "to", "threads_no", "bool", "otherCode", "pythonFile" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    FOR=3
    IN=4
    RANGE=5
    COLON=6
    LPAREN=7
    RPAREN=8
    COMMA=9
    BOOLEAN=10
    INTEGER=11
    IDENTIFIER=12
    FILEPATH=13
    DOT=14
    INDENT=15
    WS=16
    NEWLINE=17

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
            self.state = 32
            self.program()
            self.state = 33
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


        def forLoop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Multi_Core_GrammarParser.ForLoopContext)
            else:
                return self.getTypedRuleContext(Multi_Core_GrammarParser.ForLoopContext,i)


        def pythonFile(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Multi_Core_GrammarParser.PythonFileContext)
            else:
                return self.getTypedRuleContext(Multi_Core_GrammarParser.PythonFileContext,i)


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
            self.state = 35
            self.threadsNumber()
            self.state = 36
            self.time()
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3 or _la==13:
                self.state = 39
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3]:
                    self.state = 37
                    self.forLoop()
                    pass
                elif token in [13]:
                    self.state = 38
                    self.pythonFile()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def threads_no(self):
            return self.getTypedRuleContext(Multi_Core_GrammarParser.Threads_noContext,0)


        def threadST(self):
            return self.getTypedRuleContext(Multi_Core_GrammarParser.ThreadSTContext,0)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 44
                self.threadST()


            self.state = 47
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
            self.state = 49
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


        def timeST(self):
            return self.getTypedRuleContext(Multi_Core_GrammarParser.TimeSTContext,0)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 51
                self.timeST()


            self.state = 54
            self.bool_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TimeSTContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Multi_Core_GrammarParser.RULE_timeST

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTimeST" ):
                listener.enterTimeST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTimeST" ):
                listener.exitTimeST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTimeST" ):
                return visitor.visitTimeST(self)
            else:
                return visitor.visitChildren(self)




    def timeST(self):

        localctx = Multi_Core_GrammarParser.TimeSTContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_timeST)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(Multi_Core_GrammarParser.T__1)
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

        def forLoop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Multi_Core_GrammarParser.ForLoopContext)
            else:
                return self.getTypedRuleContext(Multi_Core_GrammarParser.ForLoopContext,i)


        def otherCode(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Multi_Core_GrammarParser.OtherCodeContext)
            else:
                return self.getTypedRuleContext(Multi_Core_GrammarParser.OtherCodeContext,i)


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
            self.state = 58
            self.match(Multi_Core_GrammarParser.FOR)
            self.state = 59
            self.variable()
            self.state = 60
            self.match(Multi_Core_GrammarParser.IN)
            self.state = 61
            self.iterable()
            self.state = 62
            self.match(Multi_Core_GrammarParser.COLON)
            self.state = 67
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 65
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        self.state = 63
                        self.forLoop()
                        pass

                    elif la_ == 2:
                        self.state = 64
                        self.otherCode()
                        pass

             
                self.state = 69
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

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
            self.state = 70
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
            self.state = 74
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.match(Multi_Core_GrammarParser.IDENTIFIER)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
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
            self.state = 76
            self.match(Multi_Core_GrammarParser.RANGE)
            self.state = 77
            self.match(Multi_Core_GrammarParser.LPAREN)
            self.state = 81
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 78
                self.from_()
                self.state = 79
                self.match(Multi_Core_GrammarParser.COMMA)


            self.state = 83
            self.to()
            self.state = 84
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
            self.state = 86
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
            self.state = 88
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
            self.state = 90
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
            self.state = 92
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
            self.state = 95 
            self._errHandler.sync(self)
            _alt = 1+1
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1+1:
                    self.state = 94
                    self.matchWildcard()

                else:
                    raise NoViableAltException(self)
                self.state = 97 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PythonFileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FILEPATH(self):
            return self.getToken(Multi_Core_GrammarParser.FILEPATH, 0)

        def getRuleIndex(self):
            return Multi_Core_GrammarParser.RULE_pythonFile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPythonFile" ):
                listener.enterPythonFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPythonFile" ):
                listener.exitPythonFile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPythonFile" ):
                return visitor.visitPythonFile(self)
            else:
                return visitor.visitChildren(self)




    def pythonFile(self):

        localctx = Multi_Core_GrammarParser.PythonFileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_pythonFile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(Multi_Core_GrammarParser.FILEPATH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





