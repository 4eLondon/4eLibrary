// -o-o-o-o- Conditions (switches) -o-o-o-o-

/* This file goes over the basic of switches and cases in C simply.
 *
 *  # # # # KEY # # # #
 *
 * \n - creates a new line
 *
 * %i - represents and integer value that has to then be refered to
 * eg. printf("%i", varible_here)
 *
 * switch - checks the value of a integer variable and creates diffrent cased
 * based on specific values. swtiches operate simular to if else conditions.
 *
 * case - a set of instructions that run if and only if the correct int value is
 * true
 *
 * break - this function is used to exit loops and switches early. in this case
 * it exits the switch istantly the moment a case is met.
 *
 * defualt - this is a fallback case. it only runs if no other case is true. it
 * is recommended to include this.
 * */

#include <stdio.h>
int main() {

  int a;

  printf("Please enter a number between 0 and 5: ");
  scanf("%i", &a);

  switch (a) {

  case 0: // if the variable is equal to 0 then
    printf("Variable A is eqaul to 0\n");
    break; // exit switch immediately

  case 1:
    printf("Variable A is eqaul to 1\n");
    break;

  case 2:
    printf("Variable A is eqaul to 2\n");
    break;

  case 3:
    printf("Variable A is eqaul to 3\n");
    break;

  case 4:
    printf("Variable A is eqaul to 4\n");
    break;

  case 5:
    printf("Variable A is eqaul to 5\n");
    break;

  default: // runs if no other case is true
    printf(
        "\nERROR - Your number was outside of the range. Number must be equal "
        "to zero,five or between the two.\n");
    break;
  }
  return 0;
}
