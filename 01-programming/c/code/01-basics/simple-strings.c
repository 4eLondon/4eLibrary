// -o-o-o-o- Strings -o-o-o-o-

/* This file goes over the basics of strings in C simply.
 *
 * C does not have a dedicated string type. Instead strings are arrays
 * of chars that end with a special null terminator character '\0'.
 * C adds this null terminator automatically when you use double quotes.
 * It is what tells C where the string ends.
 *
 * Because strings are arrays they cannot be reassigned with = after
 * they are declared. Functions from string.h are used instead.
 *
 *  # # # # KEY # # # #
 *
 * \n - creates a new line
 *
 * %s - represents a string value that has to then be refered to
 * eg. printf("%s", string_here)
 *
 * %c - represents a single char value
 *
 * \0 - the null terminator. marks the end of a string. added automatically
 * when you use double quotes to define a string.
 *
 * strlen() - returns the number of characters in a string, not counting \0
 *
 * strcpy() - copies one string into another
 *
 * strcmp() - compares two strings. returns 0 if they are identical.
 *
 * Note: Always make your char array large enough to hold the string plus
 * the \0 at the end. "Hello" needs at least char[6] not char[5].
 * */

#include <stdio.h>
#include <string.h> // needed for strlen, strcpy and strcmp

int main() {

  // a string is a char array. the number in [] is the max size including \0
  char greeting[20] = "Hello, World!";
  char name[20] = "Alice";

  printf("Strings in C are char arrays that end with a null terminator.\n\n");

  printf("Greeting: %s\n", greeting);
  printf("Name: %s\n\n", name);

  // individual characters can be accessed just like array elements
  printf("First character of greeting: %c\n", greeting[0]);
  printf("Second character of greeting: %c\n\n", greeting[1]);

  // strlen returns the number of characters not counting the \0
  printf("Length of greeting is %lu characters\n", strlen(greeting));
  printf("Length of name is %lu characters\n\n", strlen(name));

  // strcpy copies a string into another char array
  char copy[20];
  strcpy(copy, name); // copies name into copy
  printf("Copied name into a new variable. Copy contains: %s\n\n", copy);

  // strcmp compares two strings and returns 0 if they match
  char wordOne[10] = "apple";
  char wordTwo[10] = "apple";
  char wordThree[10] = "orange";

  if (strcmp(wordOne, wordTwo) == 0) // 0 means the strings are identical
    printf("wordOne and wordTwo are the same.\n");

  if (strcmp(wordOne, wordThree) != 0) // not 0 means they are different
    printf("wordOne and wordThree are different.\n");

  return 0;
}
