import arcade
'''
Marco Antonio Roca Montenegro
Docente: Eduardo Laruta Espejo
Materia: Infografia 2023
'''
def draw_triangle(x, y, width, height, color):
    points = [(x, y), (x + width / 2, y + height), (x - width / 2, y + height)]
    arcade.draw_polygon_filled(points, color)

def draw_nested_triangles(x, y, width, height, depth):
    if depth == 0:
        return
    draw_triangle(x, y, width, height, arcade.color.WHITE)
    draw_nested_triangles(x, y + height / 2, width / 2, height / 2, depth - 1)
    draw_nested_triangles(x + width / 4, y, width / 2, height / 2, depth - 1)
    draw_nested_triangles(x - width / 4, y, width / 2, height / 2, depth - 1)

# Configuración de ventana
SCREEN_WIDTH = 640  # ancho
SCREEN_HEIGHT = 480 # alto
SCREEN_TITLE = "Triángulos anidados"
if __name__ == "__main__":
    # Inicializar ventana y establecer el fondo
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_background_color(arcade.color.BLACK)

    # Dibujar triángulos anidados
    draw_nested_triangles(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3, SCREEN_HEIGHT / 2, SCREEN_HEIGHT / 2, 5)

    # Actualizar ventana
    arcade.finish_render()

# Mantener ventana abierta hasta que se cierre manualmente
arcade.run()