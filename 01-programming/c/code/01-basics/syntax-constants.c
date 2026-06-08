// -o-o-o-o- Constants -o-o-o-o-

/* This file goes over the basics of constants in C simply.
 *
 * Constants are values that cannot be changed after they are defined.
 * They are useful for values you know will never need to change such as
 * the value of pi or a max score in a game. Using constants instead of
 * raw numbers makes your code easier to read and update.
 *
 * There are two common ways to define constants in C:
 * const  - a typed constant variable. enforced by the compiler.
 * #define - a preprocessor macro. replaced with its value before compiling.
 *
 *  # # # # KEY # # # #
 *
 * \n - creates a new line
 *
 * %i - represents an integer value that has to then be refered to
 * eg. printf("%i", varible_here)
 *
 * const - a keyword placed before a variable type that prevents the value
 * from being changed after it is set.
 *
 * #define - a preprocessor directive that replaces a name with a value
 * everywhere it appears in the file before the code is compiled.
 * #define does not use = and does not end with a semicolon.
 *
 * Note: By convention constants are written in UPPER_SNAKE_CASE to make
 * them easy to spot and distinguish from regular variables.
 *
 * Note: const is generally preferred over #define in modern C as it is
 * typed and understood by the compiler, making it safer to use.
 * */

#include <stdio.h>

// #define constants are defined outside of functions at the top of the file
// the preprocessor swaps MAX_SCORE for 100 everywhere before compiling
#define MAX_SCORE 100
#define APP_NAME "MyProgram"

int main() {

  // const constants are declared like variables but with const in front
  // attempting to change these values later will cause a compiler error
  const float PI = 3.14159f;
  const int LIVES = 3;

  printf("Constants are values that cannot be changed after being set.\n\n");

  printf("const float PI is equal to %f\n", PI);
  printf("const int LIVES is equal to %i\n\n", LIVES);

  printf("#define MAX_SCORE is equal to %i\n", MAX_SCORE);
  printf("#define APP_NAME is equal to %s\n\n", APP_NAME);

  // constants can be used anywhere a normal variable can be used
  int playerScore = 85;
  printf("Player scored %i out of a maximum of %i\n", playerScore, MAX_SCORE);

  return 0;
}
