from colorSpace import *
from Penguin import *
from Title import *
from Ice_Cream import *
from Finished import *
from Lollipop import *
from Buttons import *
from Rainbow import *
from House import *
from snowman import *

penguinAlreadyDrawn = False
iceCreamAlreadyDrawn = False
lollipopAlreadyDrawn = False
rainbowAlreadyDrawn = False
houseAlreadyDrawn = False
snowmanAlreadyDrawn = False
page = "Snowman" #Other options: Penguin, Ice Cream, Lollipop, Finished, Rainbow, House, Snowman
number = int(random(0,3))

def setup():
    size(700,550)
    
def draw():
    global page, penguinAlreadyDrawn, iceCreamAlreadyDrawn, number, lollipopAlreadyDrawn, rainbowAlreadyDrawn, houseAlreadyDrawn, snowmanAlreadyDrawn
    if page == "Title":
        titlePage()
        if mousePressed and mouseX > 40.5 and mouseX < 191.5 and mouseY > 130 and mouseY < 280:
            page = "Penguin"
        if mousePressed and mouseX > 274.5 and mouseX < 424.5 and mouseY > 130 and mouseY < 280:
            page = "Ice Cream"
        if mousePressed and mouseX > 506.5 and mouseX < 656.5 and mouseY > 130 and mouseY < 280:
            page = "Lollipop"
        if mousePressed and mouseX > 40.5 and mouseX < 191.5 and mouseY > 345 and mouseY < 495:
            page = "Rainbow"
        if mousePressed and mouseX > 274.5 and mouseX < 424.5 and mouseY > 345 and mouseY < 495:
            page = "House"
#Edits

    if page == "Penguin":
        if not penguinAlreadyDrawn:
            background(255)
            showPenguin()
            finishedButton()
            nextPage()
            penguinAlreadyDrawn = True
        if mousePressed and mouseX > 100 and mouseX < 695 and mouseY > 5 and mouseY < 540 and pmouseX > 100 and pmouseX < 695 and pmouseY > 5 and pmouseY < 540:
            line(pmouseX, pmouseY, mouseX, mouseY)
            
    if page == "Ice Cream":
        if not iceCreamAlreadyDrawn:
            background(255)
            icecream()
            finishedButton()
            nextPage()
            iceCreamAlreadyDrawn = True
        if mousePressed and mouseX > 100 and mouseX < 695 and mouseY > 5 and mouseY < 540 and pmouseX > 100 and pmouseX < 695 and pmouseY > 5 and pmouseY < 540:
            line(pmouseX, pmouseY, mouseX, mouseY) 
            
    if page == "Lollipop":
        if not lollipopAlreadyDrawn:
            background(255)
            lollipop()
            finishedButton()
            nextPage()
            lollipopAlreadyDrawn = True
        if mousePressed and mouseX > 100 and mouseX < 695 and mouseY > 5 and mouseY < 540 and pmouseX > 100 and pmouseX < 695 and pmouseY > 5 and pmouseY < 540:
            line(pmouseX, pmouseY, mouseX, mouseY)
    
    if page == "Rainbow":
        if not rainbowAlreadyDrawn:
            background(255)
            rainbow()
            finishedButton()
            nextPage()
            rainbowAlreadyDrawn = True
        if mousePressed and mouseX > 100 and mouseX < 695 and mouseY > 5 and mouseY < 540 and pmouseX > 100 and pmouseX < 695 and pmouseY > 5 and pmouseY < 540:
            line(pmouseX, pmouseY, mouseX, mouseY) 
            
    if page == "House":
        if not houseAlreadyDrawn:
            background(255)
            house()
            finishedButton()
            nextPage()
            houseAlreadyDrawn = True
        if mousePressed and mouseX > 100 and mouseX < 695 and mouseY > 5 and mouseY < 540 and pmouseX > 100 and pmouseX < 695 and pmouseY > 5 and pmouseY < 540:
            line(pmouseX, pmouseY, mouseX, mouseY) 
            
    if page == "Snowman":
        if not snowmanAlreadyDrawn:
            background(255)
            Snowman()
            finishedButton()
            nextPage()
            snowmanAlreadyDrawn = True
        if mousePressed and mouseX > 100 and mouseX < 695 and mouseY > 5 and mouseY < 540 and pmouseX > 100 and pmouseX < 695 and pmouseY > 5 and pmouseY < 540:
            line(pmouseX, pmouseY, mouseX, mouseY) 
                         
    if page == "Finished":
        finished(number)
        if mousePressed and mouseX > 580 and mouseX < 680 and mouseY > 490 and mouseY < 540:
            page = "Title" 
            iceCreamAlreadyDrawn = False
            penguinAlredyDrawn = False
            lollipopAlreadyDrawn = False

    elif page != "Finished" or page != "Title":
        if mousePressed and mouseX > 630 and mouseX < 680 and mouseY > 20 and mouseY < 70:
            page = "Finished"

    if mousePressed and mouseX > 35 and mouseX < 70 and mouseY > 392 and mouseY < 427.5:
         stroke(random(255), random(255), random(255)) # random color box
         print("random")
    
    # updateRainbowColor()        
        #code used for the next button
        
        
        #penguinAlreadyDrawn = False
       #iceCreamAlreadyDrawn = False
       #lollipopAlreadyDrawn = False
        #rainbowAlreadyDrawn = False

