/* Project: echo input
   What it does: asks the user for their name and age, then prints them back
   Run: gcc main.c -o echo && ./echo */

#include <stdio.h>

int main() {
    char name[50];
    char age[10];

    printf("Enter your name: ");
    fgets(name, sizeof(name), stdin);

    printf("Enter your age: ");
    fgets(age, sizeof(age), stdin);

    printf("\nYou entered:\n");
    printf("  Name: %s", name);
    printf("  Age:  %s", age);

    return 0;
}
