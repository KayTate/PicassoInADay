from colorSpace import *
from Penguin import *
from Title import *
from Ice_Cream import *
from Finished import *
from Lollipop import *
from Buttons import *

penguinAlreadyDrawn = False
iceCreamAlreadyDrawn = False
lollipopAlreadyDrawn = False
page = "Title" #Other options: Penguin, Ice Cream, Lollipop, Finished
number = int(random(0,3))

def setup():
    size(700,550)
    
    
def draw():
    global page, penguinAlreadyDrawn, iceCreamAlreadyDrawn, number, lollipopAlreadyDrawn
    if page == "Title":
        titlePage()
        if mousePressed and mouseX > 40.5 and mouseX < 191.5 and mouseY > 200 and mouseY < 350:
            page = "Penguin"
        if mousePressed and mouseX > 274.5 and mouseX < 424.5 and mouseY > 200 and mouseY < 350:
            page = "Ice Cream"
        if mousePressed and mouseX > 506.5 and mouseX < 656.5 and mouseY > 200 and mouseY < 350:
            page = "Lollipop"
            
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
            
    if page == "Finished":
        finished(number)
        if mousePressed and mouseX > 580 and mouseX < 680 and mouseY > 490 and mouseY < 540:
            page = "Title"
            
    elif page != "Finished" or page != "Title":
        if mousePressed and mouseX > 630 and mouseX < 680 and mouseY > 20 and mouseY < 70:
            page = "Finished"
        #code used for the next button
def mouseClicked():    
    global page
    if page == "Penguin" and mouseX > 560 and mouseX < 610 and mouseY > 20 and mouseY < 70:
        page = "Ice Cream"
    elif page == "Ice Cream"  and mouseX > 560 and mouseX < 610 and mouseY > 20 and mouseY < 70:
        page = "Lollipop"
    elif page == "Lollipop" and mouseX > 560 and mouseX < 610 and mouseY > 20 and mouseY < 70:
        page = "Finished"
        
         # elif mousePressed and mouseX > 560 and mouseX < 610 and mouseY > 20 and mouseY < 70:
         #     if page == "Penguin":
         #         page = "Ice Cream"
         #     elif page == "Ice Cream":
         #         page = "Lollipop"
         #     elif page == "Lollipop":
         #         page = "Finished"
