from turtle import Turtle, Screen
from tkinter import Button, Radiobutton, IntVar, Label
from tkinter.ttk import Style
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
        self.screen.bgcolor("#FFFBE9")
        self.screen.setup(width=600, height=600)
        
        self.screen.tracer(0)
        self.create_logo()
        self.create_hint_button()
        self.create_new_button()
        self.create_radio_button()
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
        drawer.pencolor("#AD8B73")
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
        self.hint_button = Button(canvas.master, text="Hint", command=self.hint)
        self.hint_button.config(foreground="#f9f6f2", activeforeground="#f9f6f2", background="#8f7a66", activebackground="#bbada0", font=("Clear Sans", 12, 'bold'))
        self.hint_button.config(disabledforeground="#f9f6f2")
        self.hint_button.config(state="disabled")
        canvas.create_window(130, -180, window=self.hint_button)
    
    def active_hint_button(self):
        self.alert.clear()
        self.hint_button.config(state="normal")

    def create_new_button(self):
        canvas = self.screen.getcanvas()
        self.new_button = Button(canvas.master, text="New Game", command=self.new)
        self.new_button.config(foreground="#f9f6f2", activeforeground="#f9f6f2", background="#8f7a66", activebackground="#bbada0", font=("Clear Sans", 12, 'bold'))
        self.new_button.config(disabledforeground="#f9f6f2")
        canvas.create_window(205, -180, window=self.new_button)

    def create_radio_button(self):
        self.radio_state = IntVar()
        canvas = self.screen.getcanvas()
        label = Label(canvas.master, text="Algorithm:")
        label.config(width=10, font=("Clear Sans", 12, 'bold'), foreground="#776e65", background="#FFFBE9")
        self.radiobutton1 = Radiobutton(canvas.master, text="BFS", value=1, variable=self.radio_state, command=self.active_hint_button)
        self.radiobutton2 = Radiobutton(canvas.master, text="Backtracking", value=2, variable=self.radio_state, command=self.active_hint_button)
        self.radiobutton1.config(foreground="#776e65", activeforeground="#776e65", background="#FFFBE9", activebackground="#FFFBE9", font=("Clear Sans", 10, 'bold'))
        self.radiobutton2.config(foreground="#776e65", activeforeground="#776e65", background="#FFFBE9", activebackground="#FFFBE9", font=("Clear Sans", 10, 'bold'))
        canvas.create_window(210, -135, window=label)
        canvas.create_window(200, -105, window=self.radiobutton1)
        canvas.create_window(228, -75, window=self.radiobutton2)

        self.alert = Turtle()
        self.alert.hideturtle()
        self.alert.penup()
        self.alert.goto(0, 170)
        self.alert.pencolor('#776e65')
        self.alert.write('Please choice Algorithm!', align='center', font=("Clear Sans", 12, 'bold'))

    def intialize(self):
        start_pos = -2 * WIDTH
        for block in self.manager.all_block:
            segment = Turtle()
            segment.hideturtle()
            segment.penup()
            segment.goto(start_pos + 60*block.pos_num[1], start_pos + 60*block.pos_num[0] - 15)
            segment.pencolor("#776e65")
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
        self.drawer.pencolor("#AD8B73")
        for _ in range(2):
            self.drawer.forward(60*width)
            self.drawer.left(90)
            self.drawer.forward(60*height)
            self.drawer.left(90)
        self.drawer.penup()

    def hint(self):
        if self.step == 0:
            if self.radio_state.get() == 1:
                goal_node = self.solver.bfs()
            elif self.radio_state.get() == 2:
                goal_node = self.solver.backtracking()
            self.manager.goal_state = goal_node.state
        
        goal_state = self.manager.goal_state
        if self.step < len(goal_state) - 1:
            self.new_button.config(state="disabled")
            block = goal_state[self.step]
            self.draw_block(block)
            self.step += 1
            self.screen.update()
        else:
            self.alert.write('Found goal state!', align='center', font=("Clear Sans", 12, 'bold'))
            self.new_button.config(state="normal")

    def new(self):
        for segment in self.all_segment:
            segment.clear()
        self.drawer.clear()
        self.alert.clear()
        self.alert.write('Please choice Algorithm!', align='center', font=("Clear Sans", 12, 'bold'))
        self.radio_state.set(0)

        self.step = 0
        self.hint_button.config(state="disabled")
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
        drawer.pencolor('#361500')
        drawer.write('GAME OVER', align='center', font=("Merriweather", 50, 'normal'))
