# Generated from /home/asa/Code/Git/Multi-core_DLS/Multi_Core_Grammar.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,5,56,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,3,0,21,8,0,1,1,1,1,4,1,25,8,1,11,1,12,
        1,26,1,1,5,1,30,8,1,10,1,12,1,33,9,1,3,1,35,8,1,1,2,4,2,38,8,2,11,
        2,12,2,39,1,3,4,3,43,8,3,11,3,12,3,44,1,3,1,3,1,4,1,4,1,4,1,4,3,
        4,53,8,4,1,4,1,4,0,0,5,1,1,3,2,5,3,7,4,9,5,1,0,4,1,0,49,57,1,0,48,
        57,2,0,65,66,97,122,3,0,9,9,13,13,32,32,63,0,1,1,0,0,0,0,3,1,0,0,
        0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,1,20,1,0,0,0,3,34,1,0,0,0,
        5,37,1,0,0,0,7,42,1,0,0,0,9,52,1,0,0,0,11,12,5,116,0,0,12,13,5,114,
        0,0,13,14,5,117,0,0,14,21,5,101,0,0,15,16,5,102,0,0,16,17,5,97,0,
        0,17,18,5,108,0,0,18,19,5,115,0,0,19,21,5,101,0,0,20,11,1,0,0,0,
        20,15,1,0,0,0,21,2,1,0,0,0,22,35,5,48,0,0,23,25,7,0,0,0,24,23,1,
        0,0,0,25,26,1,0,0,0,26,24,1,0,0,0,26,27,1,0,0,0,27,31,1,0,0,0,28,
        30,7,1,0,0,29,28,1,0,0,0,30,33,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,
        0,32,35,1,0,0,0,33,31,1,0,0,0,34,22,1,0,0,0,34,24,1,0,0,0,35,4,1,
        0,0,0,36,38,7,2,0,0,37,36,1,0,0,0,38,39,1,0,0,0,39,37,1,0,0,0,39,
        40,1,0,0,0,40,6,1,0,0,0,41,43,7,3,0,0,42,41,1,0,0,0,43,44,1,0,0,
        0,44,42,1,0,0,0,44,45,1,0,0,0,45,46,1,0,0,0,46,47,6,3,0,0,47,8,1,
        0,0,0,48,53,5,10,0,0,49,50,5,13,0,0,50,53,5,10,0,0,51,53,5,13,0,
        0,52,48,1,0,0,0,52,49,1,0,0,0,52,51,1,0,0,0,53,54,1,0,0,0,54,55,
        6,4,0,0,55,10,1,0,0,0,8,0,20,26,31,34,39,44,52,1,6,0,0
    ]

class Multi_Core_GrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    TIME = 1
    INTEGER = 2
    STRING = 3
    WS = 4
    NEWLINE = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "TIME", "INTEGER", "STRING", "WS", "NEWLINE" ]

    ruleNames = [ "TIME", "INTEGER", "STRING", "WS", "NEWLINE" ]

    grammarFileName = "Multi_Core_Grammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


