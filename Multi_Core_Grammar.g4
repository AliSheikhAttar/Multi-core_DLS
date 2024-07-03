grammar Multi_Core_Grammar;

// Parser rules
start: program EOF;

program: threadsNumber time (forLoop | pythonFile)*;

threadsNumber: threadST? threads_no;
threadST: 'threads_number:';
time: timeST? bool;
timeST: 'time:';

forLoop: FOR variable IN iterable COLON (forLoop | otherCode)*;

variable: IDENTIFIER;
iterable: IDENTIFIER | range;

range: RANGE LPAREN (from COMMA)? to RPAREN;
from: INTEGER;
to: INTEGER;
threads_no: INTEGER;
bool: BOOLEAN;
otherCode: .+?; // Match all remaining code as a single node

pythonFile: FILEPATH;

// Lexer rules
FOR: 'for';
IN: 'in';
RANGE: 'range';
COLON: ':';

LPAREN: '(';
RPAREN: ')';
COMMA: ',';

BOOLEAN: 'true' | 'false';
INTEGER: [0-9]+;
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;
FILEPATH: ('/' | '\\')? (IDENTIFIER ('/' | '\\'))* IDENTIFIER '.py';
DOT: '.';
INDENT: '\t';

WS: [ \t\r]+ -> skip;
NEWLINE: '\r'? '\n' -> skip;
