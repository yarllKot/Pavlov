import turtle

def draw_fractal(scale):
    if scale >= 10:
        draw_fractal(scale / 2.0)
        turtle.left(30)
        draw_fractal(scale / 2.0)
        turtle.right(60)
        draw_fractal(scale / 2.0)
        turtle.left(30)
        draw_fractal(scale / 2.0)
    else:
        turtle.forward(scale)

scale = 400

turtle.speed(10)
turtle.pensize(2)
turtle.penup()
turtle.goto(-scale, -scale/4)
turtle.pendown()

draw_fractal(scale)
turtle.done()