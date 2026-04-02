// -o-o-o-o- Hello World -o-o-o-o-

/* This is a simple hello world program written in C.
 * This file includes the stdio header which stands for
 * standard input and output. stdio is used to output/print
 * our output -> Hello, World.
 *
 * In order to print/output we must call the "printf" function
 * which will then print the text to the console. \n represents
 * a newline. C does not create newlines automatically so inorder to
 * skip to the newline we must invoke \n within the "" of our printf.
 *
 * # # # # KEY # # # #
 *
 * \n - creates a new line
 */

#include <stdio.h>

int main() {
  printf("Hello, World!\n");
  return 0;
}
