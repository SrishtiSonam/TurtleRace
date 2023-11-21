import random
import turtle
import math

#       -------------           Screen set up
myscreen = turtle.Screen()
myscreen.bgcolor('light yellow')
myscreen.setup(1.0, 1.0)
myscreen.title('Turtle Race Game')


#       -------------           Setting up relay race-track
def setUpTrack(startx, starty, startdeg, movex, movey, endx, endy, enddeg, slidex, slidey, finishmove, finishdeg):
    pen = turtle.Turtle()
    pen.speed(0)
    pen.penup()
    pen.goto(startx, starty)
    pen.left(startdeg)
    pen.pendown()
    pen.goto(startx+movex, starty+movey)
    pen.up()
    pen.goto(endx, endy)
    pen.right(enddeg)
    pen.pendown()
    pen.goto(endx+slidex, endy+slidey)
    pen.up()
    pen.left(finishdeg)
    pen.forward(finishmove)
    pen.write(" FINISH", font=('Times New Roman', 14, 'normal'))
    pen.hideturtle()
    return pen


def createTurtlePlayer(color, startx, starty, deg):
    player = turtle.Turtle()
    player.shape("turtle")
    player.color(color)
    player.penup()
    player.goto(startx, starty)
    player.pendown()
    player.left(deg)
    return player


def raceSetUp():
    p1 = createTurtlePlayer('red', -560, -280, 90,)
    p2 = createTurtlePlayer('blue', -500, -280, 90)
    l1 = setUpTrack(-530, -300, 90, 0, 500, -600, +150, 0, 140, 0, 0, 0)
    writeName(-570, -325,16, 'First Race')
    p3 = createTurtlePlayer('red', -400, +240, 0)
    p4 = createTurtlePlayer('blue', -400, +300, 0)
    l2 = setUpTrack(-430, +270, 0, 800, 0, +310, +330, 90, 0, -120, 20, 0)
    writeName(-550, +260, 16, 'Second Race')
    p5 = createTurtlePlayer('red', +560, +200, 270)
    p6 = createTurtlePlayer('blue', +500, +200, 270)
    l3 = setUpTrack(+530, +220, 270, 0, -500, 600, -250, 180, -140, 0, 70, 90)
    writeName(490, 230, 16, 'Third Race')


#       -------------------------         Class Turtle

class TurtlePlayer:

    win1 = 0
    win2 = 0
    win3 = 0

    def __init__(self):
        self.player = turtle.Turtle()
        self.player.shape("turtle")
        self.flag1 = 0
        self.flag2 = 0
        self.flag3 = 0
        self.finishFirst = 150
        self.finishSecond = 310
        self.finishThird = -250
        self.color = ''

    def createPlayer(self, color, startx, starty, deg):
        self.color = color
        self.player.color(color)
        self.player.penup()
        self.player.goto(startx, starty)
        self.player.pendown()
        self.player.left(deg)
        return self.player

    def moveForward(self, steps):
        if self.flag1 == 0:
            space = self.finishFirst - self.player.pos()[1]
            if steps <= space:
                self.player.forward(steps)
            else:
                self.player.forward(space)
                self.flag1 = 1
                if TurtlePlayer.win1 == 0:
                    writeName(-600, 180,16,  self.color+' Won the first race')
                    TurtlePlayer.win1 = 1
                self.player.penup()
                if self.color == 'red':
                    self.player.goto(-400, 240)
                elif self.color == 'blue':
                    self.player.goto(-400, 300)
                self.player.pendown()
                self.player.right(90)

        elif self.flag1 == 1 and self.flag2 == 0:
            space = self.finishSecond - self.player.pos()[0]
            print("In second race")
            print("position: ", self.player.pos()[1], " steps to take ", steps, "space", space)
            print("\n ")
            if steps <= space:
                self.player.forward(steps)
            else:
                self.player.forward(space)
                self.flag2 = 1
                if TurtlePlayer.win2 == 0:
                    writeName(400, 260, 16, self.color+' Won the second race')
                    TurtlePlayer.win2 = 1
                self.player.penup()
                if self.color == 'red':
                    self.player.goto(560, 200)
                elif self.color == 'blue':
                    self.player.goto(500, 200)
                self.player.pendown()
                self.player.right(90)

        elif self.flag1 == 1 and self.flag2 == 1 and self.flag3 == 0:
            space = self.player.pos()[1] - self.finishThird
            print("In third race")
            print("position: ", self.player.pos()[1], " steps to take ", steps, "space", space)
            print("\n ")
            if steps <= space:
                self.player.forward(steps)
            else:
                self.player.forward(space)
                self.flag3 = 1
                if TurtlePlayer.win3 == 0:
                    writeName(-120, -240, 18, self.color + ' team, Won the race !!!')
                    TurtlePlayer.win3 = 1


