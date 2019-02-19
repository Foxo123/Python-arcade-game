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
        pass


    def rondje(self, x,y,radius,color):
        arcade.draw_circle_filled(x,y,radius,color)

    rondje1 = None
    def on_draw(self):
        """
        Rendering function
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()
        rondje1 = self.rondje(300,300,200,arcade.color.WHITE)
        # Call draw() on all your sprite lists below

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        pass

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

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