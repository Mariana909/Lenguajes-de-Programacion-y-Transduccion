 /* wc_manual.c */
#include <stdio.h>
#include <ctype.h>
int main() {
    int chars = 0;
    int words = 0;
    int lines = 0;
    int in_word = 0;
    int c;

    while ((c = getchar()) != EOF) {
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

    printf("%8d%8d%8d\n", lines, words, chars);
    return 0;
}
