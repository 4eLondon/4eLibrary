// -o-o-o-o- Simple Loops (Do While) -o-o-o-o-

/* This file goes over the basic do-while loop in C# simply.
 *
 *  # # # # KEY # # # #
 *
 * do while - a loop that executes its code block FIRST, then checks the condition.
 *            This guarantees the code inside runs AT LEAST ONCE, even if the
 *            condition is false from the start.
 *
 *            Syntax:
 *            do {
 *                // code to run
 *            } while (condition);
 *
 *            The semicolon after while(...) is REQUIRED. Same rule as in C.
 *
 * while   - the condition checked AFTER each loop iteration.
 *           The loop continues as long as the condition is true.
 *
 * ++      - increment operator. Adds 1 to a variable.
 *           eg. i++ is the same as i = i + 1
 *
 * Console.WriteLine() - prints text to the console with a newline at the end.
 *
 * Console.ReadLine()  - reads a line of user input as a string.
 *
 * int.Parse()         - converts a string to an integer.
 *
 * Note: do-while is useful for input validation — ask the user at least once,
 *       then keep asking until they enter a valid value.
 *
 * */

using System;

class Program {
    static void Main() {

        // Basic do-while: runs at least once
        int i = 0;
        Console.WriteLine("Counting with do-while:");
        do {
            Console.WriteLine($"i = {i}");
            i++;
        } while (i < 5); // checks AFTER the code block runs

        // Practical example: input validation loop
        // Keeps asking until the user enters a number between 1 and 10
        int userInput;
        do {
            Console.Write("\nEnter a number between 1 and 10: ");
            userInput = int.Parse(Console.ReadLine());

            if (userInput < 1 || userInput > 10) {
                Console.WriteLine("Invalid. Please try again.");
            }

        } while (userInput < 1 || userInput > 10);

        Console.WriteLine($"You entered: {userInput}");

    }
}
