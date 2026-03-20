import turtle
wind=turtle.Screen()
wind.title("Fire Robot")
wind.bgcolor("black")
wind.setup(width=800,height=600)
wind.tracer(0)

sword1=turtle.Turtle()
sword1.speed(0)
sword1.shape("square")
sword1.color("blue")
sword1.shapesize(stretch_wid=5,stretch_len=1)
sword1.penup()
sword1.goto(-350,0)

sword2=turtle.Turtle()
sword2.speed(0)
sword2.shape("square")
sword2.color("red")
sword2.shapesize(stretch_wid=5,stretch_len=1)
sword2.penup()
sword2.goto(350,0)

stone=turtle.Turtle()
stone.speed(0)
stone.shape("square")
stone.color("white")
stone.penup()
stone.goto(0,0)
stone.dx=0.1
stone.dy=-0.1

score1=0
score2=0
score=turtle.Turtle()
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Player 1:0 Player 2:0",align="center",font=("Cousier",24,"normal"))

def sword1_up():
    y=sword1.ycor()
    y +=20
    sword1.sety(y)

def sword1_down():
    y=sword1.ycor()
    y -=20
    sword1.sety(y)

def sword2_up():
    y=sword2.ycor()
    y +=20
    sword2.sety(y)

def sword2_down():
    y=sword2.ycor()
    y -=20
    sword2.sety(y)

wind.listen()
wind.onkeypress(sword1_up,"w")
wind.onkeypress(sword1_down,"s")
wind.onkeypress(sword2_up,"Up")
wind.onkeypress(sword2_down,"Down")


while True:
    wind.update()

    stone.setx(stone.xcor() + stone.dx)
    stone.sety(stone.ycor() + stone.dy)

    if stone.ycor()>290:
        stone.sety(290)
        stone.dy *=-1
    
    if stone.ycor()<-290:
        stone.sety(-290)
        stone.dy *=-1
    
    if stone.xcor()>390:
        stone.goto(0,0)
        stone.dx *=-1
        score1 +=1
        score.clear()
        score.write("Player 1:{} Player 2:{}".format(score1,score2),align="center",font=("Cousier",24,"normal"))
    if score1 ==10:
        score1=0
        score.clear()
        score.write("Player 1 is win",align="center",font=("Cousier",24,"normal"))
    
    if stone.xcor()<-390:
        stone.goto(0,0)
        stone.dx *=-1
        score2+=1
        score.clear()
        score.write("Player 1:{} Player 2:{}".format(score1,score2),align="center",font=("Cousier",24,"normal"))
    if score2 ==10:
        score2=0
        score.clear()
        score.write("Player 2 is win",align="center",font=("Cousier",24,"normal"))

    if (stone.xcor()>340 and stone.xcor()<350 and (stone.ycor()<sword2.ycor() +40 and stone.ycor()>sword2.ycor()-40)):
        stone.setx(340)
        stone.dx *=-1
    
    if (stone.xcor()<-340 and stone.xcor()>-350 and (stone.ycor()<sword1.ycor() +40 and stone.ycor()>sword1.ycor()-40)):
        stone.setx(-340)
        stone.dx *=-1
    
    
    