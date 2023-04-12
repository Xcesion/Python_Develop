import colorgram
import turtle as t
import random
#TODO if we want to use rgb mode to set different color in dot function
t.colormode(255)
colors = colorgram.extract('image.jpg', 30)
list = []
for i in colors:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    new_color = (r, g, b)
    list.append(new_color)
paint = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (186, 158, 53), (6, 57, 83), (109, 67, 85),
         (113, 161, 175), (22, 122, 174), (64, 153, 138),
         (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151),
         (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120),
         (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]

tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.setposition(-200,-200)

for i in range(10):
    for j in range(10):
        tim.dot(20,random.choice(paint))
        tim.penup()
        tim.forward(40)
    tim.backward(10*40)
    tim.left(90)
    tim.forward(40)
    tim.right(90)
sc= t.Screen()
sc.exitonclick()