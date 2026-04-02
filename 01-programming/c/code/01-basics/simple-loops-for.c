// -o-o-o-o- Simple loops (for) -o-o-o-o-

/* This file goes over how to do a basic for loop in C simply.
 *
 *  # # # # KEY # # # #
 *
 * \n - creates a new line
 * <= - less than or equal to
 * == - equal to
 * ++ - increment by 1
 *
 * %i - represents and integer value that has to then be refered to
 * eg. printf("%i", varible_here)
 *
 * break - this function is used to exit loops and switches early.
 *
 * Note: The loop checks to see if the variable meets the correct
 * requirements.
 * once the variable 'a' reaches 50 it will icrement a final time and become 51
 * before the loop exists. a if statement with a break ensures the varaible a
 * never overflows and the loop stops the instat 'a' is equal to 50 rather than
 * incrementing an additonal time.
 * */

#include <stdio.h>

int main() {
  int a;

  // reads as -> a is equal to 0 -> so long as a is less than or equal to 50 ->
  // add 1 to 'a'
  for (a = 0; a <= 50; a++) {
    printf("a = %i\n", a);
    if (a == 50) // this line exists the loop the momement 'a' = 50
      break;
  }
  printf("Varaible A is now equal to %i. For loop complete.\n", a);
  return 0;
}
