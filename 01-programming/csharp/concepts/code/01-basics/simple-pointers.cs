// -o-o-o-o- Simple Pointers (References) -o-o-o-o-

/* This file goes over the C# equivalent of pointers simply.
 *
 *  # # # # KEY # # # #
 *
 * IMPORTANT: C# does not use pointers in everyday code.
 *            C pointers are replaced by REFERENCES and the REF keyword in C#.
 *            True C-style pointers exist in C# but require an 'unsafe' block
 *            and are rarely needed. This file covers the C# way.
 *
 * reference type - in C#, objects (classes, arrays, strings) are automatically
 *                  reference types. Assigning them copies the reference (address),
 *                  not the data. This is similar to a pointer in C.
 *
 * value type     - in C#, primitives (int, double, bool, etc.) are value types.
 *                  Assigning them copies the actual value, not a reference.
 *                  To pass them by reference, use the 'ref' keyword.
 *
 * ref     - keyword that passes a variable BY REFERENCE to a method.
 *           Changes made inside the method affect the original variable.
 *           eg. static void Double(ref int x) { x *= 2; }
 *           Called as: Double(ref myVar);
 *           Closest C# equivalent to passing a pointer: func(&myVar) in C.
 *
 * out     - similar to ref, but the method is expected to ASSIGN a value.
 *           The variable does not need to be initialised before being passed.
 *           eg. static void GetValue(out int x) { x = 42; }
 *
 * Console.WriteLine() - prints text to the console with a newline at the end.
 *
 * */

using System;

class Program {

    // Using 'ref' to modify a variable passed in (like passing a pointer in C)
    static void DoubleValue(ref int x) {
        x *= 2; // modifies the original variable, not a copy
    }

    // Using 'out' to return a value through a parameter
    static void GetMinMax(int[] arr, out int min, out int max) {
        min = arr[0];
        max = arr[0];
        foreach (int val in arr) {
            if (val < min) min = val;
            if (val > max) max = val;
        }
    }

    static void Main() {

        // Value type behaviour (copy)
        int a = 10;
        int b = a;   // b gets a COPY of a's value
        b = 99;      // changing b does NOT affect a
        Console.WriteLine($"a = {a}, b = {b}"); // a is still 10

        // Passing by reference with 'ref' (like &variable in C)
        int myNumber = 5;
        Console.WriteLine($"\nBefore DoubleValue: {myNumber}");
        DoubleValue(ref myNumber); // passes the reference, not a copy
        Console.WriteLine($"After DoubleValue:  {myNumber}"); // now 10

        // Reference type behaviour (arrays are reference types)
        int[] arr1 = { 1, 2, 3 };
        int[] arr2 = arr1;  // arr2 points to the SAME array in memory
        arr2[0] = 99;       // changing arr2 ALSO changes arr1
        Console.WriteLine($"\narr1[0] after changing arr2[0]: {arr1[0]}"); // 99

        // Using 'out' parameters
        int[] numbers = { 4, 1, 8, 2, 7 };
        GetMinMax(numbers, out int min, out int max);
        Console.WriteLine($"\nMin: {min}, Max: {max}");

    }
}
