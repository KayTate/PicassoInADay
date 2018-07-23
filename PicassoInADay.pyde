from colorSpace import *
from Penguin import *
from Title import *

page = "Title"

def setup():
    size(700,550)
    
def draw():
    global page
    if page == "Title":
        titlePage()
        if mousePressed and mouseX > 49 and mouseX < 200 and mouseY > 200 and mouseY < 350:
            page = "Penguin"
    if page == "Penguin":
        background(255)
        colorSpace()
        showPenguin()
        
