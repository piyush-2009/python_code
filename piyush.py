import turtle
import math

screen = turtle.Screen()
screen.bgcolor("skyblue")
screen.title("3D Style White Birthday Cake")

pen = turtle.Turtle()

# Function to draw ellipse (used for top of cake layers)
def draw_ellipse(x, y, radius_x, radius_y, color):
    pen.penup()
    pen.goto(x + radius_x, y)
    pen.pendown()
    pen.color("black", color)
    pen.begin_fill()
    for i in range(361):
        angle = math.radians(i)
        x_offset = radius_x * math.cos(angle)
        y_offset = radius_y * math.sin(angle)
        pen.goto(x + x_offset, y + y_offset)
    pen.end_fill()

# Function to draw cake layer (cylinder shape)
def draw_cake_layer(x, y, width, height, color):
    draw_ellipse(x, y + height, width // 2, 10, color)
    pen.penup()
    pen.goto(x - width // 2, y + height)
    pen.pendown()
    pen.color("black", color)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(width)
        pen.right(90)
        pen.forward(height)
        pen.right(90)
    pen.end_fill()
    draw_ellipse(x, y, width // 2, 10, color)

# Function to draw candle
def draw_candle(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.setheading(0)
    pen.pendown()
    pen.color("black", "white")
    pen.begin_fill()
    for _ in range(2):
        pen.forward(3)
        pen.left(90)
        pen.forward(20)
        pen.left(90)
    pen.end_fill()

    pen.penup()
    pen.goto(x + 2.5, y + 20)
    pen.color("orange")
    pen.begin_fill()
    pen.circle(5)
    pen.end_fill()

# Draw cake layers
draw_cake_layer(0, -150, 150, 40, "white")
draw_cake_layer(0, -110, 120, 40, "white")
draw_cake_layer(0, -70, 90, 40, "white")

# Draw candles on top
for i in range(-40, 50, 20):
    draw_candle(i, -30)

# Centered birthday message
pen.penup()
pen.goto(0, 100)
pen.color("red")

pen.write("🎉🎂 Happy Birthday mara bhai 🎂🎉", align="center", font=("Arial", 18, "bold"))

pen.hideturtle()
turtle.done()

