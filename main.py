### Import required packages. ###

import turtle
from tkinter import *
from game import Game

### Turtle Initialization. ###

screen = turtle.Screen()
screen.title("")

image = "ttt.gif"
screen.addshape(image)
turtle.shape(image)

### Function to get x,y coordinates. ###

# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)

### Pre-game Configs & Dictionaries ###

game = Game()
pre_game_is_on = True
game_is_on = False
turn_player_1 = True
symbols_dict = {1: [-110, 40], 2: [-10, 40], 3: [100, 40], 4: [-110, -50], 5: [-10, -50], 6: [100, -50],
                7: [-110, -130], 8: [-10, -130], 9: [100, -130]}
positions_dict = {1: "P", 2: "P", 3: "P", 4: "P", 5: "P", 6: "P", 7: "P", 8: "P", 9: "P"}

### Call & Speed-up initial drawing. ###

turtle.tracer(n=1000, delay=0)
game.write_positions()


### Make sure with TKinter that the Message Window is in the right place. ###


def textinput(title, question):
    message = Tk()
    message.title(str(title))
    message.config(padx=2, pady=10, bg='white')
    message.geometry('%dx%d+%d+%d' % (450, 120, 100, 100))
    l = Label(message, text=str(question), font=("Verdana", 14, "bold"), bg='white', fg='black')
    l.place(x=3, y=5)
    e = Entry(message, width=28)
    e.focus_set()
    e.place(x=3, y=40)

    def submit(event="<Return>"):
        global answer
        answer = e.get()

        message.destroy()

    b = Button(message, highlightbackground='white', width=26, text="Submit Input", borderwidth=2, command=submit)
    b.place(x=3, y=80)
    b.bind_all("<Return>", submit)

    message.wait_window()


def numinput(title, question):
    message = Tk()
    message.title(str(title))
    message.config(padx=2, pady=10, bg='white')
    message.geometry('%dx%d+%d+%d' % (450, 120, 100, 100))
    l = Label(message, text=str(question), font=("Verdana", 14, "bold"), bg='white', fg='black')
    l.place(x=3, y=5)
    e = Entry(message, width=28)
    e.focus_set()
    e.place(x=3, y=40)

    def submit(event="<Return>"):
        global answer
        answer = int(e.get())

        message.destroy()

    b = Button(message, highlightbackground='white', width=26, text="Submit Input", borderwidth=2, command=submit)
    b.place(x=3, y=80)
    b.bind_all("<Return>", submit)

    message.wait_window()


### Pre-Game text input to get names of players. ###


while pre_game_is_on:
    textinput("Player 1", f"First Player, what is your name?")
    player_1 = answer
    textinput("Player 2", f"Second Player, what is your name?")
    player_2 = answer
    pre_game_is_on = False
    game_is_on = True

### Actual game loop. ###

while game_is_on:
    if "P" in positions_dict.values():
        if turn_player_1:
            numinput("Player 1", f"{player_1}, at what position would you like to "
                                 f"place 'X'?")
            if positions_dict[answer] == "X" or positions_dict[answer] == "O":
                numinput("Invalid Choice", f"{player_1}, invalid choice. Try again.")

            game.place_symbol("X", (symbols_dict.get(answer)[0], symbols_dict.get(answer)[1]))
            positions_dict.update({answer: "X"})
            turn_player_1 = False
            if positions_dict[1] == "X" and positions_dict[2] == "X" and positions_dict[3] == "X":
                game.win(player_1)
                game_is_on = False
            elif positions_dict[1] == "X" and positions_dict[4] == "X" and positions_dict[7] == "X":
                game.win(player_1)
                game_is_on = False
            elif positions_dict[4] == "X" and positions_dict[5] == "X" and positions_dict[6] == "X":
                game.win(player_1)
                game_is_on = False
            elif positions_dict[7] == "X" and positions_dict[8] == "X" and positions_dict[9] == "X":
                game.win(player_1)
                game_is_on = False
            elif positions_dict[2] == "X" and positions_dict[5] == "X" and positions_dict[8] == "X":
                game.win(player_1)
                game_is_on = False
            elif positions_dict[3] == "X" and positions_dict[6] == "X" and positions_dict[9] == "X":
                game.win(player_1)
                game_is_on = False
            elif positions_dict[1] == "X" and positions_dict[5] == "X" and positions_dict[9] == "X":
                game.win(player_1)
                game_is_on = False
            elif positions_dict[3] == "X" and positions_dict[5] == "X" and positions_dict[7] == "X":
                game.win(player_1)
                game_is_on = False
        else:
            numinput("Player 2", f"{player_2}, at what position would you like to "
                                 f"place 'O'?")
            if positions_dict[answer] == "X" or positions_dict[answer] == "O":
                numinput("Invalid Choice", f"{player_2}, invalid choice. Try again.")

            game.place_symbol("O", (symbols_dict.get(answer)[0], symbols_dict.get(answer)[1]))
            positions_dict.update({answer: "O"})
            turn_player_1 = True
            if positions_dict[1] == "O" and positions_dict[2] == "O" and positions_dict[3] == "O":
                game.win(player_2)
                game_is_on = False
            elif positions_dict[1] == "O" and positions_dict[4] == "O" and positions_dict[7] == "O":
                game.win(player_2)
                game_is_on = False
            elif positions_dict[4] == "O" and positions_dict[5] == "O" and positions_dict[6] == "O":
                game.win(player_2)
                game_is_on = False
            elif positions_dict[7] == "O" and positions_dict[8] == "O" and positions_dict[9] == "O":
                game.win(player_2)
                game_is_on = False
            elif positions_dict[2] == "O" and positions_dict[5] == "O" and positions_dict[8] == "O":
                game.win(player_2)
                game_is_on = False
            elif positions_dict[3] == "O" and positions_dict[6] == "O" and positions_dict[9] == "O":
                game.win(player_2)
                game_is_on = False
            elif positions_dict[1] == "O" and positions_dict[5] == "O" and positions_dict[9] == "O":
                game.win(player_2)
                game_is_on = False
            elif positions_dict[3] == "O" and positions_dict[5] == "O" and positions_dict[7] == "O":
                game.win(player_2)
                game_is_on = False
    else:
        game.tie()
        game_is_on = False

screen.exitonclick()
