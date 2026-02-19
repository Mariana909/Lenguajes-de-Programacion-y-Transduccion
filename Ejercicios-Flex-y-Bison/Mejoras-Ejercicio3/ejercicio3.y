/* simplest version of calculator */
%{
#include <stdio.h>
int yylex();
void yyerror(char *s);
extern FILE *yyin;
%}
/* declare tokens */
%token NUMBER
%token ADD SUB MUL DIV AND XOR NOT LEF RIG
%token ABS_OPEN ABS_CLOSE OR
%token EOL

%left OR
%left XOR
%left AND
%left LEF RIG
%left ADD SUB
%left MUL DIV
%right NOT

%%
calclist: /* nothing */                       
 | calclist orbit EOL { printf("= %d (0x%X)\n", $2, $2); }
 | calclist EOL
 ;
orbit: xorbit
 | orbit OR xorbit { $$ = $1 | $3; }
 ;
xorbit: andbit
 | xorbit XOR andbit { $$ = $1 ^ $3; }
 ;
andbit: desp
 | andbit AND desp { $$ = $1 & $3; }
 ;
desp: exp
 | desp LEF exp { $$ = $1 << $3; }
 | desp RIG exp { $$ = $1 >> $3; }
 ;
exp: factor       
 | exp ADD factor { $$ = $1 + $3; }
 | exp SUB factor { $$ = $1 - $3; }
 ;
factor: term       
 | factor MUL term { $$ = $1 * $3; }
 | factor DIV term { 
         if ($3 != 0) {
            $$ = $1 / $3;
         } else { 
            yyerror("División por cero");
            $$ = 0;
         } 
     }
 ;
term: NUMBER  
 | NOT term                 { $$ = ~$2; }
 | SUB term                 { $$ = -$2; }
 | '(' orbit ')'            { $$ = $2; }
 | ABS_OPEN orbit ABS_CLOSE { $$ = $2 >= 0 ? $2 : -$2; }
 ;
%%
int main(int argc, char **argv) {
    if (argc > 1) {
        yyin = fopen(argv[1], "r");
        if (!yyin) {
            fprintf(stderr, "Error: No se puede abrir el archivo '%s'\n", argv[1]);
            return 1;
        }
        printf("Procesando archivo: %s\n\n", argv[1]);
    } else {
        printf("Calculadora - Ctrl+D para salir\n");
        yyin = stdin;
    }
    
    yyparse();
    
    if (yyin != stdin) {
        fclose(yyin);
    }
    
    return 0;
}
void yyerror(char *s) {
    fprintf(stderr, "Error: %s\n", s);
}
