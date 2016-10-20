####################################################### TAP #####################################################
######################################### PROGRAM CREATED BY: HUMZA FAHEEMUDDIN #################################
############################################ LAST MODIFIED: 2016-10-20 ##########################################

from Tkinter import*
from math import*
from random import*
import time

root = Tk()
root.title("TAP BY HUMZA FAHEEMUDDIN")
screen = Canvas( root, width = 800, height = 800, background = "WHITE")


## Global Variables that are used everywhere.
buttonX = 350 #Represents the X Coordinate of the Button
buttonY = 450 #Represents the Y Coordinate of the Button
curLevel = 0 #keeps track of what level you are on, which is displayed on the bottom of the screen
timeIncrement = 2 #Every level is this long
end = 0 #Keeps track of the current time
theEnder = end+timeIncrement # as long as end is less than this, the program will continue to register clicks
diffTwo = 10 #For future planned levels of difficulty, difficulty two will change the program.
increment = 100 #also for future planned levels of difficulty. stay tuned to see how this is used!


#---------------------------------------------------------------------------------------------------------------#
##draw() simply draws the text on the canvas, along with the buttons. If it is red, then you don't need to
## tap anymore. If it's black, keep tapping! Otherwise, it turns white (you went over, so you lose!)

def draw():
    global levelText, tapText, timerText, end, buttonBlack, buttonRed
    
    level = "Current level: " + str(curLevel)
    taps = "Number of Taps Left: " + str(numTaps)
    times = "{0:.2f}".format(end) + " seconds have passed."
    
    if (numTaps == 0):
        buttonRed = screen.create_oval(buttonX,buttonX, buttonY, buttonY, fill="red")
    elif (numTaps < 0):
        buttonBlue = screen.create_oval(buttonX,buttonX, buttonY, buttonY, fill="white")
    else:
        buttonBlack = screen.create_oval(buttonX, buttonX, buttonY, buttonY, fill = "black")
    levelText = screen.create_text(400, 700, text=level, font = "fixedsys 20", anchor=CENTER, fill = "black" )
    tapText = screen.create_text(400, 100, text=taps, font="fixedsys 20", anchor=CENTER, fill="black")
    timerText = screen.create_text(400, 20, text=times, font="fixedsys 20", fill="black")


#---------------------------------------------------------------------------------------------------------------#
## setup() initializes some variables, and calls draw() to draw the basic setup.
def setup():
    global curLevel, numTaps, buttonHit, buttonBlack


    buttonBlack = screen.create_oval(buttonX, buttonX, buttonY, buttonY, fill = "black")
    numTaps = 1
    curLevel = 0
    draw()
    buttonHit = False


#---------------------------------------------------------------------------------------------------------------#

## detects any clicking of the button
def mouseClickDetector(event):
    global xMouse, yMouse, numTaps, curLevel, end, start, buttonHit
    global hit
    #print ( "Mouse clicked at " + str( event.x ) + "," + str(event.y ))

    xMouse = event.x
    yMouse = event.y

    if xMouse >= buttonX and xMouse <= buttonY and yMouse >= buttonX and yMouse <= buttonY and curLevel == 0:
        buttonHit = True
        hit = True
        mainGame()
    elif xMouse >= buttonX and xMouse <= buttonY and yMouse >= buttonX and yMouse <= buttonY:
        buttonHit = True
        hit = True


#---------------------------------------------------------------------------------------------------------------#
        
## if the button was clicked, decreases the number of remaining taps. currently self-destructs at level 100.
def clicker():
    global numTaps, buttonHit, curLevel
    
    if (buttonHit == True):
        numTaps = numTaps - 1
        buttonHit = False
        screen.delete(levelText, tapText, timerText)
        draw()
        screen.update()
        
    if (curLevel == 100):
        root.destroy()


#---------------------------------------------------------------------------------------------------------------#

## is the key part of the game, updates the level if you're at the right number taps, and runs the while loop
## which tests out 
def mainGame():
    global end, theEnder, curLevel, numTaps

##    if (curLevel == diffTwo):
##        #print("Difficulty Two begins!")
##        screen.delete(buttonBlack, buttonRed)

    while (end < theEnder):
        clicker()
        #timeChange()
        screen.delete(levelText, tapText, timerText)
        end = time.clock()
        draw()
        screen.update()

    if (numTaps == 0):
        curLevel = curLevel + 1
        numTaps = randint(1, 6)
        theEnder += timeIncrement
        mainGame()
        
    elif ((numTaps > 0 or numTaps < 0) and end >= theEnder):
        print("You overclicked! GG")
        time.sleep(3)
        root.destroy()

#---------------------------------------------------------------------------------------------------------------#

##
def buttonS (event):
    global hit
    hit = False
    
    #if (curLevel >= diffTwo):
        #screen.create_oval(buttonX-increment, buttonX, buttonY-increment, buttonY, fill="black")
       # screen.create_oval(buttonX+increment, buttonX, buttonY+increment, buttonY, fill="black")
    #else:
        #screen.create_oval(buttonX, buttonX, buttonY, buttonY, fill="black")


#---------------------------------------------------------------------------------------------------------------#
       
##def timeChange():
##    global timeIncrement
##    if (curLevel >= 20):
##        timeIncrement -= 0.01
##
##    print("timeIncrement is currently: " + str(timeIncrement))


#---------------------------------------------------------------------------------------------------------------#

setup()
screen.bind("<ButtonPress-1>", mouseClickDetector)
screen.bind("<ButtonRelease-1>", buttonS)
screen.pack()
screen.focus_set()

root.mainloop()
