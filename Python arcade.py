import arcade
import os
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "arcade alpha0.001"
MOVEMENT_SPEED = 5
BULLET_SPEED = 10
BULLET_DAMAGE = 20

class Game(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        """
        Initializer
        """

        # Call the parent class initializer
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        
        # Variables that will hold sprite lists
        self.player_list = None

        # Set up the player info
        self.player_sprite = None

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)
    
    game_start = False
    pos_x = 420
    pos_y = 100
    momentum_x = 0
    momentum_y = 0
    kogel_pos_x = 99
    kogel_pos_y = pos_y
    bool_kogel = False
    kogel_update_x = True
    enemy_x = 400
    enemy_y = 550
    enemy_hp = 100


    def setup(self):
        # Create your sprites and sprite lists here
        hero = None
        kogel1 = None
        Enemy = None

    def resetkogel(self):
        self.kogel_pos_y = self.pos_y
        self.bool_kogel = False
        self.kogel_update_x = True
    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()

        """  # Set up the player
        self.player_sprite = Player("images/Ships/spaceShips_007.png", SPRITE_SCALING)
        self.player_sprite.center_x = 40
        self.player_sprite.center_y = 40
        self.player_list.append(self.player_sprite)"""


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0
    
    def rondje(self, x,y,radius,color):
        arcade.draw_circle_filled(x,y,radius,color)

    def on_draw(self):
        """
        Rendering function
        """
        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()
        if self.game_start == False:
            arcade.draw_text("PRESS ENTER TO START", 300, 400, arcade.color.WHITE,20)
            arcade.draw_text("made by Robin goubitz and Tom Lengkeek",300,375,arcade.color.WHITE,10)
        else:
            rondje1 = self.rondje(self.pos_x,self.pos_y,30,arcade.color.WHITE)
            if self.bool_kogel == True:
              kogel1 = self.rondje(self.kogel_pos_x, self.kogel_pos_y, 10, arcade.color.BLUE)
            if self.enemy_hp > 0:
               Enemy = self.rondje(self.enemy_x,self.enemy_y,30,arcade.color.RED)
               arcade.draw_text(f"ENEMY HP: {self.enemy_hp}",600, 50,arcade.color.WHITE)
            if self.enemy_hp == 0:
              arcade.draw_text("YOU WON", 400 , 300, arcade.color.WHITE,20)
        # Call draw() on all your sprite lists below

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """

        if self.momentum_y == 1:
            self.pos_y += MOVEMENT_SPEED
        if self.momentum_y == -1:
            self.pos_y -= MOVEMENT_SPEED
        if self.momentum_x == 1:
            self.pos_x -= MOVEMENT_SPEED
        if self.momentum_x == -1:
            self.pos_x += MOVEMENT_SPEED
       
       
        if self.pos_x > SCREEN_WIDTH:
            self.pos_x = 0
        if self.pos_x < -10:
            self.pos_x = 799
        if self.pos_y > SCREEN_HEIGHT:
            self.pos_y = 0
        if self.pos_y < -10:
            self.pos_y = 0

        if self.bool_kogel == True:
          self.kogel_pos_y += BULLET_SPEED
        if self.kogel_pos_y > SCREEN_HEIGHT:
            self.resetkogel()
        if self.kogel_pos_x > SCREEN_WIDTH:
            self.resetkogel()
        
        if self.enemy_hp > 0:
           self.enemy_x += MOVEMENT_SPEED
        if self.enemy_x > SCREEN_WIDTH:
            self.enemy_x = -50
        if self.kogel_pos_x < self.enemy_x + 30 and self.kogel_pos_x > self.enemy_x - 30 and self.kogel_pos_y < self.enemy_y + 30 and self.kogel_pos_y > self.enemy_y - 30:
            self.enemy_hp -= BULLET_DAMAGE
            self.resetkogel()

    def on_key_press(self, key, key_modifiers):
        if self.game_start == False: 
            if key == 65293:
                self.game_start = True

        if key == 119:
            self.momentum_y = 1
        if key == 115:
            self.momentum_y = -1
        if key == 97:
            self.momentum_x = 1
        if key == 100:
            self.momentum_x = -1
        if key == 32:
            self.bool_kogel = True
            if self.kogel_update_x == True:
                self.kogel_pos_x = self.pos_x
                self.kogel_update_x = False

    def on_key_release(self, key, key_modifiers):
        if key == 119:
            self.momentum_y = 0
        if key == 115:
            self.momentum_y = 0
        if key == 97:
            self.momentum_x = 0
        if key == 100:
            self.momentum_x = 0
 
def main():
    """ Main method """
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()