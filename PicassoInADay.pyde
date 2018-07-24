from colorSpace import *
from Penguin import *
from Title import *
from Ice_Cream import *
from Finished import *
from Lollipop import *

penguinAlreadyDrawn = False
iceCreamAlreadyDrawn = False
lollipopAlreadyDrawn = False
page = "Finished" #Other options: Penguin, Ice Cream, Lollipop, Finished


def setup():
    size(700,550)
    
def draw():
    global page, penguinAlreadyDrawn, iceCreamAlreadyDrawn
    if page == "Title":
        titlePage()
        if mousePressed and mouseX > 40.5 and mouseX < 191.5 and mouseY > 200 and mouseY < 350:
            page = "Penguin"
        if mousePressed and mouseX > 274.5 and mouseX < 424.5 and mouseY > 200 and mouseY < 350:
            page = "Ice Cream"
    if page == "Penguin":
        if not penguinAlreadyDrawn:
            background(255)
            showPenguin()
            penguinAlreadyDrawn = True
        if mousePressed and mouseX > 100 and mouseX < 695 and mouseY > 5 and mouseY < 540 and pmouseX > 100 and pmouseX < 695 and pmouseY > 5 and pmouseY < 540:
            line(pmouseX, pmouseY, mouseX, mouseY) 
    if page == "Ice Cream":
        if not iceCreamAlreadyDrawn:
            background(255)
            icecream()
            iceCreamAlreadyDrawn = True
        if mousePressed and mouseX > 100 and mouseX < 695 and mouseY > 5 and mouseY < 540 and pmouseX > 100 and pmouseX < 695 and pmouseY > 5 and pmouseY < 540:
            line(pmouseX, pmouseY, mouseX, mouseY) 
    if page == "Lollipop":
        background(255)
        lollipop()
        if mousePressed and mouseX > 100 and mouseX < 695 and mouseY > 5 and mouseY < 540 and pmouseX > 100 and pmouseX < 695 and pmouseY > 5 and pmouseY < 540:
            line(pmouseX, pmouseY, mouseX, mouseY) 
    if page == "Finished":
        finished()
        if mousePressed and mouseX > 580 and mouseX < 680 and mouseY > 490 and mouseY < 540:
            page = "Title"
    # if mousePressed and mouseX > 100 and mouseX < 695 and mouseY > 5 and mouseY < 540 and pmouseX > 100 and pmouseX < 695 and pmouseY > 5 and pmouseY < 540:
    #    line(pmouseX, pmouseY, mouseX, mouseY) 
