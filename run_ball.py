import turtle
import ball
import random
import seven_segments_proc

class Ball_simulator:
    def __init__(self):
        self.tom = turtle.Turtle()
        self.num_balls = 5
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        print(self.canvas_width, self.canvas_height)
        self.ball_radius = 0.05 * self.canvas_width
        turtle.colormode(255)
        self.xpos = []
        self.ypos = []
        self.vx = []
        self.vy = []
        self.ball_color = []
        # create random number of balls, num_balls, located at random positions within the canvas; each ball has a random velocity value in the x and y direction and is painted with a random color
        for i in range(self.num_balls):
            self.xpos.append(
                random.uniform(-1 * self.canvas_width + self.ball_radius, self.canvas_width - self.ball_radius))
            self.ypos.append(
                random.uniform(-1 * self.canvas_height + self.ball_radius, self.canvas_height - self.ball_radius))
            self.vx.append(10 * random.uniform(-1.0, 1.0))
            self.vy.append(10 * random.uniform(-1.0, 1.0))
            self.ball_color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    def __draw_border(self):
        turtle.penup()
        turtle.goto(-self.canvas_width, -self.canvas_height)
        turtle.pensize(10)
        turtle.pendown()
        turtle.color((0, 0, 0))
        for i in range(2):
            turtle.forward(2 * self.canvas_width)
            turtle.left(90)
            turtle.forward(2 * self.canvas_height)
            turtle.left(90)

    def run(self):
        dt = 0.2  # time step

        while (True):
            self.tom.clear()
            self.__draw_border()

            for i in range(self.num_balls):
                ball_run = ball.Ball()
                ball_run.draw_ball(color=self.ball_color[i], size=self.ball_radius, x=self.xpos[i], y=self.ypos[i])
                ball_run.move_ball(i, self.xpos, self.ypos, self.vx, self.vy, dt)
                ball_run.update_ball_velocity(i, self.xpos, self.ypos, self.vx, self.vy, self.canvas_width,
                                               self.canvas_height, self.ball_radius)

            tao = turtle.Turtle()
            tao_color = (255, 0, 0)
            run = seven_segments_proc.Seven(tao, tao_color)
            run.Run()
            turtle.update()


        # hold the window; close it by clicking the window close 'x' mark

        turtle.done()


run_ball = Ball_simulator()
run_ball.run()

