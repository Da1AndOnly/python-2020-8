import turtle
tortoise = turtle.Turtle()
tortoise.penup()
tortoise.shape('turtle')
step = 20
for i in range(50):
    tortoise.forward(step)
    tortoise.left(24)                                          
    tortoise.stamp()
    step = step + 3
turtle.done()
