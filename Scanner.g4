antlr -visitor -no-listener Parser.g4
javac *.java
grun Parser program test.cl -gui -tokens


javac Main.java
java Main


antlr -visitor -no-listener -o dist ./Parser.g4
javac -cp ./dist:/JavaLib/antlr-4.10.1-complete.jar Main.java
java -cp ./dist Main





grammar scanner;	


NEWLINE: '\r'? '\n' -> skip;
WS: [ \n\t\r]+ -> skip;
SINGLECOMMENT: '--' ~[\r\n]* -> skip;
MULTICOMMENT: '(*' .*? '*)' -> skip;

TYPE: [A-Z_][_A-Za-z0-9]*;
ID: [a-z_][_A-Za-z0-9]*;
INT: [0-9]+;
SEMICOLON: ';';

TRUE: 'true';
FALSE: 'false';
CLASS: 'class' | 'CLASS';
FI: 'fi' | 'FI';
IF: 'if' | 'IF';
IN: 'in' | 'IN';
INHERITS: 'inherits' | 'INHERITS';
ISVOID: 'isvoid' | 'ISVOID';
LET: 'let' | 'LET';
LOOP: 'loop' | 'LOOP';
POOL: 'pool' | 'POOL';
THEN: 'then' | 'THEN';
ELSE: 'else' | 'ELSE';
WHILE: 'while' | 'WHILE';
CASE: 'case' | 'CASE';
NEW: 'new' | 'NEW';
OF: 'of' | 'OF';
NOT: 'not' | 'NOT';

LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
COLON: ':';
ASSIGN: '<-';
DARROW: '=>';
NEG: '~';
COMMA: ',';
PERIOD: '.';
AT: '@';
MUL: '*';
ADD: '+';
MINUS: '-';
DIV: '/';
LT: '<';
LEQUALS: '<=';
EQUALS: '=';
ERROR: . ;
STRING: '"' ( ESC | .)*? '"';

fragment ESC: '\\"' | '\\\\';