def mouseClicked():
    global page, iceCreamAlreadyDrawn, penguinAlreadyDrawn, lollipopAlreadyDrawn
    if iceCreamAlreadyDrawn and penguinAlreadyDrawn and lollipopAlreadyDrawn:
        page = "Finished"
    elif page == "Penguin" and mouseX > 560 and mouseX < 610 and mouseY > 20 and mouseY < 70:
        page = "Ice Cream" 
    elif page == "Ice Cream"  and mouseX > 560 and mouseX < 610 and mouseY > 20 and mouseY < 70:
        page = "Lollipop"
    elif page == "Lollipop" and mouseX > 560 and mouseX < 610 and mouseY > 20 and mouseY < 70:
        page = "Penguin"
        
        


    if page != "Finished" or page != "Title":
        if mousePressed and mouseX > 100 and mouseX < 695 and mouseY > 5 and mouseY < 540 and pmouseX > 100 and pmouseX < 695 and pmouseY > 5 and pmouseY < 540:
            line(pmouseX, pmouseY, mouseX, mouseY)
        if mouseX > 10 and mouseX < 45 and mouseY > 10 and mouseY < 45:
            # print("yellow")
            stroke(104, 67, 42)
            # rainbowMode = True
        elif mouseX > 35 and mouseX < 70 and mouseY > 52.5 and mouseY < 87.5:
            stroke(0, 0, 0) # black//outer box
            # rainbowMode = True
        elif mouseX > 10 and mouseX < 45 and mouseY > 95 and mouseY < 130:
            stroke(219, 112, 147) # pink
            # rainbowMode = True
        elif mouseX > 35 and mouseX < 70 and mouseY > 137.5 and mouseY < 172.5:
            stroke(160, 32, 240) # purple//outer box
            # rainbowMode = True
        elif mouseX > 10 and mouseX < 45 and mouseY > 180 and mouseY < 215:
            stroke(0, 100, 0) # green
            # rainbowMode = True
        elif mouseX > 35 and mouseX < 70 and mouseY > 222.5 and mouseY < 257.5:
            stroke(0, 0, 255) # blue//outer box
            # rainbowMode = True
        elif mouseX > 10 and mouseX < 45 and mouseY > 265 and mouseY < 300:
            stroke(255, 255, 0) # yellow
            # rainbowMode = True
        elif mouseX > 35 and mouseX < 70 and mouseY > 307.5 and mouseY < 342.5:
            stroke(255, 140, 0) # orange//outer box
            # rainbowMode = True
        elif mouseX > 10 and mouseX < 45 and mouseY > 350 and mouseY < 385:
            stroke(255, 0, 0) # red
            # rainbowMode = True
        elif mouseX > 10 and mouseX < 75 and mouseY > 515 and mouseY < 540: # clear
            clearPage()
            print("clear")
        elif mousePressed and mouseX > 35 and mouseX < 70 and mouseY > 392 and mouseY < 427.5:
            stroke(random(255), random(255), random(255))
            print("random")
        elif mouseX > 50 and mouseX < 75 and mouseY > 435 and mouseY < 460:
            # print("yes")
            strokeWeight(7) # thick stroke weight
        elif mouseX > 50 and mouseX < 75 and mouseY > 477.5 and mouseY < 502.5:
            # print("right")
            strokeWeight(1) # thin stroke weight
        elif mouseX > 15 and mouseX < 40 and mouseY > 435 and mouseY < 460:
            # print("left")  
            strokeWeight(3) 
