/*                          - + -   Booleans in C   - + -
 
    Naturally in C booleans are not naturally occuring in their usual true or false fashion.
    In order to create a bool we can either:
        1). Include the library stdbool.h in order to access the usual true and false.
        2). Use ints as they pretty much also act as bools under the right set up.

    When using the int method think of how normal bools work. True means on which we could just have as an int set to 1 and for false/off we can just set that to 0. At the end of the day bools are just 0s and 1s hence why we only need ints to recreate their base functionality.
*/

#include<stdio.h>
#include<stdbool.h> //This is needed to access the bool datatype
 
int main(){
    const char* status= "null"; // Used to assign string true or false to int based boolean

    printf("\n---------------------------------------------\n");
    printf("\n             Int based Booleans              \n");
    printf("\n---------------------------------------------\n");

    // Using integer method
    int pseudo_bool = 0;

    if(pseudo_bool == 0){ status = "False";}
    else{status = "True";}

    printf("Your int based boolean is currently set to %d which is equal to %s",pseudo_bool, status);

    printf("\n\nUpdating varible\n\n");

    pseudo_bool = 1;

    if(pseudo_bool == 0){ status = "False";}
    else{status = "True";}

    printf("Your int based boolean is currently set to %d which is equal to %s",pseudo_bool, status);


    printf("\n\n---------------------------------------------\n");
    printf("\n             Normal Booleans                 \n");
    printf("\n---------------------------------------------\n");

    // Using normal booleans
    bool isActive = false;

    printf("\nYour true boolean is set to %d which is equal to %s", isActive, isActive ? "true" : "false"); //string is printed with ternary operator.
                                                                                                            
    printf("\n\nUpdating varible\n\n");
    isActive = true;
                                                                                                            
    printf("Your true boolean is set to %d which is equal to %s\n", isActive, isActive ? "true" : "false"); //string is printed with ternary operator.
  
    return 0;
}
