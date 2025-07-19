import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Heart Drawing with Turtle")

# Create turtle
heart = turtle.Turtle()
heart.color("red")
heart.pensize(3)
heart.speed(2)

# Function to draw heart
def draw_heart():
    heart.begin_fill()
    heart.left(140)
    heart.forward(180)
    heart.circle(-90, 200)
    heart.left(120)
    heart.circle(-90, 200)
    heart.forward(180)
    heart.end_fill()

# Draw the heart
draw_heart()

# Add text inside heart
heart.penup()
heart.goto(0, -40)
heart.color("white")
heart.hideturtle()
heart.write("I ❤️ Python", align="center", font=("Arial", 20, "bold"))

# Keep window open
turtle.done()
