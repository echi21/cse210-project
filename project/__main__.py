import arcade
from game import constants
from game.my_game_view import MyGame


def main():
    app_window = MyGame(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    app_window.center_window()
    arcade.run()


# Main code entry point
if __name__ == "__main__":
    main()
