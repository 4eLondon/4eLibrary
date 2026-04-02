// -o-o-o-o- FORMAT SPECIFIERS -o-o-o-o-

/*
 * Format specifiers are a way of telling the program
 * how to output specific datatypes. Format specifiers always
 * begin with a % followed by a letter representing the datatype.
 *
 * The list of specifiers are as follows:
 * %e = Scientific notation (lowercase)
 * %u = Unsigned decimal integer
 * %i = Integer (same as %d)
 * %o = Octal integer
 * %p = Pointer address
 * %a = Hexadecimal floating point (lowercase)
 * %s = String of characters
 * %d = Signed decimal integer
 * %f = Floating point (decimal notation)
 * %g = Shorter of %e or %f
 * %x = Hexadecimal integer (lowercase)
 * %c = Single character
 * %b = Binary integer (C23 and later)
 * %n = Stores number of characters written so far into a pointer
 */

#include <stdio.h>

int main() {
  double a = 5.6;
  int b = 2;
  char c = (char)a;
  char d[] = "hello";

  printf("--- Float / Double ---\n");
  printf("%%f  decimal notation:         %f\n", a);
  printf("%%e  scientific notation:      %e\n", a);
  printf("%%g  shorter of %%e or %%f:      %g\n", a);
  printf("%%a  hex floating point:       %a\n", a);

  printf("\n--- Integer ---\n");
  printf("%%d  signed decimal:           %d\n", b);
  printf("%%i  integer (same as %%d):     %i\n", b);
  printf("%%u  unsigned decimal:         %u\n", b);
  printf("%%o  octal:                    %o\n", b);
  printf("%%x  hexadecimal (lowercase):  %x\n", b);
  printf("%%b  binary (C23+):            %b\n", b);

  printf("\n--- Character / String ---\n");
  printf("%%c  single character:         %c\n", c);
  printf("%%s  string:                   %s\n", d);

  printf("\n--- Pointer ---\n");
  printf("%%p  pointer address:          %p\n", (void *)&b);

  printf("\n--- Misc ---\n");
  int chars_written;
  printf("%%n  chars written so far: %n(stored, not printed)\n",
         &chars_written);
  printf("    Characters written before %%n: %d\n", chars_written);

  printf("\nWe represent decimals using either %%f or %%e or %%g\n");

  return 0;
}
