import turtle

flag = turtle.Turtle()
flag.pensize(2)
flag.speed(5)
flag.penup()
flag.goto(-300, 300)
flag.pendown()

def linea(posicion, distancia):
    flag.seth(posicion)
    flag.fd(distancia)

# *linea superior
flag.fillcolor('#01AAC9')
flag.begin_fill()
flag.color('#01AAC9')
linea(0, 600)
linea(270, 100)
linea(180, 600)
linea(90, 100)
flag.end_fill()

# *linea del centro
flag.penup()
flag.goto(-300, 200)
flag.pendown()
flag.fillcolor('#F9DF40')
flag.begin_fill()
flag.color('#F9DF40')
linea(0, 600)
linea(270, 100)
linea(180, 600)
linea(90, 100)
flag.end_fill()

# *linea inferior
flag.penup()
flag.goto(-300, 100)
flag.pendown()
flag.fillcolor('#01AAC9')
flag.begin_fill()
flag.color('#01AAC9')
linea(0, 600)
linea(270, 100)
linea(180, 600)
linea(90, 100)
flag.end_fill()

# *triangulo
flag.penup()
flag.goto(-300, 300)
flag.pendown()
flag.fillcolor('#000000')
flag.begin_fill()
flag.color('#000000')
flag.goto(-50, 150)
flag.goto(-300, 0)
flag.goto(-300, 300)
flag.end_fill()

# *texto
flag.penup()
flag.goto(0, -150)
flag.pendown()
flag.color('#000000')
flag.write("BAHAMAS", False, 
        "center", ("Arial", 50, "bold"))


# *esconde el lapiz de dibujo
flag.hideturtle()
# *evita que la ventana se cierre cuando se ejecuta el código
turtle.done()