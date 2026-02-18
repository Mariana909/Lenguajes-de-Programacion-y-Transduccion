/* simplest version of calculator */
%{
#include <stdio.h>
%}
/* declare tokens */
%token NUMBER
%token ADD SUB MUL DIV AND XOR NOT LEF RIG
%token EOL
%%
calclist: /* nothing */                       
 | calclist orbit EOL { printf("= %d (0x%x\n", $2); } /* EOL is end of an expression */
 | calclist EOL
 ;
orbit: xorbit
 | orbit '|' xorbit { $$ = $1 | $3; }
xorbit: andbit
 | xorbit XOR andbit { $$ = $1 ^ $3; }
andbit: desp
 | andbit AND desp { $$ = $1 & $3; }
desp: exp
 | desp LEF exp { $$ = $1 << $3; }
 | desp RIG exp { $$ = $1 >> $3; }
exp: factor       
 | exp ADD factor { $$ = $1 + $3; }
 | exp SUB factor { $$ = $1 - $3; }
 ;
factor: notbit       
 | factor MUL term { $$ = $1 * $3; }
 | factor DIV term { $$ = $1 / $3; }
 ;
term: NUMBER  
 | NOT term   { $$ = ~$2; }
 | "(" term ")" { $$ = $2; }
 | "|" term "|"  { $$ = $2 >= 0? $2 : - $2; }
;
%%
main(int argc, char **argv)
{
  yyparse();
}
yyerror(char *s)
{
  fprintf(stderr, "error: %s\n", s);
}
