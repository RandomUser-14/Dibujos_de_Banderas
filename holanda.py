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


flag.fillcolor("red")
flag.begin_fill()
flag.color("red")
linea(0, 600)
linea(270, 100)
linea(180, 600)
linea(90, 100)
flag.end_fill()

flag.penup()
flag.goto(-300, 200)
flag.pendown()
flag.color("ghostwhite")
flag.fillcolor("ghostwhite")
flag.begin_fill()
linea(0, 600)
linea(270, 100)
linea(180, 600)
linea(90, 100)
flag.end_fill()

flag.penup()
flag.goto(-300, 100)
flag.pendown()
flag.color("blue4")
flag.fillcolor("blue4")
flag.begin_fill()
linea(0, 600)
linea(270, 100)
linea(180, 600)
linea(90, 100)
flag.end_fill()

flag.penup()
flag.goto(0, -150)
flag.pendown()
flag.color("black")
flag.write("HOLANDA", False,
           "center", ("Arial", 50, "bold"))

flag.hideturtle()
turtle.done()
