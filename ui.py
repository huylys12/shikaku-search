from turtle import Turtle, Screen
from tkinter import Button
from block import BlockManager, Block
from search import Solver
FONT = ("Merriweather", 22, "bold")
WIDTH = 60


class GUI:
    def __init__(self, block_manager: BlockManager, solver: Solver):
        self.step = 0
        self.manager = block_manager
        self.solver = solver
        # list Turtle
        self.all_segment = []
        self.screen = Screen()
        self.screen.title("Shikaku - Puzzle Game")
        self.screen.setup(width=600, height=600)
        
        self.screen.tracer(0)
        self.create_logo()
        self.create_hint_button()
        self.create_new_button()
        self.create_frame()
        self.intialize()

        self.drawer = Turtle()
        self.drawer.hideturtle()
        self.drawer.penup()
        
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


    def draw_block(self, block: Block):
        start_val = -WIDTH * 2 - 30
        start_pos = block.start_pos
        width = block.width
        height = block.height

        self.drawer.goto(start_val + 60*start_pos[1], start_val + 60*start_pos[0])
        self.drawer.pendown()
        self.drawer.pensize(8)
        self.drawer.pencolor("black")
        for _ in range(2):
            self.drawer.forward(60*width)
            self.drawer.left(90)
            self.drawer.forward(60*height)
            self.drawer.left(90)
        self.drawer.penup()

    def hint(self):
        if self.step == 0:
            goal_node = self.solver.bfs()
            self.manager.goal_state = goal_node.state
        
        goal_state = self.manager.goal_state
        if self.step < len(goal_state) - 1:
            block = goal_state[self.step]
            self.draw_block(block)
            self.step += 1
            self.screen.update()
        else:
            self.drawer.goto(0, 170)
            self.drawer.pencolor('#092')
            self.drawer.write('Found goal state', align='center', font=("Tahoma", 12, 'normal'))
            

    def new(self):
        for segment in self.all_segment:
            segment.clear()
        self.drawer.clear()
        self.step = 0
        self.all_segment.clear()
        if self.manager.generate():
            self.manager.create()
            self.intialize()
        else:
            self.game_over()

    def game_over(self):
        drawer = Turtle()
        drawer.hideturtle()
        drawer.penup()
        drawer.goto(0, -30)
        drawer.pencolor('#E83A14')
        drawer.write('GAME OVER', align='center', font=("Merriweather", 50, 'normal'))
