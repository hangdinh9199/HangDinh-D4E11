from turtle import *
speed(-1)
color('blue')
for edge in range(3, 7):
    for i in range(edge):
        if edge == 3 or edge == 5:
            color('blue')
        else:
            color('red')
        forward(100)
        left(360/edge)
    
mainloop()