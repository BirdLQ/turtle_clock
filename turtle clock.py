# -*- coding: utf-8 -*-
"""
@author: BirdLQ
"""

from turtle import *

# Function to move the turtle to a specific location without drawing a line
def jump(distance, angle=0):
    penup()  # Lift the pen
    right(angle)  # Rotate right by 'angle' degrees
    forward(distance)  # Move forward by 'distance' units
    left(angle)  # Rotate left to restore the original heading
    pendown()  # Put the pen down

# Function to draw a hand of the clock
def hand(length, tip):
    fd(length*1.15)  # Move forward
    rt(90)  # Rotate right
    fd(tip/2.0)  # Move forward
    lt(120)  # Rotate left
    fd(tip)  # Repeat this process to draw the hand
    lt(120)
    fd(tip)
    lt(120)
    fd(tip/2.0)

# Function to create a hand shape
def make_hand_shape(name, length, tip):
    reset()  # Clear the screen and bring the turtle to the center
    jump(-length*0.15)  # Move the turtle to the starting position
    begin_poly()  # Start recording the vertices of the polygon
    hand(length, tip)  # Draw the hand
    end_poly()  # Stop recording the vertices of the polygon
    hand_form = get_poly()  # Get the polygon
    register_shape(name, hand_form)  # Register the polygon shape with 'name'

# Function to draw the clock face
def clockface(radius):
    reset()  # Clear the screen and bring the turtle to the center
    for i in range(60):  # For each minute
        if i % 5 == 0:  # If it's an hour
            jump(radius)  # Move the turtle to the edge of the clock face
            pensize(7)  # Set the pen size
            fd(25)  # Draw a longer line
            jump(-radius-25)  # Move the turtle back to the center
        else:
            jump(radius+5)  # Move the turtle to the edge of the clock face
            pensize(1)  # Set the pen size
            fd(20)
            jump(-radius-25)  # Move the turtle back to the center
        rt(6)  # Rotate the turtle slightly to the right
    pensize(7)  # Set the pen size
    penup()
    home()
    right(90)  # Rotate right
    forward(radius+25)  # Move to home minus radius
    left(90)  # Rotate left to restore the original heading
    pendown()
    circle(radius+25)  # Draw the outer circle

# Function to setup the clock hands and the clock face
def setup():
    global second_hand, minute_hand, hour_hand, writer
    mode("logo")  # Set the mode to 'logo'
    make_hand_shape("second_hand", 140, 25)  # Create the second hand shape
    make_hand_shape("minute_hand",  125, 25)  # Create the minute hand shape
    make_hand_shape("hour_hand", 95, 25)  # Create the hour hand shape
    clockface(160)  # Draw the clock face
    second_hand = Turtle()  # Create the second hand turtle
    second_hand.shape("second_hand")  # Set the shape of the second hand
    second_hand.color("gray40", "gray90")  # Set the color of the second hand
    minute_hand = Turtle()  # Create the minute hand turtle
    minute_hand.shape("minute_hand")  # Set the shape of the minute hand
    minute_hand.color("cornflowerblue", "cyan")  # Set the color of the minute hand
    hour_hand = Turtle()  # Create the hour hand turtle
    hour_hand.shape("hour_hand")  # Set the shape of the hour hand
    hour_hand.color("blue3", "red3")  # Set the color of the hour hand
    for hand in second_hand, minute_hand, hour_hand:
        hand.resizemode("user")  # Allow the hand to be resized
        hand.shapesize(1, 1, 3)  # Set the size of the hand
        hand.speed(0)  # Set the speed of the hand
    ht()  # Hide the turtle
    writer = Turtle()  # Create a turtle for writing text
    writer.ht()  # Hide the writer turtle
    writer.pu()  # Lift the pen
    writer.bk(85)  # Move the writer turtle back

# Function to update the position of the hands
def tick():
    global second, minute, hour
    second += 1  # Increment the second
    if second >= 60:  # If a minute has passed
        second = 0  # Reset the second
        minute += 1  # Increment the minute
    minute += 1/60  # Increment the minute every second
    if minute >= 60:  # If an hour has passed
        minute = 0  # Reset the minute
        hour += 1  # Increment the hour
    hour += 1/3600  # Increment the hour every second
    if hour >= 24:  # If a day has passed
        hour = 0  # Reset the hour
    try:
        tracer(False)  # Turn off the animation
        writer.clear()  # Clear the writer turtle
        writer.home()  # Move the writer turtle to the center
        writer.forward(65)  # Move the writer turtle forward
        writer.back(150)  # Move the writer turtle back
        writer.forward(85)  # Move the writer turtle forward
        tracer(True)  # Turn on the animation
        second_hand.setheading(6*second)  # Set the heading of the second hand
        minute_hand.setheading(6*minute)  # Set the heading of the minute hand
        hour_hand.setheading(30*hour)  # Set the heading of the hour hand
        tracer(True)  # Turn on the animation
        ontimer(tick, 1000)  # Call the tick function again after 1 second
    except Terminator:
        pass  # If the turtle graphics window was closed, do nothing

def get_time_input(prompt):
    while True:
        try:
            time = int(input(prompt))
            return time
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    global second, minute, hour
    hour = get_time_input("Enter the hour : ")
    minute = get_time_input("Enter the minutes : ")
    second = get_time_input("Enter the seconds : ")
    
    tracer(False)
    setup()
    tracer(True)
    tick()
    return "EVENTLOOP"

if __name__ == "__main__":
    mode("logo")
    msg = main()
    print(msg)
    mainloop()
