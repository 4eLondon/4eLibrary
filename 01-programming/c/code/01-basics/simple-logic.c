// -o-o-o-o- Simple logic -o-o-o-o-

/* This file goes over how to do a basic if else statements in C simply.
 *
 *  # # # # KEY # # # #
 *
 * \n - creates a new line
 * &* - assigns a value to a variable where * is the variabe name
 *
 * != - not equal to operator
 * == - equal to operator
 *
 * Note: = is the asign operator, it is used to assign values to variables.
 * == means equal to and is used for conditonal statments. Never use a single =
 * to check for condions such as if a varaible is equal to a certain value.
 *
 * %i - represents and integer value that has to then be refered to
 * eg. printf("%i", varible_here)
 *
 * scanf is used to get user input.
 * eg scanf("%*",&variable-here) where * is the format selector/data type.
 *
 * */

#include <stdio.h>

int main() {

  int a;
  printf("Plese enter either 0 or 1: ");
  scanf("%i", &a); // This gets user input and assigns an int to variable a

  // reads as -> If a is eqaul to 0 -> run code in {}
  if (a != 0) {
    printf("Variable A is equal to 1. You get a treat\n");
  }

  // checks if the above if statement is true and only runs if is not true.
  else {
    printf("Variable A is not equal to 1. You get no treats\n");
  }

  return 0;
}
