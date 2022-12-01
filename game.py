### Import required packages. ###

from turtle import Turtle

### Used dictionaries. ###


numbers_dict = {1: [-150, 20], 2: [-50, 20], 3: [65, 20], 4: [-150, -55], 5: [-50, -55], 6: [65, -55], 7: [-150, -120],
                8: [-50, -120], 9: [65, -120]}


class Game:

    def __init__(self):
        super().__init__()

    def write_positions(self):
        for k, v in numbers_dict.items():
            t = Turtle("triangle")
            t.hideturtle()
            t.speed(0)
            t.penup()
            t.color("black")
            t.goto(v[0], v[1])
            t.write(k, True, align="center", font=("Verdana", 20, "bold"))

    def place_symbol(self, symbol, position):
        t = Turtle("triangle")
        t.speed("fastest")
        t.penup()
        t.color("red")
        t.goto(position)
        t.write(symbol, True, align="center", font=("Verdana", 40, "bold"))
        t.hideturtle()

    def tie(self):
        t = Turtle("triangle")
        t.speed("fastest")
        t.penup()
        t.color("black")
        t.goto(0, -300)
        t.write("This is a tie. Thank you for playing.", True, align="center", font=("Verdana", 20, "bold"))
        t.hideturtle()

    def win(self, player):
        t = Turtle("triangle")
        t.speed("fastest")
        t.penup()
        t.color("black")
        t.goto(0, -300)
        t.write(f"{player} has won. Thank you for playing.", True, align="center", font=("Verdana", 20, "bold"))
        t.hideturtle()
