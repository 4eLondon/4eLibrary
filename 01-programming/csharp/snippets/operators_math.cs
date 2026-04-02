using System;
class operators_math{
  static void Main(){
    Console.WriteLine("Please enter a number");
    string input = Console.ReadLine();
    Console.WriteLine("Please enter another number");
    string input2 = Console.ReadLine();
   
    int num = Convert.ToInt32(input);
    int num2 = Convert.ToInt32(input2);

    Console.WriteLine(num+ " + "+num2+" = "+(num+num2));
    Console.WriteLine(num+ " - "+num2+" = "+(num-num2));
    Console.WriteLine(num+ " * "+num2+" = "+(num*num2));
    Console.WriteLine(num+ " / "+num2+" = "+(num/num2));
  }
}
