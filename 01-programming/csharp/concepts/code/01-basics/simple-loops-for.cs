// -o-o-o-o- Simple Loops (For) -o-o-o-o-

/* This file goes over the basic for loop in C# simply.
 *
 *  # # # # KEY # # # #
 *
 * for loop - a loop that repeats a block of code a set number of times.
 *            It has three parts inside the parentheses, separated by semicolons:
 *
 *            for (initialiser; condition; increment) { }
 *
 *            initialiser - runs once before the loop starts. Sets up a counter.
 *                          eg. int i = 0
 *            condition   - checked before every iteration. Loop runs while true.
 *                          eg. i < 5
 *            increment   - runs after every iteration. Usually updates the counter.
 *                          eg. i++
 *
 *            Syntax is identical to C.
 *
 * ++      - increment operator. Adds 1 to a variable.
 *           eg. i++ is the same as i = i + 1
 *
 * --      - decrement operator. Subtracts 1 from a variable.
 *           eg. i-- is the same as i = i - 1
 *
 * break   - exits the loop immediately.
 * continue - skips the rest of the current iteration and moves to the next.
 *
 * Console.WriteLine() - prints text to the console with a newline at the end.
 *
 * */

using System;

class Program {
    static void Main() {

        // Basic for loop counting up
        Console.WriteLine("Counting up (0 to 4):");
        for (int i = 0; i < 5; i++) {
            Console.WriteLine($"i = {i}");
        }

        // For loop counting down
        Console.WriteLine("\nCounting down (5 to 1):");
        for (int i = 5; i > 0; i--) {
            Console.WriteLine($"i = {i}");
        }

        // For loop with a step of 2 (counting by twos)
        Console.WriteLine("\nCounting by twos (0 to 10):");
        for (int i = 0; i <= 10; i += 2) {
            Console.WriteLine($"i = {i}");
        }

        // Using break to exit a loop early
        Console.WriteLine("\nBreaking at 3:");
        for (int i = 0; i < 10; i++) {
            if (i == 3) break;
            Console.WriteLine($"i = {i}");
        }

        // Using continue to skip an iteration
        Console.WriteLine("\nSkipping 3 (continue):");
        for (int i = 0; i < 6; i++) {
            if (i == 3) continue;
            Console.WriteLine($"i = {i}");
        }

    }
}
