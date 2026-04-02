#include <stdio.h>

int main() {
  char name[50];
  printf("What would you like to name your file: ");
  scanf("%49s", name);

  // write
  FILE *f = fopen(name, "w");
  if (f != NULL) {
    fprintf(f,
            "Here lies data from a file. Abandon hope all who reads this.\n");
    fclose(f);
  }

  // read
  FILE *g = fopen(name, "r");
  if (g != NULL) {
    char data[50];
    fgets(data, 50, g);
    printf("File reads: %s\n", data);
    fclose(g);
  }

  return 0;
}
