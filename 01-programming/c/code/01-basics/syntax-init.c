//  -o-o-o-o-o- C File Initialization -o-o-o-o-o-

/* In C there are a few things to include in most files.
 *
 * #include is where we include different libraries and components.
 * Certain components are needed in order to perform specific tasks.
 * <stdio.h> for example allows the file to use input and output
 * functions, such as the printf() function which prints output.
 *
 * int main() is the main entry point for our program.
 * There can only be one main function.
 *
 * int  = this means the function will return an integer value.
 *        0 means success and non-zero means an error more often than not.
 * main = the name C expects for the entry point. No other function
 *        should use this name as the program starts here.
 * ()   = function arguments go here. We will leave this blank for now.
 *        Void is a common arguement used in the main function as it means no
 * arguments are expected. The main function typically does not expect one
 * anyway.
 * {}   = this is where the bulk of our code goes. Program
 *        behavior and output all go inside these brackets.
 *
 * return 0; marks the end of the program and returns a success
 * status to the operating system. In modern C, this is optional,
 * but it is recommended as good practice.
 */

#include <stdio.h>

int main(void) {
  printf("Hello");
  return 0;
}
