grammar ExampleDSL;

start: program EOF;



program: threads_number? time? code_address ;

threads_number : INTEGER ;


code_address : STRING ;

INTEGER: '0' | [1-9]+ [0-9]*;
STRING : [A-Ba-z]+;
WS: [ \t\r]+ -> skip;
NEWLINE: ('\n' | '\r\n' | '\r') -> skip;

