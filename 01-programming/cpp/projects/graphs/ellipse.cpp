#include "raylib.h"
#include <cmath>

int main() {
  InitWindow(500, 500, "ellipse");

  while (!WindowShouldClose()) {
    BeginDrawing();
    ClearBackground(BLACK);

    int r = 100;
    int sx = 300, sy = 300;

    for (float t = 0; t < 2 * PI; t += 0.001f) {
      float x = cos(t) * 2;
      float y = sin(t);
      DrawPixel(sx + x * r, sy + y * r, RED);
    }

    EndDrawing();
  }

  CloseWindow();
}
