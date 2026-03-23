#include <stdio.h>
int main() {

  int num, num2;

  printf("Enter a number: ");
  scanf("%i", &num);
  printf("Enter another number: ");
  scanf("%i", &num2);

  printf("%i + %i = %i\n", num, num2, num + num2);
  printf("%i - %i = %i\n", num, num2, num - num2);
  printf("%i * %i = %i\n", num, num2, num * num2);
  printf("%i / %i = %i\n", num, num2, num / num2);
  return 0;
}
