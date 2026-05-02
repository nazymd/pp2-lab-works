from TSIS3.ui import main_menu, username_screen
from TSIS3.racer import play_game

while True:
    action = main_menu()

    if action == "play":
        username = username_screen()

        result = "retry"
        while result == "retry":
            result = play_game(username)