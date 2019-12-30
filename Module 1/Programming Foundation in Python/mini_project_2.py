import turtle

def draw_shape(shape):
    for i in range(5):
        shape.forward(100)
        shape.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor('blue')
    ope = turtle.Turtle('arrow')
    ope.shape('circle')
    ope.color('red')
    ope.speed(3)
    for i in range(5):
        draw_shape(ope)
        ope.right(10)
    
    window.exitonclick()

draw_art()