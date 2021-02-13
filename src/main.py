# This Python file is game of star war using turtle lib

####################################################
# Fist part: defining the window and players structs

import turtle
import math
import random

window = turtle.Screen()
window.setup(width=600, height=600)
window.title('Star Wars Game Created by Geziel Elyon')
window.bgcolor('#282a36')

window.tracer(0)

vertex = ((0, 15), (-15, 0), (-18, 5), (-18, -5),
          (0, 0), (18, -5), (18, 5), (15, 0))
window.register_shape('player', vertex)

asVertex = ((0, 10), (5, 7), (3, 3), (10, 0), (7, 4), (8, -6),
            (0, -10), (-5, -5), (-7, -7), (-10, 0), (-5, 4), (-1, 8))
window.register_shape('target', asVertex)

##################################
# Second part: creating the player


class BasicStruct(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)

        self.speed(0)
        self.penup()


def player1(position1, position2):
    xCordinate1 = position1.xcor()
    yCordinate1 = position1.ycor()

    xCordinate2 = position2.xcor()
    yCordinate2 = position2.ycor()

    cordinate = math.atan2(yCordinate1 - yCordinate2,
                           xCordinate1 - xCordinate2)
    cordinate = cordinate * 180.0 / 3.14159

    return cordinate


player = BasicStruct()
player.color('#0962ed')
player.shape('player')
player.score = 0

###################################
# Third part: creating the missiles

missiles = []
for _ in range(3):
    missile = BasicStruct()
    missile.color('#8be9fd')
    missile.shape('arrow')
    missile.speed = 1
    missile.state = 'ready'
    missile.hideturtle()
    missiles.append(missile)

pen = BasicStruct()
pen.color('white')
pen.hideturtle()
pen.goto(0, 250)
pen.write('Score: 0', False, align='center', font=('Arial', 24, 'bold'))

###################################
# Fourth part: creating the targets

targets = []
for _ in range(5):
    target = BasicStruct()
    target.color('#50fa7b')
    target.shape('arrow')

    target.speed = random.randint(2, 3)/50
    target.goto(0, 0)
    variation = random.randint(0, 260)
    distance = random.randint(300, 400)
    target.setheading(variation)
    target.fd(distance)
    target.setheading(player1(player, target))
    targets.append(target)

###################################
# Fifth part: creating defences functions


def turnLeft():
    player.lt(20)


def turnRight():
    player.rt(20)


def fire_missile():
    for missile in missiles:
        if missile.state == 'ready':
            missile.goto(0, 0)
            missile.showturtle()
            missile.setheading(player.heading())
            missile.state = "fire"
            break


window.listen()
window.onkey(turnLeft, 'Left')
window.onkey(turnRight, 'Right')
window.onkey(fire_missile, 'space')

###################################
# Sixth part: basic gamin functions

death = False
while True:

    window.update()
    player.goto(0, 0)

    for missile in missiles:
        if missile.state == "fire":
            missile.fd(missile.speed)

        if missile.xcor() > 300 or missile.xcor() < -300 or missile.ycor() > 300 or missile.ycor() < -300:
            missile.hideturtle()
            missile.state = "ready"

    for target in targets:
        target.fd(target.speed)

        for missile in missiles:
            if target.distance(missile) < 20:
                variation = random.randint(0, 260)
                distance = random.randint(600, 800)
                target.setheading(variation)
                target.fd(distance)
                target.setheading(player1(player, target))
                target.speed += 0.01

                missile.goto(600, 600)
                missile.hideturtle()
                missile.state = "ready"

                player.score += 10
                pen.clear()
                pen.write("Score: {}".format(player.score), False,
                          align="center", font=("Arial", 24, "bold"))

        if target.distance(player) < 20:
            taauko = random.randint(0, 260)
            distance = random.randint(600, 800)
            target.setheading(taauko)
            target.fd(distance)
            target.setheading(player1(player, target))
            target.speed += 0.005
            death = True
            player.score -= 30
            pen.clear()
            pen.write("Score: {}".format(player.score), False,
                      align="center", font=("Arial", 24, "bold"))
    if death == True:
        player.hideturtle()
        missile.hideturtle()
        for a in targets:
            a.hideturtle()
        pen.clear()
        break

window.mainloop()
