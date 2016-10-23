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
x1 = 350
y1 = 350
x2 = 450
y2 = 450
xx1 = 350
yy1 = 350
xx2 = 450
yy2 = 450
curLevel = 0 #keeps track of what level you are on, which is displayed on the bottom of the screen
timeIncrement = 2 #Every level is this long
end = 0 #Keeps track of the current time
theEnder = end+timeIncrement # as long as end is less than this, the program will continue to register clicks
diffTwo = 5
diffThree = 15
maxRoll = 9
##buttonTwoHit = False


#---------------------------------------------------------------------------------------------------------------#
##draw() simply draws the text on the canvas, along with the buttons. If it is red, then you don't need to
## tap anymore. If it's black, keep tapping! Otherwise, it turns white (you went over, so you lose!)

def draw():
    global levelText, tapText, timerText, end, buttonBlack, buttonRed
    
    level = "Current level: " + str(curLevel)
    taps = str(numTaps)
    tapsHard = str(numTapsHard)
    times = "{0:.2f}".format(end) + " seconds have passed."
    
    levelText = screen.create_text(400, 700, text=level, font = "fixedsys 20", anchor=CENTER, fill = "black" )
    if (curLevel >= diffThree):
        tapText = screen.create_text(x1+50, y1+50, text=tapsHard, font="fixedsys 20", anchor=CENTER, fill="red")
    else:
        tapText = screen.create_text(x1+50, y1+50, text=taps, font="fixedsys 20", anchor=CENTER, fill="red")
    timerText = screen.create_text(400, 50, text=times, font="fixedsys 20", fill="black")


#---------------------------------------------------------------------------------------------------------------#

def colorChanger():
    global button

    #somethingDrawn = True
    
    if (numTaps == 0):
        screen.delete(blackCircle)
        button = screen.create_oval(x1, y1, x2, y2, fill="red")
    elif (numTaps < 0):
        button = screen.create_oval(x1, y1, x2, y2, fill="white")


#---------------------------------------------------------------------------------------------------------------#

##def deleteCircle():
##    global somethingDrawn
##    
##    if (somethingDrawn == True):
##        print("RED")
##        screen.delete(button)
##
##    somethingDrawn = False
        
#---------------------------------------------------------------------------------------------------------------#
    
## setup() initializes some variables, and calls draw() to draw the basic setup.
def setup():
    global curLevel, numTaps, buttonHit, blackCircle, buttonTwoHit, numTapsTwo, numTapsHard

    blackCircle = screen.create_oval(x1, y1, x2, y2, fill = "black")
    somethingDrawn = True
    numTaps = 1
    numTapsHard = 1
    #numTapsTwo = 1
    curLevel = 0
    draw()
    buttonHit = False
    
#---------------------------------------------------------------------------------------------------------------#

## detects any clicking of the button
def mouseClickDetector(event):
    global numTaps, curLevel, end, start, buttonHit, hit
    #print ( "Mouse clicked at " + str( event.x ) + "," + str(event.y ))

    xMouse = event.x
    yMouse = event.y

    if xMouse >= x1 and xMouse <= x2 and yMouse >= y1 and yMouse <= y2 and curLevel == 0:
        buttonHit = True
        hit = True
        mainGame()
    elif xMouse >= x1 and xMouse <= x2 and yMouse >= y1 and yMouse <= y2:
        buttonHit = True
        hit = True
    elif numTaps <= 0 and xMouse:
        numTaps -= 1


#---------------------------------------------------------------------------------------------------------------#

##def mouseTwoClickDetector(event):
##    global buttonTwoHit, hitTwo, numTaps
##    xMouse = event.x
##    yMouse = event.y
##
##    if xMouse >= xx1 and xMouse <= xx2 and yMouse >= yy1 and yMouse <= yy2:
##        buttonTwoHit = True
##        hitTwo = True
##        print("YO")
##    elif numTapsTwo <= 0 and xMouse:
##        numTapsTwo -= 1
    

#---------------------------------------------------------------------------------------------------------------#
        
## if the button was clicked, decreases the number of remaining taps. currently self-destructs at level 100.
def clicker():
    global numTaps, buttonHit, curLevel, buttonTwoHit
    
    if (buttonHit == True):
        numTaps = numTaps - 1
        buttonHit = False
        screen.delete(levelText, tapText, timerText)
        draw()
        screen.update()

##    if (buttonTwoHit == True):
##        numTapsTwo = numTapsTwo - 1
##        buttonTwoHit = False
##        screen.delete(levelText, tapText, timerText)
##        draw()
##        screen.update()
##        
    if (curLevel == 100):
        root.destroy()


#---------------------------------------------------------------------------------------------------------------#

## is the key part of the game, updates the level if you're at the right number taps, and runs the while loop
## which tests out 
def mainGame():
    global end, theEnder, curLevel, numTaps, blackCircle, numTapsTwo, numTapsHard

    if (curLevel > diffThree):
        blackCircle = screen.create_oval(x1, y1, x2, y2, fill="black")
##        blueCircle = screen.create_oval(xx1, yy1, xx2, yy2, fill="blue")
    elif (curLevel > 0):
        blackCircle = screen.create_oval(x1, y1, x2, y2, fill="black")
        
        
    while (end < theEnder):
        clicker()
        screen.delete(levelText, tapText, timerText)
        end = time.clock()
        colorChanger()
        draw()
        screen.delete(button)
        screen.update()        

    if (numTaps == 0):
        curLevel = curLevel + 1
        numTaps = randint(1, maxRoll)
        #numTapsTwo = randint(1, maxRoll)
        numTapsHard = numTaps
        theEnder += timeIncrement
        if (curLevel >= diffTwo):   
            positionChanger()
        mainGame()
        
    elif ((numTaps > 0 or numTaps < 0) and end >= theEnder):
        print("You didn't do the right number of clicks! GG")
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

def positionChanger():
    global x1, x2, y1, y2
    x1 = randint(100, 700)
    y1 = randint(200, 600)
    x2 = x1+100
    y2 = y1+100
##    xx1 = randint(100, 700)
##    yy1 = randint (200, 600)
##    xx2 = xx1 + 100
##    yy2 = yy1 + 100
    #screen.create_oval(x1, y1, x2, y2, fill="green")

#---------------------------------------------------------------------------------------------------------------#

def quitGame(event):

    print("You pressed Q, so the game quit!")
    time.sleep(2)
    root.destroy()
    
#---------------------------------------------------------------------------------------------------------------#
       
setup()
screen.bind("<ButtonPress-1>", mouseClickDetector)
##screen.bind("<ButtonPress-3>", mouseTwoClickDetector)
screen.bind("q", quitGame)
screen.bind("<ButtonRelease-1>", buttonS)
screen.pack()
screen.focus_set()

root.mainloop()

