/*                      - + - Command line arguments - + -
 
    Definition: Command line to arguments allow us to pass extra information to our program when it is ran from the terminal. They are implemented by adding the (int argc, char *argv[]) flags to our main C function.
 
    argc = This is the argument count. It tells us how many arguments were passed including the program name itself.

    argv = This is a vector that stores the arguments themselves. argv[0] will always be the program name so if the program is called "hello.c" then argv[0] will equal "./hello" after the program is ran.

    Usage: Typilcally commandline arguments are used to make programs my interactive rather than hardcoded with a single purpose in mind. Think of basic terminal command such as ls that hold the abiliy to list the contents in a folder. We can pass arguments to ls such as ~/home/download/mysongs and ls can remotly list the contents of that file using our defined argument.
 */

#include<stdio.h>

int main(int argc, char *argv[]){

    // The program will print each argument in order
    for (int i; i < argc; i++) {
        printf("arg %d: %s\n",i,argv[i]);
    }
    return 0;
}
