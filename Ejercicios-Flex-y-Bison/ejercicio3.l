/* Calculadora Hexadecimal - Decimal con Operadores Lógicos */
%{
#include "ejercicio3.tab.h"
%}
%%
"+"    { return ADD; }
"-"    { return SUB; }
"*"    { return MUL; }
"/"    { return DIV; }
"|"    { return '|'; }
"&"    { return AND; }
"^"    { return XOR; }
"~"    { return NOT; }
"<<"   { return LEF; }
">>"   { return RIG; }
"("    { return '('; }
")"    { return ')'; }
/* Modificación que incluye a los números hexadecimales */}
0[xX][0-9a-fA-F]+ { yylval = strtol(yytext, NULL, 16); return NUMBER; }
[0-9]+ { yylval = atoi(yytext); return NUMBER; 
\n     { return EOL; }
[ \t]  { /* ignore whitespace */ }
.      { printf("Mystery character %c\n", *yytext); }
%%
