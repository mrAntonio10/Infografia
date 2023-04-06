import arcade
#definimos constantes
SCREEN_WIDTH=800
SCREEN_HEIGHT=800
SCREEN_TITLE='Marco - Bresenham'


class App(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
        #bg color
        arcade.set_background_color(arcade.color.BLACK)

        self.px = (SCREEN_WIDTH/2) #
        self.py = SCREEN_HEIGHT/2  # 
        self.movement = 5
        self.points = [] #array posicion comidas


    #teclas presionadas   
    def on_key_press(self, symbol: int, modifiers: int):
        '''METODO PARA DETECTAR TECLAS PRESIONADAS
        Argumentos: 
            symbol: que tecla fue presionada
            modifiers: modificadores presionados (CTRL, ALT, SHIFT)
        '''
        if (symbol == arcade.key.UP):
            print('ARRIBA :D')
            self.py += self.movement

        if (symbol == arcade.key.DOWN):
            print('ABAJO :D')
            self.py -= self.movement

        if (symbol == arcade.key.LEFT):
            print('IZQUIERDA :D')
            self.px -= self.movement

        if (symbol == arcade.key.RIGHT):
            print('DERECHA :D')
            self.px += self.movement
        
    #detectar mouse
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        '''
        Metodo para detectar click del mouse
        Argumentos:
            X: coordenada x del click
            Y: coordenada y del click
            Button: boton del mouse presionado
            Modifiers: Shift, CTRL, etc
        '''
        if button == arcade.MOUSE_BUTTON_LEFT:
            print(f"Agregando punto ({x}, {y}) array {len(self.points)}")
            self.points.append((x,y))
        print(x, y, button)

    def player_is_on_food(self):
        '''
        Metodo para detectar si colisiona con la comida
        Retorna un indice, este es el detector
            Indice del punto en la lista self.point si existe colision

            else
                Devuelve el valor de -1
        '''
        for i, p in enumerate(self.points):
            if abs(self.px - p[0]):    
                print('Hay colision')
                return self.points.index
            else:
                return -1


    def on_update(self, delta_time: float):
        'metodo para actualizar objetos del juego'
        #print(f'{1/delta_time}') #Son los fps del juego
        colision = self.player_is_on_food()
        if colision != -1:
            print(f"Colision en el punto {colision}: {self.points[colision]}")

    #dibujos en pantalla
    def on_draw(self):
        'METODOS DE DIBUJO'
        arcade.start_render() #tenemos que renderizar
                            # punto en x - punto en y - color - SIZE
        arcade.draw_point(self.px, self.py, arcade.color.RED, 10)
        if self.points:
            arcade.draw_points(self.points, arcade.color.GREEN, 5)


#MAIN
if __name__ == "__main__":
    App = App()
    #TIENE QUE CORRER ARCADE
    arcade.run()
