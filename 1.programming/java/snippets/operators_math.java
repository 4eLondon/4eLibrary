import java.util.Scanner;

public class operators_math {
  public static void main(String[] agrs) {

    Scanner input = new Scanner(System.in);

    System.out.println("Please enter a number: ");
    String a = input.nextLine();

    System.out.println("Please enter another number: ");
    String b = input.nextLine();

    int num = Integer.parseInt(a);
    int num2 = Integer.parseInt(b);

    System.out.println(num + " + " + num2 + " = " + (num + num2));
    System.out.println(num + " - " + num2 + " = " + (num - num2));
    System.out.println(num + " * " + num2 + " = " + (num * num2));
    System.out.println(num + " / " + num2 + " = " + (num / num2));

    input.close();
  }
}
