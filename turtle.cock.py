import turtle
heure=int(input("Enter the time in hh format"))
minute=int(input("Enter the minutes in mm format "))
seconde=int(input("Enter the seconds in the format ss"))

t = turtle.Turtle()
t.ht()
t.speed(100)

#The time is entered by the user
h1=[heure, minute, seconde]
if heure > 12:
    print("It's", ":".join(map(str, h1)), "pm")
else:
    print("It's", ":".join(map(str, h1)), "am")

#fonction pour calculer l'heure

while heure>12:
    heure=heure-12

while minute>=60:
    r=minute%61
    q=minute//61
    minute=q

while seconde>=60:
    r=seconde%61
    q=seconde//61
    seconde=q

h=0.5 * (heure * 60 + minute)
m=360/60*minute
s=360/60*seconde

#clock face
def horloge(x, y, c, e, p, e_e, p_p):
    t.width(5)
    t.penup()
    t.goto(x,y-c)
    t.pendown()
    t.circle(c)
    t.left(90)
    t.penup()
    t.forward(c)
    for loop in range(12):
        t.width(3)  
        t.forward(e)
        t.pendown()
        t.forward(p)
        t.penup()
        t.goto(x,y)
        t.left(30)
    for loop in range(60):
        t.width(1)
        t.forward(e_e)
        t.pendown()
        t.forward(p_p)
        t.penup()
        t.goto(x,y)
        t.left(6)

#hands
def aigh(x, y, f):
    t.goto(x,y)
    t.setheading(90)
    t.rt(h)
    t.pendown()
    t.width(10)
    t.forward(f)

def aigm(x, y, f):
    t.goto(x,y)
    t.setheading(90)
    t.rt(m)
    t.pendown()
    t.width(5)
    t.forward(f)

def aigs(x, y, f):
    t.goto(x,y)
    t.setheading(90)
    t.color("red")
    t.width()
    t.rt(s)
    t.pendown()
    t.width(1)
    t.forward(f)

horloge(0, 0, 200, 180, 20, 185, 15)
aigh(0, 0, 100)
aigm(0, 0, 150)
aigs(0, 0, 170)
