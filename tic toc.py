from tkinter import *
import random


# Function to handle each player's turn
def next_turn(row, column):
    global player
    if buttons[row][column]['text'] == "" and check_winner() is False:
        buttons[row][column]['text'] = player

        # Check if there is a winner after each turn
        if check_winner() is False:
            player = players[1] if player == players[0] else players[0]
            label.config(text=(player + " turn"))
        elif check_winner() is True:
            label.config(text=(player + " wins"))
        elif check_winner() == "Tie":
            label.config(text="Tie")



def check_winner():

    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")




            return True
    for col in range(3):
        if buttons[0][col]['text'] == buttons[1][col]['text'] == buttons[2][col]['text'] != "":
            buttons[0][col].config(bg="green")
            buttons[1][col].config(bg="green")
            buttons[2][col].config(bg="green")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return  True


    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True
    if empty_spaces() is False:
        for row in range(3):
            for col in range(3):
                buttons[row][col].config(bg="yellow")
        return "Tie"
    return False


# Function to check if there are empty spaces left
def empty_spaces():
    spaces = 9

    for row in range(3):
        for col in range(3):
            if buttons[row][col]['text'] != "":
                spaces -=1

    if spaces == 0:
        return False
    else:
        return  True




# Function to reset the game for a new game
def new_game():
    global player
    player = random.choice(players)
    label.config(text=player + " turn")
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="",bg="gray")


# Set up the game window
window = Tk()
window.title("Tic-Tac-Toe")
players = ["x", "o"]
player = random.choice(players)
buttons = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Label to show the current player's turn
label = Label(text=player + " turn", font=('Times Roman', 40))
label.pack(side="top")

# Button to reset the game
reset_button = Button(text="Restart", font=('consolas', 20), command=new_game)
reset_button.pack(side="top")

# Frame to hold the buttons for the tic-tac-toe board
frame = Frame(window)
frame.pack()

# Create the 3x3 grid of buttons
for row in range(3):
    for col in range(3):
        buttons[row][col] = Button(frame, text="", font=('consolas', 20), width=5, height=2,
                                   command=lambda row=row, col=col: next_turn(row, col))
        buttons[row][col].grid(row=row, column=col)

window.mainloop()