#       --------------      Dice roll Setup
def createBox(x1, x2, y1, y2):
    box = turtle.Turtle()
    box.penup()
    box.begin_fill()
    box.goto(x1, y1)
    box.pendown()
    box.goto(x1, y2)
    box.right(90)
    box.goto(x2, y2)
    box.right(90)
    box.goto(x2, y1)
    box.right(90)
    box.goto(x1, y1)
    box.hideturtle()


def turtlePip(x, y):
    pip = turtle.Turtle()
    pip.shape("turtle")
    pip.penup()
    pip.goto(x, y)
    pip.left(90)
    return pip


def turtlesBox():
    createBox(-252, 252, 100, 50)
    t1 = turtlePip(-180, 75)
    t2 = turtlePip(-108, 75)
    t3 = turtlePip(-36, 75)
    t4 = turtlePip(36, 75)
    t5 = turtlePip(108, 75)
    t6 = turtlePip(180, 75)
    return t1, t2, t3, t4, t5, t6


def writeName(x, y, size, name):
    pen = turtle.Turtle()
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.write(name, font=('Times New Roman', size, 'normal'))
    pen.hideturtle()
    return pen


def diceBox():
    createBox(-52, 52, 50, -150)
    p = writeName(-20, 10, 14, 'Roll')
    p = writeName(-15, -15, 14, 'the')
    p = writeName(-25, -40, 14, 'Dice!!!')
    createBox(-30, 30, -120, -60)


def playerBox():
    createBox(-252, -52, 50, -150)
    createBox(52, 252, 50, -150)
    p1 = writeName(-180, 10, 14, 'Player 1')
    p2 = writeName(124, 10, 14, 'Player 2')


def pipMoveForRed(c, p1, p2, p3, p4, p5, p6):

    def p1move():
        p1.goto(-152, -70)

    def p2move():
        p2.goto(-102, -70)

    def p3move():
        p3.goto(-202, -70)

    def p4move():
        p4.goto(-152, -110)

    def p5move():
        p5.goto(-102, -110)

    def p6move():
        p6.goto(-202, -110)

    if c == 1:
        p1move()
    elif c == 2:
        p1move()
        p2move()
    elif c == 3:
        p1move()
        p2move()
        p3move()
    elif c == 4:
        p1move()
        p2move()
        p3move()
        p4move()
    elif c == 5:
        p1move()
        p2move()
        p3move()
        p4move()
        p5move()
    elif c == 6:
        p1move()
        p2move()
        p3move()
        p4move()
        p5move()
        p6move()


def pipMoveForBlue(c, p1, p2, p3, p4, p5, p6):
    def p1move():
        p1.goto(152, -70)

    def p2move():
        p2.goto(102, -70)

    def p3move():
        p3.goto(202, -70)

    def p4move():
        p4.goto(152, -110)

    def p5move():
        p5.goto(102, -110)

    def p6move():
        p6.goto(202, -110)

    if c == 1:
        p1move()
    elif c == 2:
        p1move()
        p2move()
    elif c == 3:
        p1move()
        p2move()
        p3move()
    elif c == 4:
        p1move()
        p2move()
        p3move()
        p4move()
    elif c == 5:
        p1move()
        p2move()
        p3move()
        p4move()
        p5move()
    elif c == 6:
        p1move()
        p2move()
        p3move()
        p4move()
        p5move()
        p6move()


def goBackPip(p1, p2, p3, p4, p5, p6):
    p1.goto(-180, 75)
    p2.goto(-108, 75)
    p3.goto(-36, 75)
    p4.goto(36, 75)
    p5.goto(108, 75)
    p6.goto(180, 75)


#       --------------      Creating participating turtles
raceSetUp()
redPlayer = TurtlePlayer()
bluePlayer = TurtlePlayer()
firstPlayer = redPlayer.createPlayer('red', -560, -280, 90)
secondPlayer = bluePlayer.createPlayer('blue', -500, -280, 90)
diceBox()
playerBox()
writeName(-160, -200, 20, 'Speedy Shell Relay Tournament')
pip1, pip2, pip3, pip4, pip5, pip6 = turtlesBox()
pointer = turtle.Turtle()
pointer.left(90)
pointer.penup()

t = 0
while TurtlePlayer.win3 == 0:
    count = math.ceil((random.random())*6)
    if t % 2 == 0:
        pointer.goto(-150, 5)
        rollCount = writeName(-5, -107, 20, count)
        pipMoveForRed(count, pip1, pip2, pip3, pip4, pip5, pip6)
        redPlayer.moveForward(count*30)
    else:
        pointer.goto(150, 5)
        rollCount = writeName(-5, -107, 20, count)
        pipMoveForBlue(count, pip1, pip2, pip3, pip4, pip5, pip6)
        bluePlayer.moveForward(count*30)
    goBackPip(pip1, pip2, pip3, pip4, pip5, pip6)
    goBackPip(pip1, pip2, pip3, pip4, pip5, pip6)
    rollCount.clear()
    t = t + 1

turtle.done()

