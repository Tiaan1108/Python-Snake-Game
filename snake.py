
import turtle
import random

h = [0] #set direction
a = [0];b = [0] #set score
fcoord = [0,0,0] #food coord
pos = [] #set position

def main_game(x,y):
    x = 0
    y = 0
    a[0] = 0
    b[0] = 0
    h[0] = 0
    fcoord[2] = 0
    pos[:] = []
    turtle.hideturtle()
    turtle.clear()
    turtle.pu()
    turtle.color("black")
    turtle.goto(-30,0)
    turtle.write("Play",font=("Verdana", 34, "bold"))
    turtle.title("Snake Game")
    turtle.onscreenclick(start)

def game_edge():
    turtle.clear()
    turtle.pu()
    turtle.speed(0)
    turtle.pensize(20)
    turtle.color("grey")
    turtle.goto(-220,220)
    turtle.pd()
    turtle.goto(220,220)
    turtle.goto(220,-220)
    turtle.goto(-220,-220)
    turtle.goto(-220,220)
    turtle.pu()
    turtle.goto(0,0)

def start(x,y):
    turtle.onscreenclick(None)

    game_edge()

    tfood = turtle.Turtle()
    tfood.hideturtle()
    tfood.pu()
    tfood.speed(0)
    tfood.shape("square")
    tfood.color("red")

    g_score = turtle.Turtle()
    g_score.hideturtle()
    g_score.pu()
    g_score.speed(0)
    g_score.goto(100,-250)
    g_score.write("Score:" + str(a[0]), align="center",font=("Arial", 14, "normal"))
    
    while x > -210 and x < 210 and y > -210 and y <210:
        if fcoord[2] == 0:
            food(tfood)
            fcoord[2] = 1
        turtle.onkey(u,"Up")
        turtle.onkey(l,"Left")
        turtle.onkey(r,"Right")
        turtle.onkey(d,"Down")
        turtle.listen()
        move()
        x = turtle.xcor()
        y = turtle.ycor()        
        if x > fcoord[0]*20-5 and x < fcoord[0]*20+5 and y > fcoord[1]*20-5 and y < fcoord[1]*20+5:
            fcoord[2] = 0
            tfood.clear()
            a[0] += 1
            g_score.clear()
            g_score.write("Score:" + str(a[0]), align="center",font=("Arial", 14, "normal"))
        
        if len(pos) > 1:
            for i in range(1,len(pos)):
                if x < pos[i][0]+5 and x > pos[i][0]-5 and y < pos[i][1]+5 and y > pos[i][1]-5:
                        g_score.clear()
                        tfood.clear()
                        gameover()
                        return
    g_score.clear()
    tfood.clear()
    gameover()

def food(tfood):
    x = random.randrange(-8,8,1)
    y = random.randrange(-8,8,1)
    fcoord[0] = x
    fcoord[1] = y
    tfood.hideturtle()
    tfood.pu()
    tfood.shape("square")
    tfood.color("red")
    tfood.goto(x*20,y*20)
    tfood.stamp()

#Up   
def u():
    if h[0] == 270:
        pass
    else:
        h[0] = 90
#Down
def d():
    if h[0] == 90:
        pass
    else:
        h[0] = 270
#Left
def l():
    if h[0] == 0:
        pass
    else:
        h[0] = 180
#Right
def r():
    if h[0] == 180:
        pass
    else:
        h[0] = 0

def move():
    turtle.pensize(1)
    turtle.color("black")
    turtle.pu()
    turtle.speed(4)
    turtle.setheading(h[0])
    turtle.shape("square")
    turtle.stamp()
    turtle.fd(20)
    x = turtle.xcor()
    y = turtle.ycor()
    if b[0] > a[0]:     
        turtle.clearstamps(1)
        pos.insert(0,[round(x),round(y)])
        pos.pop(-1)
    else:
        pos.insert(0,[round(x),round(y)])       
        b[0] += 1    
    
def gameover():
    turtle.onscreenclick(None)
    turtle.speed(0)
    turtle.pu()
    turtle.goto(0,150)
    turtle.color("red")
    turtle.write("Game Over",align="center", font=("Arial", 14, "normal"))
    turtle.goto(0,50)
    turtle.write("Score:" + str(a[0]),align="center",font=("Arial", 14, "normal"))
    turtle.goto(220,-270)
    turtle.write("(Click anywhere to return to the main menu)",align="right",font=("Arial", 10, "normal"))
    turtle.onscreenclick(main_game)
    
# Start the game.
if __name__ == '__main__':
    main_game(0,0)
    turtle.mainloop()
