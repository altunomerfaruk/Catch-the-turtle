import turtle
from tkinter import PhotoImage
from turtle import Turtle, Screen, Shape
from random import randint

GameScreen = turtle.Screen()
GameScreen.bgcolor("light blue")
style = ('Courier', 30, 'italic')
skor = 0


def start_game(x, y):
    global skor
    skor = 0

    tospik2.clear()
    tospik2.write(f"Skor: {skor}", align='center', font=style)

    countdown(30)

def click_tortoise(x, y):
    global skor
    skor += 1

    tortoise.setposition(randint(-200, 200),randint(-200, 200))
    tospik2.clear()
    tospik2.write(f"Skor: {skor}", align='center', font=style)


def countdown(time):
    tospik.clear()
    if time > 0:
        GameScreen.onclick(None)
        tospik.write(f"Time: {time}", align='center', font=style)
        GameScreen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        global skor
        tospik.write("Click Screen", align='center', font=style)
        GameScreen.onclick(lambda x, y: start_game(x, y))


tospik = turtle.Turtle()
tospik.hideturtle()
tospik.penup()
tospik.speed(0)
top_height = GameScreen.window_height() / 2
tospik.setposition(0, top_height - top_height / 10)

tospik2 = turtle.Turtle()
tospik2.hideturtle()
tospik2.penup()
tospik2.speed(0)
tospik2.setposition(0, top_height - top_height / 5)
tospik2.write(f"Skor: {skor}", align='center', font=style)

try:
    larger = PhotoImage(file="erase.gif").subsample(6, 6)
    GameScreen.addshape("larger", Shape("image", larger))
    tortoise = Turtle("larger")
except Exception as e:
    print("There is no erase.gif")
    tortoise = Turtle("turtle")

tortoise.penup()
tortoise.speed(0)
tortoise.onclick(click_tortoise)


tospik.write("Click Screen", align='center', font=style)


GameScreen.onclick(lambda x, y: countdown(30))

GameScreen.mainloop()