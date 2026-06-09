// -o-o-o-o- Conditions (If else) -o-o-o-o-

/* This file goes over how to do a basic if else statement in C# simply.
 *
 *  # # # # KEY # # # #
 *
 * \n - creates a new line (also Console.WriteLine() does this automatically)
 *
 * != - not equal to operator
 * == - equal to operator
 *
 * Note: = is the assign operator, it is used to assign values to variables.
 * == means equal to and is used for conditional statements. Never use a single =
 * to check for conditions such as if a variable is equal to a certain value.
 *
 * Console.WriteLine() - prints text to the console with a newline at the end.
 *                       equivalent to printf("...\n") in C.
 *
 * Console.Write()     - prints text WITHOUT a newline at the end.
 *                       equivalent to printf("...") in C (no \n).
 *
 * Console.ReadLine()  - reads a line of text input from the user as a string.
 *                       equivalent to scanf() in C.
 *
 * int.Parse()         - converts a string into an integer.
 *                       needed because Console.ReadLine() always returns a string.
 *                       eg. int a = int.Parse(Console.ReadLine());
 *
 * int                 - declares an integer variable, same as in C.
 *
 * */

using System;

class Program {
    static void Main() {

        int a;
        Console.Write("Please enter either 0 or 1: ");
        a = int.Parse(Console.ReadLine()); // Gets user input and converts it to an int

        // reads as -> If a is not equal to 0 -> run code in {}
        if (a != 0) {
            Console.WriteLine("Variable A is equal to 1. You get a treat");
        }

        // checks if the above if statement is true and only runs if it is not true.
        else {
            Console.WriteLine("Variable A is not equal to 1. You get no treats");
        }

    }
}
