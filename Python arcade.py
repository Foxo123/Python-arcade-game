import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "NEGERS ETEN POEP OMDAT ZE DAT LEKKER VINDEN alpha0.001"


class Game(arcade.Window):
    """
   The game class
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLACK)

        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        # Create your sprites and sprite lists here
        rondje1 = None


    def rondje(self, x,y,radius,color):
        arcade.draw_circle_filled(x,y,radius,color)

    pos_x = 420
    pos_y = 100

    momentum_x = 0
    momentum_y = 0

    def on_draw(self):
        """
        Rendering function
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()
        self.rondje1 = self.rondje(self.pos_x,self.pos_y,30,arcade.color.WHITE)
        #self.niggatoilet = arcade.

        # Call draw() on all your sprite lists below

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        if self.momentum_y == 1:
            self.pos_y += 5
        if self.momentum_y == -1:
            self.pos_y += -5
        ##self.pos_x += 5
        if self.pos_x > SCREEN_WIDTH:
            self.pos_x = 0
        if self.pos_x < -10:
            self.pos_x = 799
        
        

    def on_key_press(self, key, key_modifiers):
        if key == 119:
            self.momentum_y = 1
        if key == 115:
            self.momentum_y = -1
        if key == 97:
            self.momentum_x = 1
        if key == 100:
            self.momentum_x = -1

            

    def on_key_release(self, key, key_modifiers):
        if key == 119:
            self.momentum_y = 0
        if key == 115:
            self.momentum_y = 0
        if key == 97:
            self.momentum_x = 0
        if key == 100:
            self.momentum_x = 0

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    """ Main method """
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()