from colorSpace import *

<<<<<<< HEAD

def setup():
    size(700, 550)         # width, height//screen size
    colorBox()
=======
from Penguin import *
from Title import *
from Ice_Cream import *
from Finished import *
from Lollipop import *

page = "Title"

def setup():
    size(700,550)
    
def draw():
    global page
    if page == "Title":
        titlePage()
        if mousePressed and mouseX > 40.5 and mouseX < 191.5 and mouseY > 200 and mouseY < 350:
            page = "Penguin"
        if mousePressed and mouseX > 274.5 and mouseX < 424.5 and mouseY > 200 and mouseY < 350:
            page = "Ice Cream"
    if page == "Penguin":
        background(255)
        showPenguin()
    if page == "Ice Cream":
        background(255)
        icecream()

        
>>>>>>> 2b634d9e69edf08a15747641be1f7c54657578ec
