""" some comment """

import arcade
import random
import os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600



class Game(arcade.Window):
    def __init__(self):
        arcade.open_window(800, 600, "Space Ingayders")
        arcade.set_background_color(arcade.color.BLACK )
        
        
    def movement(momentum_X, momentum_Y):
        pass
    
    def momentum(Keypress):
        pass

    def player(player_x, player_y):
        pass

    def on_draw(self):
        arcade.start_render()

    def update(self, delta_time):
        pass
    
def main():
    arcade.start_render()    
    Game()
    arcade.finish_render()
    arcade.run()

if __name__ == "__main__":
    main()