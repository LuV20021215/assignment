from turtle import *

def draw_spiral():
    # from turtle import *
    
    bgcolor('lavender')
    x = 1

    speed(10000)
    while x < 240:




        pencolor("lavender")
        fd(4 + x)
        rt(90.0001)
        x = x + 1

        pencolor("lavender")
        fd(4 + x)
        rt(120.0001)


    while x < 400:




        pencolor("violet")
        fd(4 + x)
        rt(90.0001)


        pencolor("cornflowerblue")
        fd(4 + x)
        rt(120.0001)

        pencolor("royalblue")
        fd(4 + x)
        rt(90.0001)
        pencolor("Purple")
        fd(4 + x)
        rt(120.0001)
        x = x + 2




    exitonclick()

draw_spiral()