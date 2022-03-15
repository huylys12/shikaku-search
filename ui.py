from turtle import Turtle, Screen
from tkinter import Button
from block import BlockManager, Block
FONT = ("Merriweather", 22, "bold")
WIDTH = 60


class GUI:
    def __init__(self, block_manager: BlockManager):
        self.manager = block_manager
        # list Turtle
        self.all_segment = []
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        
        self.screen.tracer(0)
        self.create_logo()
        self.create_hint_button()
        self.create_new_button()
        self.create_frame()
        self.intialize()
        self.screen.mainloop()

    def create_frame(self):
        start_pos = (-WIDTH * 2 - 30, -WIDTH * 2 - 30)
        drawer = Turtle()
        drawer.hideturtle()
        drawer.penup()
        def draw_dots():
            for i in range(20):
                if i % 4 == 0:
                    drawer.dot(8)
                else:
                    drawer.dot(3, "gray")
                drawer.forward(WIDTH / 4)

        drawer.goto(start_pos)
        for i in range(6):
            if i > 0:
                drawer.goto(-drawer.xcor(), drawer.ycor() + WIDTH)
            draw_dots()

        drawer.goto(start_pos)
        drawer.setheading(90)
        for i in range(6):
            if i > 0:
                drawer.goto(drawer.xcor() + WIDTH, -drawer.ycor())
            draw_dots()

        drawer.goto(start_pos)
        drawer.pendown()
        drawer.pensize(8)
        for _ in range(4):
            drawer.forward(WIDTH*5)
            drawer.right(90)
        self.screen.update()

    def create_logo(self):
        logo_img = "./images/shikaku-logo.gif"
        self.screen.addshape(logo_img)
        logo = Turtle(shape=logo_img)
        logo.penup()
        logo.goto(0, 230)

    def create_hint_button(self):
        canvas = self.screen.getcanvas()
        hint_button = Button(canvas.master, text="Hint", command=self.hint)
        canvas.create_window(90, -180, window=hint_button)
    
    def create_new_button(self):
        canvas = self.screen.getcanvas()
        new_button = Button(canvas.master, text="New", command=self.new)
        canvas.create_window(135, -180, window=new_button)

    def intialize(self):
        start_pos = -2 * WIDTH
        for block in self.manager.all_block:
            segment = Turtle()
            segment.hideturtle()
            segment.penup()
            segment.goto(start_pos + 60*block.pos_num[1], start_pos + 60*block.pos_num[0] - 15)
            segment.write(block.number, align='center', font=FONT)
            self.all_segment.append(segment)

    def hint(self):
        pass

    def new(self):
        pass