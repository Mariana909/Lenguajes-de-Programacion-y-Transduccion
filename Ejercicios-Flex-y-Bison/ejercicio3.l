/* Calculadora Hexadecimal - Decimal con Operadores Lógicos */
%{
#include <ejercicio2.tab.h>
%}
%%
"+"    { return ADD; }
"-"    { return SUB; }
"*"    { return MUL; }
"/"    { return DIV; }
"|"    { return ABS; }
"||"   { return OR; } /* Ya que flex tiene en cuenta la coincidencia más larga, no hay conflicto con ABS */
"&"    { return AND; }
"^"    { return XOR; }
"~"    { return NOT; }
[0-9]+ { yylval = atoi(yytext); return NUMBER; }
/* Modificación que incluye a los números hexadecimales */
0x[a-f0-9]+ {yyval = strol(yytext, NULL, 16); return NUMBER}
\n     { return EOL; }
[ \t]  { /* ignore whitespace */ }
.      { printf("Mystery character %c\n", *yytext); }
%%
