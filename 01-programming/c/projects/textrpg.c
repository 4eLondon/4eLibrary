#include <stdio.h>

// Function that calculates damage form attacks
int attack(int aggressor_atk, int victim_hp) {
  int new_victim_hp = victim_hp - aggressor_atk;
  printf("-- suffered %i points of damage. -- health is now %i\n",
         aggressor_atk, new_victim_hp);
  return new_victim_hp;
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

  // -o-o-o-o-o- TESTING -o-o-o-o-o-
  printf("Player hp is %i, attack is %i and glyph is %c\n", player.hp,
         player.atk, player.glyph);
  printf("Woodsman hp is %i, attack is % i and glyph is %c\n", woodsman.hp,
         woodsman.atk, woodsman.glyph);
  printf("Hound hp is %i, attack is %i and glyph is %c\n", hound.hp, hound.atk,
         hound.glyph);

  player.hp = attack(hound.atk, player.hp);
  player.hp = attack(hound.atk, player.hp);

  return 0;
}
