grammar Multi_Core_Grammar;

start: program EOF;



program: threads_number? time? code_address ;
threads_number : INTEGER ;
time: TIME;

code_address : STRING ;


TIME: 'true' | 'false' ;
INTEGER: '0' | [1-9]+ [0-9]*;
STRING : [A-Ba-z]+;
WS: [ \t\r]+ -> skip;
NEWLINE: ('\n' | '\r\n' | '\r') -> skip;

