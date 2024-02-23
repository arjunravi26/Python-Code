from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for positions in STARTING_POSITIONS:
            self.add_segment(positions)

    def add_segment(self, positions):
        segment = Turtle('square')
        segment.penup()
        segment.color('white')
        segment.goto(positions)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def left_move(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right_move(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up_move(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down_move(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
