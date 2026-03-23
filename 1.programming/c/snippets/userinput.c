#include <stdio.h>
int main() {
  char name[50];
  printf("Please enter your name: \n");
  scanf("%49s", name);
  printf("Your name is %s\n", name);
  return 0;
}
