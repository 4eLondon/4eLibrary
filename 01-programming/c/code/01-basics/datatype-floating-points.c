// -o-o-o-o-o- Floating point numbers -o-o-o-o-o-

/* Floating point numbers are numbers that include a decimal point.
 * In C we have two data types that count as floating point, those being
 * floats and doubles respectively.
 *
 * Float = holds a size of 4 bytes with absolute precision for the first 7
 * decimal places.
 *
 * Double = holds a size of 8 bytes with absolute precision for up to 16 decimal
 * places.
 *
 * # # # # KEY # # # #
 *
 * %f - reperesents floating point numbers
 * %.*f - reperesents a floating point number to a * decimal places
 * \n - creates a new line
 * */

#include <stdio.h>

int main() {

  // the f at the end tells the compile the value is specifically a float
  // without this f the variable would start as a double then get converted to a
  // float
  float a = 1.123456789f;
  float b = 0.123456789f;
  float c = a + b;

  double x = 2.123456789;
  double y = 0.123456789;
  double z = x + y;

  // the .8 within the %f specifier reduces the float to 8 decimal places.
  // It automatically rounds.
  printf("\n-o- Floats -o-\n");
  printf("A float called A is equal to %.9f\n", a);
  printf("A float called B is equal to %.9f\n", b);
  printf("C reperesents A + B. C is equal to %.9f\n", c);

  printf("\n -o-o-o- Orignal values are as follows: -o-o-o-\n");
  printf("A was set as %.9f but was changed to '%.9f' at runtime\n",
         1.123456789, a);
  printf("B was set as %.9f but was changed to '%.9f' at runtime\n",
         0.123456789, b);

  printf("\n-x- Doubles -x-\n");
  printf("A double called X is equal to %.9f\n", x);
  printf("A double called Y is equal to %.9f\n", y);
  printf("Z reperesents X + Y. Z is equal to %.9f\n", z);

  printf("\n -x-x-x- Orignal values are as follows: -x-x-x-\n");
  printf("X was set as %.9f and remained as '%.9f' at runtime\n", 2.123456789,
         x);
  printf("Y was set as %.9f and remained as '%.9f' at runtime\n", 0.123456789,
         y);

  return 0;
}
