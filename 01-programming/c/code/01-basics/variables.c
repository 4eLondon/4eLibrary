// -o-o-o-o- VARIABLES -o-o-o-o-

/* C handles variables simply. First we have a data type followed by a name then
 * a value.
 *
 * The most common data types youll encounter are:
 * int - integers aka whole numbers
 * char - single characters/letters
 * float - floating point aka decimals numbers
 * double - More precise decimal values
 *
 * Strings do not exist in C. Strings are instead char arrays, each letter of a
 * word is stored as a char that combine to create strings.
 *
 * Note that chars are noted by single quotes ('') while strings user double
 * quotes ("").
 *
 * # # # # KEY # # # #
 *
 * %i - used to represent integer values
 * %c - used to represent characters
 * %s - used to represent strings
 * %f - used to represent floating values
 * \n - creates a new line
 * */

#include <stdio.h>

int main() {

  // The basic variable types are seen below:
  int number = 7;
  float decimal = 3.14;
  double pi = 3.141592653589793;
  char character = 'A';
  char string[10] = "Hello"; // an array of chars make a string. this one can
                             // hold 10 letters/chars

  // This section prints the variables. See format specifiers for notes on the
  // symbols such as %i and %s
  printf("This is a int, It is used for whole numbers both positive and "
         "negative: %i\n",
         number);
  printf("This is a char, It is used for single characters: %c\n", character);
  printf("This is a float, It is used for decimal values: %g\n", decimal);
  printf("This is a double, It is used for precise decimal values: %f\n", pi);
  printf("This is a string, It is used for words: %s\n", string);

  return 0;
}
