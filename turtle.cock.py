# -*- coding: utf-8 -*-
"""
@author: BirdLQ
"""

import turtle, time

heure_=int(input("Enter the time in hh format: "))
minute_=int(input("Enter the minutes in mm format: "))
seconde_=int(input("Enter the seconds in ss format: "))

#calculate time
def formt(h, m, s):
    minute, seconde = divmod(s, 60)
    heure, minute = divmod(minute+m, 60)
    heure = (heure+h)%12
    return heure, minute, seconde

heure, minute, seconde = formt(heure_, minute_, seconde_)

#The time is entered by the user
def write_time(heure, minute, seconde):
    t.goto(-75,-250)
    if heure_ > 12:
        t.write("It's : {:02d}:{:02d}:{:02d} pm".format(heure, minute, seconde),
                 font=("Arial", 16, "normal"))
    else:
        t.write("It's : {:02d}:{:02d}:{:02d} am".format(heure, minute, seconde),
                 font=("Arial", 16, "normal"))

#fonction to calculate hands angles
def angle(h, m, s):
    angle_s=(360 / 60) * s
    angle_m=(360 / 60) * m + angle_s*1/60
    angle_h=(360 / 12) * h + angle_m*1/12
    '''
    h=(1/60.0)*6*s
    m=(6.0*m)+angle_s
    s=(30.0*h/12)+angle_m
    '''
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
    t.ht()
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
    hour_t.ht()
    hour_t.goto(x,y)
    hour_t.setheading(90)
    hour_t.rt(h)
    hour_t.pendown()
    hour_t.width(10)
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
    min_t.ht()
    min_t.goto(x,y)
    min_t.setheading(90)
    min_t.rt(m)
    min_t.pendown()
    min_t.width(5)
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
    sec_t.ht()
    sec_t.goto(x,y)
    sec_t.setheading(90)
    sec_t.color("red")
    sec_t.width()
    sec_t.rt(s)
    sec_t.pendown()
    sec_t.width(1)
    sec_t.forward(f)

#init turtle
t = turtle.Turtle()

#turtles for hands
hour_t = turtle.Turtle()
min_t = turtle.Turtle()
sec_t = turtle.Turtle()

wn = turtle.Screen()
wn.title("Clock")

wn.tracer(0)

#draw the clock
horloge()

def draw(h, m, s):
    aigh(h)
    aigm(m)
    aigs(s)
    
def refresh(h=heure, m=minute, s=seconde):
    global seconde
    wn.tracer(0)
    hour_t.undo()
    min_t.undo()
    sec_t.undo()
    
    h_, m_, s_ = formt(h, m, s)
    t.undo()
    write_time(h_, m_, s_)
    
    #get the hands angles
    agl_h, agl_m, agl_s = angle(h_, m_, s_)

    #draw the hands
    draw(agl_h, agl_m, agl_s)

    wn.update()
    
    seconde +=1

    #wn.ontimer(refresh, 1000)

for _ in iter(int, 1):
    refresh(s=seconde)
    time.sleep(1)

wn.exitonclick()

#wn.mainloop()
