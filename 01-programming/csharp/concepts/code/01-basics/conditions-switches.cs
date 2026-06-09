// -o-o-o-o- Conditions (Switches) -o-o-o-o-

/* This file goes over the basics of switches and cases in C# simply.
 *
 *  # # # # KEY # # # #
 *
 * \n - creates a new line (also Console.WriteLine() does this automatically)
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
 * switch - checks the value of a variable and creates different cases
 *          based on specific values. Switches operate similar to if else conditions.
 *          In C#, switch works with int, string, char, and more (unlike C).
 *
 * case - a set of instructions that run if and only if the correct value is
 *        matched.
 *
 * break - exits the switch immediately once a case is met.
 *         required in C# just like in C — without it you get a compile error
 *         (C# does NOT allow case fall-through, unlike C).
 *
 * default - this is a fallback case. It only runs if no other case is true.
 *           It is recommended to always include this.
 *
 * */

using System;

class Program {
    static void Main() {

        int a;

        Console.Write("Please enter a number between 0 and 5: ");
        a = int.Parse(Console.ReadLine());

        switch (a) {

            case 0: // if the variable is equal to 0 then
                Console.WriteLine("Variable A is equal to 0");
                break; // exit switch immediately

            case 1:
                Console.WriteLine("Variable A is equal to 1");
                break;

            case 2:
                Console.WriteLine("Variable A is equal to 2");
                break;

            case 3:
                Console.WriteLine("Variable A is equal to 3");
                break;

            case 4:
                Console.WriteLine("Variable A is equal to 4");
                break;

            case 5:
                Console.WriteLine("Variable A is equal to 5");
                break;

            default: // runs if no other case is true
                Console.WriteLine(
                    "\nERROR - Your number was outside of the range. Number must be equal " +
                    "to zero, five or between the two.");
                break;
        }

    }
}
