// -o-o-o-o- Simple Loops (While) -o-o-o-o-

/* This file goes over the basic while loop in C# simply.
 *
 *  # # # # KEY # # # #
 *
 * while loop - a loop that repeats a block of code AS LONG AS a condition is true.
 *              The condition is checked BEFORE each iteration.
 *              If the condition is false from the start, the code never runs.
 *
 *              Syntax:
 *              while (condition) {
 *                  // code to repeat
 *              }
 *
 *              Syntax is identical to C.
 *
 * ++      - increment operator. Adds 1 to a variable.
 *           eg. i++ is the same as i = i + 1
 *
 * break   - exits the loop immediately, even if the condition is still true.
 *
 * continue - skips the rest of the current iteration and re-checks the condition.
 *
 * true    - a boolean literal. while (true) creates an infinite loop that runs
 *           forever until a break statement exits it.
 *
 * Console.WriteLine() - prints text to the console with a newline at the end.
 * Console.ReadLine()  - reads a line of user input as a string.
 *
 * Note: Always make sure the condition will eventually become false,
 *       or use break — otherwise you get an infinite loop.
 *
 * */

using System;

class Program {
    static void Main() {

        // Basic while loop
        int i = 0;
        Console.WriteLine("Counting with while loop:");
        while (i < 5) {
            Console.WriteLine($"i = {i}");
            i++; // increment — without this the loop runs forever
        }

        // While loop with user input — keeps going until user types "quit"
        Console.WriteLine("\nType something (type 'quit' to stop):");
        string input = "";
        while (input != "quit") {
            input = Console.ReadLine();
            if (input != "quit") {
                Console.WriteLine($"You typed: {input}");
            }
        }
        Console.WriteLine("Loop ended.");

        // Infinite loop with break
        int count = 0;
        Console.WriteLine("\nInfinite loop broken at 3:");
        while (true) {
            Console.WriteLine($"count = {count}");
            count++;
            if (count == 3) break; // exit when count reaches 3
        }

    }
}
