#include<raylib.h>

void render_text(){
    int x_axis =0;
    int y_axis =0;

    for(float ya=60; ya<=1000; ya+=20){
        DrawText(TextFormat("%i",y_axis), ya, 730, 12, WHITE);
        y_axis ++;
    }
    for(float xa=60; xa<=700; xa+=20){
        DrawText(TextFormat("%i",x_axis), 30, xa, 12, WHITE);
        x_axis ++;
    }
}

int main(){
    InitWindow(1200,800,"grid");
    while(!WindowShouldClose()){
        BeginDrawing();
        ClearBackground(BLACK);

        // Draw Vertical lines
        for(float x = 60; x<= 1000; x+=20 ){
            DrawLine(x, 60, x, 700, BLUE);
        }
        
        // Draw Horizontal lines
        for(float y = 60; y<= 700; y+=20 ){
            DrawLine(60, y, 1000, y, GRAY);
        }

        render_text();


        EndDrawing();
    }
    CloseWindow();
    return 0;
}
