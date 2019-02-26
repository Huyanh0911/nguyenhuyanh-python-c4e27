from turtle import *
speed(0)

color("red")

left(30)
for v in range(4):
    for i in range(2):
        forward(100)
        right(60)
        forward(100)
        right(120)
    right(90)

mainloop()