// -o-o-o-o- Syntax (Comments) -o-o-o-o-

/* This file goes over the different types of comments in C# simply.
 *
 *  # # # # KEY # # # #
 *
 * Comments are lines of text ignored by the compiler. They are used to explain
 * code, leave notes, or temporarily disable code. C# supports the same comment
 * styles as C, plus one extra type for documentation.
 *
 * // - single-line comment. Everything after // on that line is ignored.
 *      Same as in C.
 *
 * /* ... * / - multi-line comment. Everything between the opening and closing
 *      markers is ignored, across as many lines as needed.
 *      Same as in C.
 *
 * /// - XML documentation comment. Unique to C#. Used to describe classes,
 *       methods, and parameters. Tools like Visual Studio and IDEs read these
 *       to generate tooltips and documentation automatically.
 *       No equivalent in standard C.
 *
 * Note: Comments do not affect how the program runs.
 *       Good comments explain WHY, not just WHAT.
 *
 * */

using System;

class Program {

    /// <summary>
    /// This is an XML documentation comment.
    /// It describes what the method does for IDEs and documentation tools.
    /// </summary>
    /// <param name="name">The name to greet.</param>
    /// <returns>A greeting string.</returns>
    static string Greet(string name) {
        return $"Hello, {name}!"; // inline comment: returns a greeting
    }

    static void Main() {

        // This is a single-line comment
        Console.WriteLine("Comments do not affect output.");

        /*
         * This is a multi-line comment.
         * It can span as many lines as needed.
         * Useful for longer explanations or temporarily disabling code.
         */
        Console.WriteLine("Multi-line comments work the same as in C.");

        // Calling the documented method
        string message = Greet("World");
        Console.WriteLine(message);

        // Console.WriteLine("This line is commented out and will not run.");

    }
}
