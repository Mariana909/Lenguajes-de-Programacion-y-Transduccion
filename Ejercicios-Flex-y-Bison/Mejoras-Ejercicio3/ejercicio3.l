/* Calculadora Hexadecimal - Decimal con Operadores Lógicos */
%{
#include "ejercicio3.tab.h"
/* Estados para manejar | ambiguo */
int abs_depth = 0;        /* nivel de anidamiento de valor absoluto */
int expect_operand = 1;   /* 1 si esperamos un operando (inicio o tras operador) */
%}
%%
"+"    { expect_operand = 1; return ADD; }
"-"    { expect_operand = 1; return SUB; }
"*"    { expect_operand = 1; return MUL; }
"/"    { expect_operand = 1; return DIV; }
"&"    { expect_operand = 1; return AND; }
"^"    { expect_operand = 1; return XOR; }
"~"    { expect_operand = 1; return NOT; }
"<<"   { expect_operand = 1; return LEF; }
">>"   { expect_operand = 1; return RIG; }
"("    { expect_operand = 1; return '('; }
")"    { expect_operand = 0; return ')'; }
"|"  {
    if (expect_operand) {
        abs_depth++;
        expect_operand = 1;
        return ABS_OPEN;
    } else {
        if (abs_depth > 0) {
            abs_depth--;
            expect_operand = 0;
            return ABS_CLOSE;
        } else {
            expect_operand = 1;
            return OR;
        }
    }
}
0[xX][0-9a-fA-F]+      { yylval = strtol(yytext, NULL, 16); expect_operand = 0; return NUMBER; }
[0-9]+[a-wyzA-WYZ_][^\n]*  { fprintf(stderr, "Línea ignorada: %s\n", yytext); }
[0-9]+                 { yylval = atoi(yytext); expect_operand = 0; return NUMBER; }
\n     { expect_operand = 1; return EOL; }
[ \t]  { /* ignore whitespace */ }
[a-zA-Z_][a-zA-Z0-9_.:]*  { fprintf(stderr, "Ignorado: %s\n", yytext); }
.                          { fprintf(stderr, "Carácter desconocido: %c\n", *yytext); }
%%
