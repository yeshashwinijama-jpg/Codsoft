import random

board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]


def show():

    print()

    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")

    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")

    print(board[6] + " | " + board[7] + " | " + board[8])

    print()


show()

for i in range(5):

    user = int(input("Enter position: "))

    if board[user - 1] != "X" and board[user - 1] != "O":

        board[user - 1] = "X"

    else:

        print("Already Filled")

    computer = random.randint(1, 9)

    while board[computer - 1] == "X" or board[computer - 1] == "O":

        computer = random.randint(1, 9)

    board[computer - 1] = "O"

    show()