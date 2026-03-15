import turtle

GameScreen = turtle.Screen()
GameScreen.bgcolor("light blue")
style = ('Courier', 30, 'italic')

def countdown(time):
    GameScreen.onclick(None)  # disable click until countdown completes
    tospik.clear()

    if time > 0:
        tospik.write(time, align='center', font=style)
        GameScreen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        tospik.write("Click Screen", align='center', font=style)
        GameScreen.onclick(lambda x, y: countdown(30))



tospik = turtle.Turtle()
tospik.hideturtle()
tospik.write("Click Screen", align='center', font=style)
GameScreen.onclick(lambda x, y: countdown(30))



GameScreen.mainloop()

