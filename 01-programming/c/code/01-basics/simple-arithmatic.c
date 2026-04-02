// -o-o-o-o-o- SIMPLE ARITHMATIC -o-o-o-o-o-

/* This file goes over how to do basic arithmatic operations in C simply.
 *
 *  # # # # KEY # # # #
 *
 * \n - creates a new line
 * %i - represents and integer value that has to then be refered to
 * eg. printf("%i", varible_here)
 * */

#include <stdio.h>

int main(void) {
  int a = 4;
  int b = 2;
  int c = a + b;
  int d = a - b;
  int e = a / b;
  int f = a * b;

  printf("\nA number A is equal to %i\n", a);
  printf("A number B is equal to %i\n", b);
  printf("C is the result of A plus B. C is equal to %i\n", c);
  printf("D is the result of A minus B. D is equal to %i\n", d);
  printf("E is the result of A divided by B. E is equal to %i\n", e);
  printf("F is the result of A multiplied by B. F is equal to %i\n", f);
}
