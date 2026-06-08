// -o-o-o-o- Functions -o-o-o-o-

/* This file goes over the basics of functions in C simply.
 *
 * Functions are reusable blocks of code that perform a specific task.
 * Instead of writing the same code over and over, you write it once
 * inside a function and call it whenever you need it.
 *
 * A function must be defined before it is called. If you want to define
 * it after main() you must forward declare it above main using a
 * function prototype.
 *
 *  # # # # KEY # # # #
 *
 * \n - creates a new line
 *
 * %i - represents an integer value that has to then be refered to
 * eg. printf("%i", varible_here)
 *
 * return type - the data type the function will hand back when it finishes.
 * eg. int means it returns a whole number. void means it returns nothing.
 *
 * void - used as a return type when a function does not return a value.
 *
 * return - exits the function and hands a value back to whoever called it.
 *
 * function prototype - a forward declaration that tells C a function exists
 * before its full definition appears in the file.
 *
 * Note: main() itself is a function. Every function follows the same
 * structure -> return type, name, parentheses, then a block of code in {}.
 * */

#include <stdio.h>

// function prototype - tells C this function exists before we define it below
int add(int a, int b);
void greet(void);

int main() {

  printf("Functions let you write reusable blocks of code.\n\n");

  greet(); // calling a void function. it runs its code and returns nothing.

  // calling the add function and storing the result in a variable
  int result = add(4, 6);
  printf("Calling add(4, 6) returns %i\n", result);

  // the return value can also be used directly without storing it
  printf("Calling add(10, 25) directly returns %i\n", add(10, 25));

  return 0;
}

// a void function - performs a task but does not return a value
void greet(void) {
  printf("Hello from inside a function!\n\n");
}

// a function that takes two integers and returns their sum
// 'a' and 'b' are parameters - they are the inputs the function expects
int add(int a, int b) {
  return a + b; // return hands the result back to whoever called the function
}
