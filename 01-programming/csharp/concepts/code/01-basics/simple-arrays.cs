// -o-o-o-o- Simple Arrays -o-o-o-o-

/* This file goes over basic arrays in C# simply.
 *
 *  # # # # KEY # # # #
 *
 * array   - a fixed-size collection of elements of the same type.
 *           Declared differently from C:
 *           C:  int arr[5];
 *           C#: int[] arr = new int[5];
 *
 * new     - keyword used to allocate/create an array (or object) in memory.
 *           eg. int[] arr = new int[5]; creates an array of 5 integers.
 *
 * index   - arrays are zero-indexed, meaning the first element is at index 0.
 *           eg. arr[0] is the first element, arr[4] is the fifth.
 *
 * .Length - a built-in property that returns the number of elements in an array.
 *           eg. arr.Length
 *           Similar to manually tracking size in C.
 *
 * for     - a loop used to iterate over arrays. See simple-loops-for.cs.
 *
 * foreach - a simpler loop for reading every element in a collection.
 *           eg. foreach (int item in arr) { ... }
 *           No direct equivalent in C (C uses a standard for loop).
 *
 * Console.WriteLine() - prints text to the console with a newline at the end.
 *
 * */

using System;

class Program {
    static void Main() {

        // Declaring and initialising an array of 5 integers
        int[] numbers = new int[5];

        // Assigning values to each element by index
        numbers[0] = 10;
        numbers[1] = 20;
        numbers[2] = 30;
        numbers[3] = 40;
        numbers[4] = 50;

        // Printing each element using a for loop
        Console.WriteLine("Array elements (for loop):");
        for (int i = 0; i < numbers.Length; i++) {
            Console.WriteLine($"numbers[{i}] = {numbers[i]}");
        }

        // Declaring and initialising an array in one line (initialiser syntax)
        int[] primes = { 2, 3, 5, 7, 11 };

        // Printing using a foreach loop (simpler, read-only)
        Console.WriteLine("\nPrime numbers (foreach loop):");
        foreach (int prime in primes) {
            Console.WriteLine(prime);
        }

        // 2D array (like a grid/table)
        int[,] grid = {
            { 1, 2, 3 },
            { 4, 5, 6 }
        };

        Console.WriteLine("\n2D array (grid):");
        for (int row = 0; row < grid.GetLength(0); row++) {
            for (int col = 0; col < grid.GetLength(1); col++) {
                Console.Write($"{grid[row, col]} ");
            }
            Console.WriteLine();
        }

    }
}
