from db import create_tables
from game import run_game

create_tables()

username = input("Enter username: ")

while True:
    run_game(username)