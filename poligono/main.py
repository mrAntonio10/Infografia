import arcade
import numpy as np
from polygon import Polygon

# definicion de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "matrices de transformacion"


class TransformWindow(arcade.Window):
    def __init__(self, polygon: Polygon):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.polygon = polygon

    def on_draw(self):
        arcade.start_render()
        self.polygon.draw()
    
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP:
            self.polygon.translate(0, 5)
            # self.polygon.move(0, 5)
        elif symbol == arcade.key.DOWN:
            self.polygon.translate(0,-5)
        elif symbol == arcade.key.LEFT:
            self.polygon.translate(-5,0)
        elif symbol == arcade.key.RIGHT:
            self.polygon.translate(5,0)
            
def main():
    poly = Polygon([(40, 40), (200, 40), (120, 300)])
    app = TransformWindow(poly)
    arcade.run()


if __name__ == "__main__":
    main()
