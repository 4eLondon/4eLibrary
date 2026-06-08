// -o-o-o-o- Structs -o-o-o-o-

/* This file goes over the basics of structs in C simply.
 *
 * Structs (structures) allow you to group multiple variables of different
 * types together under a single name. Think of them as a custom data type
 * you design yourself. For example a 'Person' could have a name, an age
 * and a height all bundled into one struct.
 *
 *  # # # # KEY # # # #
 *
 * \n - creates a new line
 *
 * %i - represents an integer value that has to then be refered to
 * eg. printf("%i", varible_here)
 *
 * %s - represents a string value
 * %f - represents a floating point value
 *
 * struct - a user defined type that groups variables (called members) together.
 *
 * typedef - allows us to give a type a new name so we dont have to write
 * the word 'struct' every time we declare one.
 *
 * . (dot operator) - used to access a member of a struct.
 * eg. person.age accesses the age member of a struct called person.
 *
 * Note: Structs on their own are just a blueprint. No memory is used until
 * you actually create a variable of that struct type.
 * */

#include <stdio.h>

// defining a struct called Person using typedef so we can use 'Person'
// instead of having to write 'struct Person' every time
typedef struct {
  char name[50]; // char array used as a string to store the persons name
  int age;       // integer to store the persons age
  float height;  // float to store the persons height in meters
} Person;

// a second struct to show that structs can contain other structs
typedef struct {
  char subject[50]; // the subject the grade belongs to
  int score;        // the score out of 100
} Grade;

int main() {

  // creating a Person variable and assigning values to its members
  Person personOne;
  personOne.age = 21;       // accessing and setting the age member
  personOne.height = 1.82f; // accessing and setting the height member

  // strings cannot be assigned with = so we use a char array directly
  char nameOne[50] = "Alice";
  Person personTwo = {"Bob", 34,
                      1.75f}; // shorthand way to set all members at once

  printf("Structs group different data types under one name.\n\n");

  // printing the members of personTwo using the dot operator
  printf("Person Two's name is %s\n", personTwo.name);
  printf("Person Two's age is %i\n", personTwo.age);
  printf("Person Two's height is %gm\n\n", personTwo.height);

  // creating a Grade variable
  Grade mathGrade = {"Mathematics", 87};
  Grade englishGrade = {"English", 92};

  printf("Structs can represent any grouped data. Here are some grades:\n\n");

  printf("Subject: %s | Score: %i/100\n", mathGrade.subject, mathGrade.score);
  printf("Subject: %s | Score: %i/100\n", englishGrade.subject,
         englishGrade.score);

  printf(
      "\nStruct members can be updated at any time using the dot operator.\n");

  mathGrade.score = 95; // updating a member after the struct was created
  printf("Maths score updated. New score: %i/100\n", mathGrade.score);

  return 0;
}
