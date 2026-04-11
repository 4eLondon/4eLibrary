#include "raylib.h"

void draw_grid() {
  InitWindow(500, 500, "grid");

  float ax = 20, ay = 0;
  float bx = 20, by = 500;

  float cx = 0, cy = 20;
  float dx = 500, dy = 20;

  // ay & cy = length +x
  // by & dy = length -y
  // bx & dx = width +x
  // ax & cx = width -x
  //
  while (!WindowShouldClose()) {
    BeginDrawing();
    ClearBackground(BLACK);

    float lx1 = ax, ly1 = ay, lx2 = bx, ly2 = by;
    float lx3 = cx, ly3 = cy, lx4 = dx, ly4 = dy;

    do {
      for (float f = 0; f <= 1; f += 0.001f) {
        DrawPixel(lx1 + (lx2 - lx1) * f, ly1 + (ly2 - ly1) * f, GRAY);
        DrawPixel(lx3 + (lx4 - lx3) * f, ly3 + (ly4 - ly3) * f, GRAY);
      }
      lx1 += 20;
      lx2 += 20;
      ly3 += 20;
      ly4 += 20;
    } while (lx1 < 500 && ly3 < 500);

    EndDrawing();
  }

  CloseWindow();
}
