# Variables in C

As with all programming languages variables serve as a means for us to store data in memory for easy usage and modification later. In C the idea is mostly the same but a few differences are to be noted when it comes to making variables and assigning data types to them.

The list of data types that exist naturally in C are as follows:

| Name | Use |

| --- | --- |

| char | Short for character. It stores as single letter or digit |

| int | Whole numbers. May be negative or positive |

| float | Number with a floating point/decimals. |

| double | A much more precise version of floats |

## Boolean

You may have noticed that there was no mention of ```strings``` or ```boolean``` and that for good reason. If you think about it booleans are really just representations of **1s** and **0s**. On and off, true or false. Boolean for this reason can just be created as an ```int``` where a if-else statement later goes to check the state of things whether true or false. Should we wish to have the ```bool``` data type we can enable it by including the ```stdbool.h``` header to use true or false more directly rather than ints.

## Strings

```Strings``` on the other hand do not exist as natively as ```boolean```. C has no concepts of *"words"* being a thing outright as common in languages like python. In order to make a string we would first have to create a variable with the ```char``` data type and then set that variable to be an array. Strings are just chars placed in order next to each other so you can see how this logic works. 

All stings in C end with ```\0``` which is called the null terminator it is what marks the end of a string and is itself treated as a character. For any string you make simply add 1 to the character count to account for \0.This is key in making an array where the size is fixed. One could bypass this rule as modern C does place more focus on the actual characters before \0.

ie. The snippet```char pet[3]="cat"``` will run as valid code without any direct errors from C despite the rule stating the array should actually be ```[4]``` to account for \0. For this its important to keep the null terminator in mind.

Below are all the possible ways to make a string.

#### Fixed arrays

As stated earlier strings are simply an array of chars. Given we know how ```arrays``` work we can then make a string.

eg. ```char name[4] = "Tom";``` 

This works well when we know the amount of character before hand where we can then hardcoded the array size granted it wont change. Granted our string length doesn't surpass our array size we will not encounter and errors. Setting the array size to ```[5]``` but only using ```[0],[1],[2],[3]``` for tom will see the space left behind unoccupied.

#### Uninitialized strings

Our first attempt to create a more traditional string as seen in languages such as python begins here. Uninitialized strings as the name suggest are strings that were not given an initial size in the form of an array and as such are far more flexible without having to be defined outright. We create uninitialized strings by making our char variable a pointer with ```*```. It is important to note Uninitialized veriables are dangerously random. In this case we do in fact mean **Random**, and uninitialized variable as no predictable behavior and could interfere with other aspects of the program and its host system.

eg. ```char *city;```

One in theory could use this for things such as user input. Rather than spend time confining the string it will simply take up as much space as it needs. Though useful uninitialized strings aren't exactly a great way to go about creating strings as they may cause crashes and data corruption but technically they are a legal method to make flexible dynamic stings simply over more complex methods yet to be stated below.


