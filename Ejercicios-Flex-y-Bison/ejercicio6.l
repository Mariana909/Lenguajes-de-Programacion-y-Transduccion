%{
int chars = 0;
int words = 0;
int lines = 0;
%}
%%
[a-zA-Z]+  { words++; chars += strlen(yytext); }
\n         { chars++; lines++; }
.          { chars++; }
%%

int main(int argc, char **argv)
{
  if (argc > 1) {
    FILE *file = fopen(argv[1], "r");
    if (file == NULL) {
      fprintf(stderr, "Error: no se pudo abrir el archivo '%s'\n", argv[1]);
      return 1;
    }
    yyin = file;   /* yyin es el puntero de entrada de Flex */
  }
  /* Si no se pasa archivo, lee desde stdin como antes */

  yylex();
  printf("Líneas: %8d\nPalabras: %8d\nCaracteres: %8d\n", lines, words, chars);

  if (argc > 1) {
    fclose(yyin);
  }

  return 0;
}
