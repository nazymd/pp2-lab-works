from ui import main_menu, username_screen
from racer import play_game

while True:
    action = main_menu()

    if action == "play":
        username = username_screen()

        result = "retry"
        while result == "retry":
            result = play_game(username)