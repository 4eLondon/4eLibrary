// -o-o-o-o- Simple loops -o-o-o-o-

/* This file goes over how to do a basic while loop in C simply.
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
 * Note: The while loop checks to see if the variable meets the correct
 * requirements. if we used  while (a < 10) the loop would exit the instant too
 * early making 'a' 9 instead of 10. if we used while (a <= 10) the loop would
 * exit one instat too late making 'a' 11 instead of 10. a if statement was used
 * to check the moment 'a' becomes 10 and instatly exits using break to prevent
 * overflow.
 * */

#include <stdio.h>

int main() {

  int a = 0;

  // reads as -> while a is less than 10 -> run code in {}
  while (a <= 10) {
    printf("Variable A is equal to %i\n", a);

    if (a == 10)
      break; // This line exist to prevent over and underflow.
             // Break will exist the loop early if the required condition is
             // met.

    a++; // this adds 1 to the value of variable a
  }

  printf("Variable A is now equal to or less than 10. Variable A equals %i "
         "Loop complete \n",
         a);

  return 0;
}
