try:  # import as appropriate for 2.x vs. 3.x
   import tkinter as tk
except:
   import Tkinter as tk
import turtle

PREVIEW_WINDOW_SIZE = (600, 600)
PREVIEW_WINDOW_TITLE = 'Drawbot Preview'


def preview_drawing(lines, speed=5, draw_movement=False, animation=True):
    # Setup screen
    screen = turtle.Screen()
    screen.setup(*PREVIEW_WINDOW_SIZE)
    screen.title(PREVIEW_WINDOW_TITLE)
    screen.setworldcoordinates(0, 1, 1, 0)
    if not animation:
        screen.tracer(False)

    # Setup cursor
    cursor = turtle.Turtle()

    # Move to initial position
    cursor.speed(0)
    cursor.right(90)
    cursor.penup()
    cursor.goto(0, 0)

    cursor.pendown()
    cursor.speed(speed)

    if draw_movement:
        cursor.pencolor('red')

    # Draw each line
    for line in lines:
        cursor.goto(line[0].x, line[0].y)

        if draw_movement:
            cursor.pencolor('black')
        else:
            cursor.pendown()

        for i in range(1, len(line)):
            cursor.goto(line[i].x, line[i].y)
        
        if draw_movement:
            cursor.pencolor('red')
        else:
            cursor.penup()
        
    turtle.mainloop()
