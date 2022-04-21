import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)
    # for i in range(5,9):
    #     some_turtle.left(90)
    #     some_turtle.forward(100)

# def draw_triangle(mak):
#     for i in range(1,4):
#         mak.right(120)
#         mak.forward(100)

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")
    
#For Square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("white")
    brad.speed(2)
    for i in range(1,36):
        draw_square(brad)
        brad.right(10)

# #For Circle    
#     angie = turtle.Turtle()
#     angie.shape("arrow")
#     angie.color("yellow")
#     angie.speed(0)
#     angie.circle(100)

# #For Triangle    
        
#     mak = turtle.Turtle()
#     mak.shape("turtle")
#     mak.color("white")    
#     mak.speed(0)   
#     draw_triangle(mak)

    window.exitonclick()

draw_shapes()
