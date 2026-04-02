// -o-o-o-o- Simple loops (do while) -o-o-o-o-

/* This file goes over how to do a basic do while loops in C simply.
 *
 *  # # # # KEY # # # #
 *
 * \n - creates a new line
 * <= - less than or equal to
 * == - equal to
 * -- - decrement by 1
 *
 * %i - represents and integer value that has to then be refered to
 * eg. printf("%i", varible_here)
 * */

#include <stdio.h>

int main() {
  int a = 20;

  // code will run this loop so long as the while condtion is met
  do {
    printf("a is eqaual to %i\n", a);
    a--; // this line decreses a by one each cycle
  } while (a > 0);

  printf("Varaible A is now equal to %i. Do while loop complete.\n", a);

  return 0;
}
