from turtle import Screen, Turtle
from tkinter import *
import turtle
import winsound
import time
import random
root=Tk()
v1=IntVar()
v2=IntVar()

is_single=True
is_double=False
is_paused=False
ball_entry=True
flag=0
flag1=0
count=0
probability=.1


def single():
    global is_single
    global is_double
    is_single=True
    is_double=False

    easy_level=Radiobutton(root,font=('corbel',15,'italic'),text="Easy",variable=v2,value=4,command=lambda : easy())
    easy_level.place(relx=.2,rely=.6)

    medium_level=Radiobutton(root,font=('corbel',15,'italic'),text="Medium",variable=v2,value=3,command=lambda : medium())
    medium_level.place(relx=.43,rely=.6)

    hard_level=Radiobutton(root,font=('corbel',15,'italic'),text="Hard",variable=v2,value=5,command=lambda : hard())
    hard_level.place(relx=.69,rely=.6)

def double():
    global is_double
    global is_single
    is_double=True
    is_single=False

def easy():
    global probability
    probability=.3

def medium():
    global probability
    probability=.1

def hard():
    global probability
    probability=.05

def destroyer():
    global flag,v1,v2 
    flag=1
    v1.set(None)
    v2.set(None)
    #root.destroy()
    game()

def pause():
    global is_paused
    if is_paused == True:
        is_paused = False
    else:
        is_paused = True

def bye():
    exit(0)

def menu():

    root.title("PONG GAME")
    root.resizable(False,False)

    window_height = 600
    window_width = 800

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")
    root.configure(bg="black")


    heading=Label(root,text="Pong Game",font=('verdana',15,'bold'),bg='white',fg="indigo").pack(fill=BOTH)
    instructions=Label(root,font=('Times New Roman',15,'normal'),text="\n=> The one who scores 3 points first wins the game\n=> Player A : 'q' for up  'a' for down\n=>Player B : 'Arrow up' for up  'Arrow down' for down\n=>Press 's' and 'd' for switching to single and double player mode respectively during the game\n=>Click on the mode below and have fun\n=>Press 'p' to pause or continue the game",bg='black',fg='white').pack(fill=BOTH)

    singleplayer=Radiobutton(root,font=('corbel',15,'italic'),text="Single Player",variable=v1,value=2,command = lambda : single())
    singleplayer.place(relx=.2,rely=.45)

    doubleplayer=Radiobutton(root,font=('corbel',15,'italic'),text="Double Player",variable=v1,value=1,command = lambda : double())
    doubleplayer.place(relx=.6,rely=.45)

    playy=Button(root,text='PLAY',font=('verdana',13,'bold'),bd='5',command=lambda : destroyer())
    playy.place(relx=.2,rely=.75)

    exitt=Button(root,text='EXIT',font=('verdana',13,'bold'),bd='5',command=lambda : bye())
    exitt.place(relx=.69,rely=.75)

    root.mainloop()

