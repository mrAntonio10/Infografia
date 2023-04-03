import arcade

#variables de ventana
SCREEN_WIDTH=1000
SCREEN_HEIGHT=650
SCREEN_TITLE='Mi Grafico'


#Mi dibujo
CHARACTER_SCALING = 1
TITLE_SCALING = 0.5
COIN_SCALING = 0.5


#Creamos una clase para manejar las dimensiones de ventana
class window(arcade.Window):

    #Constructor
    def __init__(self):
        #Hacemos uso de los metodos de la clase padre "arcade"
            #maneja las variables de ventana
        super().__init__(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
        #hacemos set del bg
        arcade.set_background_color(arcade.csscolor.AQUA)

        self.coin_list = None
        self.wall_list = None
        self.player_list = None

        self.player_sprite = None


    #la clase window tambien maneja una funcion de montaje
    def setup(self):
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash = True)
        self.coin_list = arcade.SpriteList(use_spatial_hash = True)

        image_source = ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png"
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        
        self.player_list.append(self.player_sprite)

        for x in range(0,1250,64):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", TITLE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)

        coordinate_list = [[512,96],
                           [256,96],
                           [768,96]

                        ]
        
        for coordinate in coordinate_list:
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", TITLE_SCALING)
            wall.position = coordinate
            self.wall_list.append(wall)

    #la clase window tiene una funcion dibujo
    def on_draw(self):
        #renderizamos
        arcade.start_render()
        #nuestro dibujo
        self.wall_list.draw()
        self.player_list.draw()


def main():
    pantalla = window()
    pantalla.setup()
    arcade.run()


#Con esto nos aseguramos que manejemos desde main
if __name__ == '__main__':
    main()