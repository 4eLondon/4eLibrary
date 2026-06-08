// -o-o-o-o- Arrays -o-o-o-o-

/* This file goes over the basics of arrays in C simply.
 *
 * An array is a collection of values of the same data type stored
 * together under one name. Instead of making ten separate variables
 * you can store ten values in a single array and access each one
 * by its position.
 *
 *  # # # # KEY # # # #
 *
 * \n - creates a new line
 *
 * %i - represents an integer value that has to then be refered to
 * eg. printf("%i", varible_here)
 *
 * [] - square brackets are used to declare an array and to access
 * its elements by index.
 *
 * index - the position of an element inside an array. Indexes always
 * start at 0, not 1. So the first element is at index 0.
 *
 * Note: Arrays in C have a fixed size. Once declared the size cannot
 * be changed. Trying to access an index outside the array size will
 * cause undefined behaviour.
 * */

#include <stdio.h>

int main() {

  // declaring an array of 5 integers
  // the number in [] defines how many elements the array can hold
  int numbers[5] = {10, 20, 30, 40, 50};

  printf("Arrays store multiple values of the same type under one name.\n\n");

  // accessing individual elements by their index
  // remember: indexes start at 0 not 1
  printf("Element at index 0 is %i\n", numbers[0]); // first element
  printf("Element at index 1 is %i\n", numbers[1]);
  printf("Element at index 2 is %i\n", numbers[2]);
  printf("Element at index 3 is %i\n", numbers[3]);
  printf("Element at index 4 is %i\n", numbers[4]); // last element

  printf("\nArray elements can be updated by assigning to their index.\n");

  numbers[2] = 99; // updating the element at index 2
  printf("Element at index 2 is now %i\n", numbers[2]);

  printf("\nA for loop is the most common way to go through an array.\n\n");

  // using a for loop to print every element without writing each one manually
  for (int i = 0; i < 5; i++) {
    printf("numbers[%i] = %i\n", i, numbers[i]);
  }

  return 0;
}
