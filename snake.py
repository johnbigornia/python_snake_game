from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.is_up = False
        self.is_down = False
        self.is_left = False
        self.is_right = True
        self.head = self.snake_segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def extend(self):
        #add a new segment into snake
        self.add_segment(self.snake_segments[-1].position())

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.snake_segments.append(new_segment)

    def move(self):
        # from last to first segment
        # will move to the next segment and the next segment will move to the next one
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[seg_num - 1].xcor()
            new_y = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if not self.is_down and self.is_right:
            self.head.left(90)
            self.is_right = False
            self.is_up = True
        if not self.is_down and self.is_left:
            self.head.left(-90)
            self.is_left = False
            self.is_up = True

    def down(self):
        if not self.is_up and self.is_right:
            self.head.left(-90)
            self.is_right = False
            self.is_down = True
        if not self.is_up and self.is_left:
            self.snake_segments[0].left(90)
            self.is_left = False
            self.is_down = True

    def left(self):
        if not self.is_left and self.is_up:
            self.head.left(90)
            self.is_up = False
            self.is_left = True
        if not self.is_left and self.is_down:
            self.head.left(-90)
            self.is_down = False
            self.is_left = True

    def right(self):
        if not self.is_left and self.is_up:
            self.head.left(-90)
            self.is_up = False
            self.is_right = True
        if not self.is_left and self.is_down:
            self.head.left(90)
            self.is_down = False
            self.is_right = True

