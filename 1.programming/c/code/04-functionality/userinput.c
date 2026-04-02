// -o-o-o-o- USER INPUT -o-o-o-o-

/* This file covers the basics of getting user input.
 * scanf is a baisc function within C's Standard library that reads input from
 * the user. In this example we utilize scanf to read user input then assign it
 * to the name variable before outputting the value of name with printf.
 *
 */

#include <stdio.h>

int main() {
  char name[50]; // create name variable
  printf("Please enter your name: \n");
  scanf("%49s", name); // read input and assign it to name variable
  printf("Your name is %s\n", name);
  return 0;
}
