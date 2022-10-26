import sys
import turtle
from turtle import Turtle, Screen
from random import randint

#List to hold colors and initialized turtle list
colors = ['green', 'red', 'orange', 'yellow', 'blue', 'purple']

# Method that will assign a color and relocate each turtle to the starting line
def startYourEngines(turtleList):
    i = 0
    x = -240
    y = -180
    for turtle in turtleList:
        turtle.penup()
        turtle.color(colors[i])
        turtle.goto(x, y)
        turtle.speed(2)
        turtle.name = str(colors[i])
        y += 74
        i += 1

# Method to create a start and finish line
def drawingLines():
    line = Turtle()
    line.hideturtle()
    line.speed(10)
    x = -220
    for i in range(2):
        line.penup()
        line.goto(x, 250)
        line.down()
        line.goto(x, -250)
        line.penup()
        x += 440

#Method will move the racers forward by a random amount
def letsRace(turtleList):
    for turtle in turtleList:
        randomDistance = randint(0, 10)
        turtle.forward(randomDistance)

#Method will check to see if a turtle has crossed the finish line
def crossFinish(userBet, turtleList):
    isRaceOn = True
    for turtle in turtleList:
        if turtle.xcor() > 230:
            print(f"The {turtle.name} turtle has won!")
            winningColor = turtle.name
            if winningColor == userBet:
                print("You've Won!")
            else:
                print("You've Lost")
            isRaceOn = False
            return isRaceOn
    return isRaceOn


#Main program function
def race():
    #Create instance of list of turtles
    turtle.TurtleScreen._RUNNING=True
    turtleList = []

    # Create the screen
    screen = Screen()
    screen.setup(width=500, height=400)

    # Create the turtles
    for turtleIndex in range(0, 6):
        newTurtle = Turtle(shape='turtle')
        newTurtle.penup()
        turtleList.append(newTurtle)

    #Grabs the users bet and starts the race
    userBet = screen.textinput("Make Your Bets!", "Which turtle will win the race? Enter a color.").lower()
    if userBet != '' or userBet == '':
        isRaceOn = True
        startYourEngines(turtleList)
        drawingLines()

    while isRaceOn == True:
        letsRace(turtleList)
        isRaceOn = crossFinish(userBet,turtleList)

    screen.exitonclick()
    # Take user input, restart game
    play = input("Do you want to play again? 'y' or 'n'").lower()
    if play == 'y':
        race()
    else:
        sys.exit("Thank you for playing")

#Start the program
race()



