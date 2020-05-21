from turtle import *
color = ('red', 'blue', 'brown', 'yellow', 'grey')
ind = color.index
#z = [3, 4, 5, 6, 7 ,8]
for edge in range(3, 8):
    for i in range(edge):
        color = ind
        forward(100)
        left(360/edge)
mainloop()
# need corrections