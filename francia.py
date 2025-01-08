import turtle

flag = turtle.Turtle()
flag.pensize(2)
flag.speed(3)
flag.penup()
flag.goto(-300, 300)
flag.pendown()

def linea(posicion, distancia):
    flag.seth(posicion)
    flag.fd(distancia)


flag.fillcolor("blue4")
flag.begin_fill()
flag.color("blue4")
linea(0, 200)
linea(270, 300)
linea(180, 200)
linea(90, 300)
flag.end_fill()

flag.penup()
flag.goto(-100, 300)
flag.pendown()
flag.fillcolor("ghostwhite")
flag.begin_fill()
flag.color("ghostwhite")
linea(0, 200)
linea(270, 300)
linea(180, 200)
linea(90, 300)
flag.end_fill()

flag.penup()
flag.goto(100, 300)
flag.pendown()
flag.fillcolor("red")
flag.begin_fill()
flag.color("red")
linea(0, 200)
linea(270, 300)
linea(180, 200)
linea(90, 300)
flag.end_fill()

flag.penup()
flag.goto(0, -150)
flag.pendown()
flag.color("black")
flag.write("FRANCIA", False,
           "center", ("Arial", 50, "bold"))

flag.hideturtle()
turtle.done()