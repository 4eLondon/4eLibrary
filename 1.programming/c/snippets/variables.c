#include <stdio.h>

int main() {

  int number = 7;
  float decimal = 3.14;
  char character = 'A';
  char string[10] = "Hello";

  printf("This is a number: %i\n", number);
  printf("This is a character: %c\n", character);
  printf("This is a decimal: %.1f\n", decimal);
  printf("This is a string: %s\n", string);

  return 0;
}
