# import random

import pyinputplus as pyip

from art import logo

gameboard = {
    "top-L": " ", "top-C": " ", "top-R": " ",
    "mid-L": " ", "mid-C": " ", "mid-R": " ",
    "low-L": " ", "low-C": " ", "low-R": " "
}

def printBoard(board):
    print(gameboard["top-L"] + "|" + gameboard["top-C"] + "|" + gameboard["top-R"])
    print("-+-+-")
    print(gameboard["mid-L"] + "|" + gameboard["mid-C"] + "|" + gameboard["mid-R"])
    print("-+-+-")
    print(gameboard["low-L"] + "|" + gameboard["low-C"] + "|" + gameboard["low-R"])

print(logo)
print()
player = "X"
spaces = list(gameboard.keys())

while len(spaces) > 0:
    printBoard(gameboard)
    print()

    if len(spaces) > 1:
        move = pyip.inputMenu(spaces, prompt=f"Turn for {player}. Which space would you like?\n")
        gameboard[move] = player
        spaces.remove(move)

        if player == "X":
            player = "O"
        else:
            player = "X"

    else:
        move = spaces[0]
        gameboard[move] = player
        spaces.remove(move)

print("Game Over")
print("Final Result:\n")
printBoard(gameboard)
