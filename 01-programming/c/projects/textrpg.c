#include <stdio.h>
#include <stdlib.h>

// Function that calculates damage from attacks
int attack(int aggressor_atk, int victim_hp) {
  int new_victim_hp = victim_hp - aggressor_atk;
  printf("-- suffered %i points of damage. -- health is now %i\n",
         aggressor_atk, new_victim_hp);
  return new_victim_hp;
};

// function that displays stats
void overlay() {
  printf("\nHealth []\n");
  printf("\nAttack []\n");
};

// simple story function
void story(char speaker[], char said_text[]) {
  printf("\n%s :\n     %s", speaker, said_text);
};

// Struct oulining common variables across entities
struct entity {
  int hp, atk;
  char glyph;
};

int main() {

  // Entity definitions
  struct entity player;
  player.hp = 10;
  player.atk = 1;
  player.glyph = '@';

  struct entity woodsman;
  woodsman.hp = 30;
  woodsman.atk = 3;
  woodsman.glyph = '&';

  struct entity hound;
  hound.hp = 3;
  hound.atk = 2;
  hound.glyph = '%';

  // Start Menu
  int menu_choice;

  do {
    printf("\n= = = = = = = = = = = = = = = = = = = = =\n");
    printf("\n=              C  A  B  I  N            =\n");
    printf("\n= = = = = = = = = = = = = = = = = = = = =\n");
    printf("               New Game    [1]             \n");
    printf("               Load Game   [2]             \n");
    printf("               Exit        [3]             \n");

    scanf("%i", &menu_choice);

    switch (menu_choice) {
    case 1:
      system("clear");
      printf("Generating world . . .\n");
      printf("Placing items . . .\n");
      printf("Hiding secrets . . .\n");
      printf("Sprinkling snow . . .\n");
      break;

    case 2:
      system("clear");
      printf("\nx - x - x [ Select your save file] x - x - x\n");
      // load from file
      break;

    case 3:
      system("clear");
      return 0;

    default:
      system("clear");
      printf("! ! ! [ Invalid option choosen ] ! ! !");
      menu_choice = 0;
      break;
    };
  } while (menu_choice != 1 && menu_choice != 2 || menu_choice == 0);

  return 0;
}
