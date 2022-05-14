import turtle

def draw_square(some_turtle):
    for i in range(1,3):
        some_turtle.right(140)
        some_turtle.forward(100)
        some_turtle.right(40)
        some_turtle.forward(100)

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")
    
#For Square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("white")
    brad.speed(0)
    for i in range(1,73):
        draw_square(brad)
        brad.right(5)
    brad.right(90)
    brad.forward(300)

    window.exitonclick()

draw_shapes()