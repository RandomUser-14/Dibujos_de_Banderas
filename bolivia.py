import turtle

flag = turtle.Turtle()
flag.pensize(2)
flag.speed(5)
flag.penup()
flag.goto(-260, 300)
flag.pendown()

def linea(posicion, distancia):
    flag.seth(posicion)
    flag.fd(distancia)

# *linea superior
flag.fillcolor('#CE1127')
flag.begin_fill()
flag.color('#CE1127')
linea(0, 520)
linea(270, 100)
linea(180, 520)
linea(90, 100)
flag.end_fill()

# *linea del centro
flag.penup()
flag.goto(-260, 200)
flag.fillcolor('#F9D716')
flag.begin_fill()
flag.color('#F9D716')
flag.pendown()
linea(0, 520)
linea(270, 100)
linea(180, 520)
linea(90, 100)
flag.end_fill()


# *linea inferior
flag.penup()
flag.goto(-260, 100)
flag.fillcolor('#007A3D')
flag.begin_fill()
flag.color('#007A3D')
flag.pendown()
linea(0, 520)
linea(270, 100)
linea(180, 520)
linea(90, 100)
flag.end_fill()

# *texto
flag.penup()
flag.goto(0, -150)
flag.pendown()
flag.color('#000000')
flag.write("BOLIVIA", False, 
        "center", ("Arial", 50, "bold"))

flag.hideturtle()
turtle.done()