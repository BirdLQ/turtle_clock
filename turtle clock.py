# -*- coding: utf-8 -*-
"""
@author: BirdLQ
"""

import turtle

heure_=int(input("Enter the time in hh format: "))
minute_=int(input("Enter the minutes in mm format: "))
seconde_=int(input("Enter the seconds in ss format: "))

#calculate time
def formt(h, m, s):
    minute, seconde = divmod(s, 60)
    heure, minute = divmod(minute+m, 60)
    heure = (heure+h)%12
    
    return heure, minute, seconde

#The time is entered by the user
def write_time(heure, minute, seconde):    
    t.undo()
    t.goto(-75,-250)
    
    t.write("It's : {:02d}:{:02d}:{:02d} {moment}".format(heure, minute, seconde, 
            moment = "pm" if heure_ > 12 else "am"), font=("Arial", 16, "normal"))

#fonction to calculate hands angles
def angle(h, m, s):
    angle_s= (360 / 60) * s
    angle_m= (360 / 60) * m + angle_s/60
    angle_h= (360 / 12) * h + angle_m/12
    
    return angle_h, angle_m, angle_s

#clock face
def horloge(x=0, y=0, c=200, e=180, p=20, e_e=185, p_p=15):
    '''
    Parameters
    ----------
    x : int()
        Abscissa starting point.
    
    y : int()
        Ordinate starting point.
    
    c : int()
        Clock face size.
    
    e : int()
        Hours clock index starting position.
    
    p : int()
        Hours clock index size.
        
    e_e : int()
        Minutes clock index starting position.
        
    p_p : int()
        Minutes clock index size.
        
    Returns
    -------
    None.

    '''
    t.penup()
    t.goto(x+c,y)
    t.clear()
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
def aigh(h, x=0, y=0, f=100):
    '''
    Parameters
    ----------
    x : int()
        Abscissa starting point.
        
    y : int()
        Ordinate starting point.
        
    f : int()
        clock hour hand size.

    Returns
    -------
    None.

    '''
    hour_t.goto(x, y)
    hour_t.clear()
    hour_t.setheading(h)
    hour_t.forward(f)

def aigm(m, x=0, y=0, f=150):
    '''
    Parameters
    ----------
    x : int()
        Abscissa starting point.
        
    y : int()
        Ordinate starting point.
    
    f : int()int()
        clock minutes size.

    Returns
    -------
    None.

    '''
    min_t.goto(x, y)
    min_t.clear()
    min_t.setheading(m)
    min_t.forward(f)

def aigs(s, x=0, y=0, f=170):
    '''
    Parameters
    ----------
    x : int()
        Abscissa starting point.
    
    y : int()
        Ordinate starting point.
    
    f : int()
        clock seconds size.

    Returns
    -------
    None.

    '''
    sec_t.goto(x, y)
    sec_t.clear()
    sec_t.setheading(s)
    sec_t.forward(f)

def draw(h, m, s):
    aigh(h)
    aigm(m)
    aigs(s)

heure, minute, seconde = formt(heure_, minute_, seconde_)
    
def refresh():
    global heure, minute, seconde
    
    heure, minute, seconde = formt(heure, minute, seconde)

    write_time(heure, minute, seconde)
    # get the hands angles
    agl_h, agl_m, agl_s = angle(heure, minute, seconde)

    # draw the hands
    draw(agl_h, agl_m, agl_s)

    seconde += 1

    screen.update()

    screen.ontimer(refresh, 1000)

screen = turtle.Screen()
screen.title("Clock")
screen.mode('logo')  # 0 degrees at top, circles go clockwise, like a clock!
screen.tracer(False)

# main turtle
t = turtle.Turtle()
t.hideturtle()
t.width(5)

horloge() #draw clock face

# turtles for hands
hour_t = turtle.Turtle()
hour_t.hideturtle()
hour_t.width(10)

min_t = turtle.Turtle()
min_t.hideturtle()
min_t.width(5)

sec_t = turtle.Turtle()
sec_t.hideturtle()
sec_t.width(1)
sec_t.color("red")

refresh()

screen.mainloop()
