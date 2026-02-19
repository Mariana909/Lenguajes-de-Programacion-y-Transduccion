/* wc_manual.c */
#include <stdio.h>
#include <ctype.h>

int main(int argc, char **argv) {
    int chars = 0;
    int words = 0;
    int lines = 0;
    int in_word = 0;
    int c;
    FILE *input;

    if (argc > 1) {
        input = fopen(argv[1], "r");
        if (input == NULL) {
            fprintf(stderr, "Error: no se pudo abrir el archivo '%s'\n", argv[1]);
            return 1;
        }
    } else {
        input = stdin;  /* Si no se pasa archivo, lee desde stdin */
    }

    while ((c = fgetc(input)) != EOF) {
        chars++;
        
        if (c == '\n') {
            lines++;
        }
        
        if ((c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z')) {
            if (!in_word) {
                words++;
                in_word = 1;
            }
        } else {
            in_word = 0;
        }
    }

    printf(" %8d\n    %8d\n  %8d\n", lines, words, chars);

    if (input != stdin) {
        fclose(input);
    }

    return 0;
}