def game():
    global flag1,flag2,count,probability,ball_entry
    print(probability)
    wn=turtle.Screen()
    turtle.TurtleScreen._RUNNING=True
    wn.title("PONG GAME")
    wn._bgcolor("black")
    wn.setup(width=800,height=600)
    wn.tracer(0)

    
    #Score
    points_a=0
    points_b=0


    #Paddle A
    paddle_a=Turtle()
    paddle_a.speed(0)
    paddle_a.shape("square")
    paddle_a.color("white")
    paddle_a.shapesize(stretch_wid=5,stretch_len=1) #default the size of any share is 20 pix by 20px,,so thats gonna be 20*5=100 pics
    paddle_a.penup()
    paddle_a.goto(-350,0)


    #Paddle B
    paddle_b=Turtle()
    paddle_b.speed(0)
    paddle_b.shape("square")
    paddle_b.color("white")
    paddle_b.shapesize(stretch_wid=5,stretch_len=1) #default the size of any share is 20 pix by 20px,,so thats gonna be 20*5=100 pics
    paddle_b.penup()
    paddle_b.goto(350,0)


    #Ball
    ball1=Turtle()
    ball1.speed(0)
    ball1.shape("square")
    ball1.color("white")
    ball1.penup()
    ball1.goto(0,0)
    ball1.dx=+0.15
    ball1.dy=-0.15

    ball2=Turtle()
    ball2.speed(0)
    ball2.shape("square")
    ball2.color("blue")
    ball2.penup()
    ball2.goto(0,0)
    ball2.dx=+0.15
    ball2.dy=-0.15
    ball2.hideturtle()
    
    balls=[ball1,ball2]

    #turtles
    pen=Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0,260)
    pen.write("Player A : 0   Player B : 0",align="center",font=("Courier",24,"normal"))

    line=Turtle()
    line.color("white")
    line.penup()
    line.goto(-400,250)
    line.pendown()
    line.forward(800)
    line.hideturtle()

    pen1=Turtle()
    pen1.color("white")
    #pen.penup()
    pen1.hideturtle()

    winsound.PlaySound("coundown_pong_sound.wav", winsound.SND_ASYNC)
    for second in range(3,0,-1):
        pen1.clear()
        pen1.write(second,align="center",font=(None,100))
        if second>1:
            time.sleep(.7)
        else:
            time.sleep(.4)

    pen1.clear()
    pen1.write("PLAY!!",align="center",font=(None,60))
    time.sleep(.7)
    pen1.clear()

    #Movement of paddles
    def paddle_a_up():
        y=paddle_a.ycor()
        y+=20
        paddle_a.sety(y)
        if y>200:
            paddle_a.sety(200)

    def paddle_a_down():
        y=paddle_a.ycor()
        y-=20
        paddle_a.sety(y)
        if y<-250:
            paddle_a.sety(-250)

    def paddle_b_up():
        y=paddle_b.ycor()
        y+=20
        paddle_b.sety(y)
        if y>200:
            paddle_b.sety(200)

    def paddle_b_down():
        y=paddle_b.ycor()
        y-=20
        paddle_b.sety(y)
        if y<-250:
            paddle_b.sety(-250)

    #Input through keyboard

    wn.listen()
    wn.onkeypress(paddle_a_up,"q")
    wn.onkeypress(paddle_a_down,"a")
    wn.onkeypress(paddle_b_up,"Up")
    wn.onkeypress(paddle_b_down,"Down")
    wn.onkeypress(single,"s")
    wn.onkeypress(double,"d")
    wn.onkeypress(pause,"p")
    


    while True:
        wn.update()
        if not is_paused:
            if flag==1:

                if points_a==3:
                    pen.goto(0,200)
                    pen.write("Player A wins!!",align="center",font=("Arial",20,"bold"))
                    pen.goto(0,-40)
                    pen.write("GAME OVER",align="center",font=("courier",15,"normal"))
                    pen.goto(0,-65)
                    pen.write("Click on the screen!",align="center",font=("courier",15,"italic"))
                    winsound.PlaySound("Pong_game_over.wav", winsound.SND_ASYNC)
                    time.sleep(5)
                    turtle.exitonclick()
                    menu()      

                elif points_b==3:
                    pen.goto(0,200)
                    pen.write("Player B wins!!",align="center",font=("Arial",20,"bold"))
                    pen.goto(0,-40)
                    pen.write("GAME OVER",align="center",font=("courier",15,"normal"))
                    pen.goto(0,-65)
                    pen.write("Click on the screen!",align="center",font=("courier",15,"italic"))
                    winsound.PlaySound("Pong_game_over.wav", winsound.SND_ASYNC)
                    time.sleep(5)
                    turtle.exitonclick()
                    menu()      

                for ball in balls:    
                    #Move the ball
                    if ball==ball1:
                        ball1.setx(ball1.xcor() + ball1.dx)
                        ball1.sety(ball1.ycor() + ball1.dy)
                    
                    if (count>25 and probability==0.3) or (count>15 and probability==0.1) or (count>10 and probability==0.05):
                        if ball==ball2:
                            ball2.showturtle()
                            if ball_entry==True:
                                winsound.PlaySound("second_ball.wav", winsound.SND_ASYNC)
                                ball_entry=False
                            ball2.setx(ball2.xcor() + ball2.dx)
                            ball2.sety(ball2.ycor() + ball2.dy)
                        
                        
                    #Border Checking
                    if ball.ycor() > 240:
                        ball.sety(240)
                        ball.dy *= -1
                        winsound.PlaySound("Bounce.wav", winsound.SND_ASYNC)

                    if ball.ycor() < -290:
                        ball.sety(-290)
                        ball.dy *= -1
                        winsound.PlaySound("Bounce.wav", winsound.SND_ASYNC)

                    if ball.xcor() > 390:
                        ball1.goto(0,0)
                        ball2.goto(0,0)
                        ball2.hideturtle()
                        ball_entry=True
                        ball.dx *= -1
                        points_a+=1
                        pen.clear()
                        pen.write(f"Player A : {points_a}   Player B : {points_b}",align="center",font=("Courier",24,"normal"))
                        winsound.PlaySound("Points_sound.wav", winsound.SND_ASYNC)
                        ball.dx=0.15
                        ball.dy=-0.15
                        time.sleep(0.8)
                        flag1=count=0

                    if ball.xcor() < -390: 
                        ball1.goto(0,0)
                        ball2.goto(0,0)
                        ball2.hideturtle()
                        ball_entry=True
                        ball.dx *= -1
                        points_b+=1
                        pen.clear()
                        pen.write(f"Player A : {points_a}   Player B : {points_b}",align="center",font=("Courier",24,"normal"))
                        winsound.PlaySound("Points_sound.wav", winsound.SND_ASYNC)
                        ball.dx=0.15
                        ball.dy=-0.15
                        time.sleep(0.8)
                        flag1=count=0

                    
                    #Collissions
                    if (ball.xcor() > 340 and ball.ycor() <350) and (ball.ycor() < paddle_b.ycor() +40 and ball.ycor() > paddle_b.ycor() -40):
                        ball.setx(340)
                        ball.dx*= -1
                        ball.dx-=0.02
                        ball.dy-=0.02
                        count+=1
                        winsound.PlaySound("Bounce.wav", winsound.SND_ASYNC)
                        
                        if count>3 and is_single==True:
                            random_num=random.random()
                            print(random_num)
                            if random_num<probability:
                                flag1=1
                            else:
                                flag1=0
                        
                
                    if (ball.xcor() < -340 and ball.ycor() >-350) and (ball.ycor() < paddle_a.ycor() +40 and ball.ycor() > paddle_a.ycor() -40):
                        ball.setx(-340)
                        ball.dx*= -1
                        ball.dx-=0.02
                        ball.dy-=0.02
                        count+=1
                        winsound.PlaySound("Bounce.wav", winsound.SND_ASYNC)

                    #Single Player
                    
                    if is_single==True:
                        closest_ball=balls[0]
                        for ball in balls:
                            if ball.xcor()>closest_ball.xcor():
                                closest_ball=ball
                        
                        if closest_ball.xcor()>0 and closest_ball.dx>0:
                            if flag1==1:
                                paddle_b.sety(closest_ball.ycor()-60)
                                if closest_ball.ycor()<-250:
                                    paddle_b.sety(closest_ball.ycor()-60)
                                #else:
                                    #paddle_b.sety(closest_ball.ycor()+60)
                            elif flag1==0:
                                paddle_b.sety(closest_ball.ycor())
                            if closest_ball.ycor()>200:
                                paddle_b.sety(200)
                            if closest_ball.ycor()<-250:
                                paddle_b.sety(-250)
        
menu()
