import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

def draw_tree():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Dibujando un Árbol")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.start_render()
    # Dibuja el tronco
    arcade.draw_rectangle_filled(
        SCREEN_WIDTH/2, SCREEN_HEIGHT/4,
        SCREEN_WIDTH/10, SCREEN_HEIGHT/2,
        arcade.color.BROWN
    )
    # Dibuja las hojas
    arcade.draw_circle_filled(
        SCREEN_WIDTH/2, SCREEN_HEIGHT/2,
        SCREEN_WIDTH/5, arcade.color.GREEN
    )
    arcade.draw_circle_filled(
        SCREEN_WIDTH/2 + SCREEN_WIDTH/6, SCREEN_HEIGHT/2 + SCREEN_HEIGHT/6,
        SCREEN_WIDTH/6, arcade.color.GREEN
    )
    arcade.draw_circle_filled(
        SCREEN_WIDTH/2 - SCREEN_WIDTH/6, SCREEN_HEIGHT/2 + SCREEN_HEIGHT/6,
        SCREEN_WIDTH/6, arcade.color.GREEN
    )
    arcade.finish_render()
    arcade.run()

draw_tree()
