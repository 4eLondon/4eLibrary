#include <raylib.h>

int main() {
  InitWindow(500, 500, "triangle");

  // ax x+ while bx x-
  // ay y+ while by y-

  float ax = 400, ay = 400;
  float bx = 100, by = 400;

  float cx = 250, cy = 100;
  float dx = 100, dy = 400;

  float ex = 250, ey = 100;
  float fx = 400, fy = 400;

  while (!WindowShouldClose()) {
    BeginDrawing();
    ClearBackground(BLACK);

    float tx = ax, ty = ay;
    float ttx = bx, tty = by;

    float lx = cx, ly = cy;
    float llx = dx, lly = dy;

    float ox = ex, oy = ey;
    float oox = fx, ooy = fy;

    for (float f = 0; f < 1; f += 0.001f) {
      DrawPixel(tx + (ttx - tx) * f, ty + (tty - ty) * f, RED);
      DrawPixel(lx + (llx - lx) * f, ly + (lly - ly) * f, BLUE);
      DrawPixel(ox + (oox - ox) * f, oy + (ooy - oy) * f, GREEN);
    }

    EndDrawing();
  };

  CloseWindow();
}
