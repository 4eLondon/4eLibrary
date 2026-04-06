#include <stdio.h>

int main() {

  int a = 3;
  int *x = &a;

  printf("The value stored in variable A is %i\n", a);
  printf("A variable 'x' is a pointer that points to the address of variable "
         "A. Variable 'x' is equal to %i\n",
         *x);
  printf("The memory addres of variable A is %p\n", &a);

  return 0;
}
