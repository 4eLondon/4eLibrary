// -o-o-o-o- Enums -o-o-o-o-

/* This file goes over the basics of enums in C simply.
 *
 * Enums (enumerations) are a way to assign names to integer values.
 * Instead of remembering that 0 means Monday or 1 means Tuesday,
 * enums let you use readable names in your code. Under the hood they
 * are still integers, starting at 0 unless told otherwise.
 *
 *  # # # # KEY # # # #
 *
 * \n - creates a new line
 *
 * %i - represents an integer value that has to then be refered to
 * eg. printf("%i", varible_here)
 *
 * enum - a user defined type that holds a set of named integer constants.
 *
 * typedef - allows us to give a type a new name so we dont have to write
 * the word 'enum' every time we use it.
 *
 * Note: By default the first item in an enum is equal to 0, the next is 1
 * and so on. You can manually set values by using the = operator inside
 * the enum definition. Any item after a manually set value will continue
 * counting up from that value.
 * */

#include <stdio.h>

// A basic enum. Each name is automatically assigned an integer value.
// MONDAY = 0, TUESDAY = 1, WEDNESDAY = 2 and so on.
typedef enum {
  MONDAY,
  TUESDAY,
  WEDNESDAY,
  THURSDAY,
  FRIDAY,
  SATURDAY,
  SUNDAY
} Day;

// An enum with manually assigned values.
// Values do not have to start at 0 or be sequential.
typedef enum {
  COLD = 1, // manually set to 1
  WARM = 2, // manually set to 2
  HOT = 3   // manually set to 3
} Temperature;

int main() {

  Day today = WEDNESDAY;     // assigns the enum value WEDNESDAY to 'today'
  Temperature weather = HOT; // assigns the enum value HOT to 'weather'

  printf("Enums store named integer values.\n\n");

  // printing the underlying integer values of our enums
  printf("MONDAY is equal to %i\n", MONDAY);
  printf("TUESDAY is equal to %i\n", TUESDAY);
  printf("WEDNESDAY is equal to %i\n", WEDNESDAY);
  printf("THURSDAY is equal to %i\n", THURSDAY);
  printf("FRIDAY is equal to %i\n", FRIDAY);
  printf("SATURDAY is equal to %i\n", SATURDAY);
  printf("SUNDAY is equal to %i\n\n", SUNDAY);

  printf("Today is set to WEDNESDAY. Its underlying value is %i\n\n", today);

  // enums work well with switch statements since they are just integers
  switch (today) {

  case MONDAY:
    printf("Today is Monday\n");
    break;

  case TUESDAY:
    printf("Today is Tuesday\n");
    break;

  case WEDNESDAY: // this case will be true since today = WEDNESDAY
    printf("Today is Wednesday\n");
    break;

  case THURSDAY:
    printf("Today is Thursday\n");
    break;

  case FRIDAY:
    printf("Today is Friday\n");
    break;

  case SATURDAY:
    printf("Today is Saturday\n");
    break;

  case SUNDAY:
    printf("Today is Sunday\n");
    break;

  default: // runs if no other case is true
    printf("\nERROR - Day not recognised.\n");
    break;
  }

  printf("\nThe weather enum uses manual values.\n");
  printf("COLD = %i, WARM = %i, HOT = %i\n", COLD, WARM, HOT);
  printf("Current weather is set to HOT. Its underlying value is %i\n",
         weather);

  return 0;
}
