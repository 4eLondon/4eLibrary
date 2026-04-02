// -o-o-o-o- ARITHMATIC OPERATORS -o-o-o-o-

/* This file covers the basics of simple arithmatic in C.
 * Addtion, Subtraction, Division and Multiplication are covered.
 * Format specifiers are used to represnt data types in our output. In C we
 * can not simply plug a variable into a print statement, we must first assign
 * it a format specifier such as %i to represnt a interger value.
 *
 * Outside of our "" we then list the variables in order you wish for them to
 * appear.
 *
 * Eg. if we have
 * int num1 = 1
 * int num2 = 2
 * printf("The first number is %i and the second number is %i",num2,num1)
 *
 * Num 1 will appear after num 2 because that was what was specified.
 */

#include <stdio.h>
int main() {
  int num, num2;              // Initialize variabes for numbers
  printf("Enter a number: "); // This section prompts the user for input
  scanf("%i", &num);          // User input saved to the variable num.
  printf("Enter another number: ");
  scanf("%i", &num2);

  // This section prints the outcome of operations
  printf("%i + %i = %i\n", num, num2, num + num2);
  printf("%i - %i = %i\n", num, num2, num - num2);
  printf("%i * %i = %i\n", num, num2, num * num2);
  printf("%i / %i = %i\n", num, num2, num / num2);
  return 0;
}
