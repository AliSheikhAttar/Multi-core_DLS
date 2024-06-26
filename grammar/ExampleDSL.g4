grammar ExampleDSL;

start: program EOF;



program: threads_number? time? code_address ;
threads_number : INTEGER ;
time: TIME;


TIME: 'true' | 'false' ;
INTEGER: '0' | [1-9]+ [0-9]*;
WS: [ \t\r]+ -> skip;
NEWLINE: ('\n' | '\r\n' | '\r') -> skip;

