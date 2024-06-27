grammar Multi_Core_Grammar;

// Parser rules
start: program EOF;

program: threadsNumber time code;

threadsNumber: threadST threads_no;
threadST: 'threads_number:';
time: bool;
code: forLoop* otherCode?;

forLoop: FOR variable IN (iterable|variable) COLON;

variable: IDENTIFIER;
iterable: IDENTIFIER | range;

range: RANGE LPAREN INTEGER (COMMA INTEGER)? RPAREN;
threads_no: INTEGER;
bool: BOOLEAN;
otherCode: .+; // Match all remaining code as a single node

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
DOT: '.';

WS: [ \t\r]+ -> skip;
NEWLINE: '\r'? '\n' -> skip;
