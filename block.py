from turtle import Turtle
START_POS = -60 *2


# use for algorithm
class Block:
    def __init__(self, pos: tuple):
        self.pos_num = pos
        self.start_pos = pos
        self.width = 1
        self.height = 1
        

# use for GUI
class BlockGraphic(Turtle, Block):
    def __init__(self, pos: tuple):
        Turtle.__init__()
        Block.__init__(pos)

        self.hideturtle()
        self.penup()
        self.goto(START_POS + 60*self.pos_num[1], START_POS + 60*self.pos_num[0])
