import turtle

GameScreen = turtle.Screen()
GameScreen.bgcolor("light blue")
style = ('Courier', 30, 'italic')
skor = 0
def countdown(time):
    GameScreen.onclick(None)  # disable click until countdown completes
    tospik.clear()

    if time > 0:
        tospik.write( f"Time:{time}" , align='center', font=style)
        GameScreen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        tospik.write("Click Screen", align='center', font=style)
        GameScreen.onclick(lambda x, y: countdown(30))

tospik = turtle.Turtle()
tospik.hideturtle()
tospik.penup()
tospik.speed(0)
top_height = GameScreen.window_height()/2
tospik.setposition(0, top_height - top_height/10)
tospik2 = turtle.Turtle()
tospik2.hideturtle()
tospik2.penup()
tospik2.speed(0)
tospik2.setposition(0, top_height - top_height/5)
tospik2.write(f"Skor: {skor}", align='center', font=style)





tospik.write("Click Screen", align='center', font=style)
GameScreen.onclick(lambda x, y: countdown(30))



GameScreen.mainloop()

