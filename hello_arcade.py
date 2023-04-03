#importamos el paquete
import arcade

#definir constantes EN MAYUSCULAS
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Hola arcade"

#crear nueva ventana
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

arcade.set_background_color(arcade.color.BLUE)
#renderizamos la pantalla
arcade.start_render()
#dibujamos un circulo
arcade.draw_circle_filled(
    SCREEN_WIDTH / 2, #POSICION EN X
    SCREEN_HEIGHT / 2, #POSICION EN Y
    180,
    [192,173,140]
)
arcade.draw_circle_filled(
    SCREEN_WIDTH / 2, #POSICION EN X
    SCREEN_HEIGHT / 2, #POSICION EN Y
    130,
    [239, 221, 111]
)

arcade.draw_triangle_filled(
        100, 100,
        400, 100,
        300, 300,
        arcade.color.BLUE
    )
arcade.finish_render()

arcade.run()
 