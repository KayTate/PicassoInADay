from colorSpace import *

def lollipop():
    colorBox()

    white = 255
    
    strokeWeight(2)
    noFill()
    ellipse(255, 225, 110, 110)  #left big lollipop
    ellipse(255, 225, 74, 74)
    ellipse(255, 225, 38, 38)
    noFill()
    rect(252, 280, 10, 263)
    
    noFill()     #small center lollipop
    ellipse(375, 320, 80, 80)
    ellipse(375,320,54,54)
    ellipse(375,320,28,28)
    noFill()
    rect(373, 360, 7, 183)

    noFill()                     #small left lollipop
    ellipse(150, 320, 80, 80)
    ellipse(150,320,54,54)
    ellipse(150,320,28,28)
    noFill()
    rect(148, 360, 7, 183)
            
    noFill()                    #small far right lollipop
    ellipse(600, 320, 80, 80)
    ellipse(600,320,54,54)
    ellipse(600,320,28,28)
    noFill()
    rect(597, 360, 7, 183)

    noFill()     #center right big lollipop
    ellipse(495, 225, 110, 110)
    ellipse(495, 225, 74, 74)
    ellipse(495, 225, 38, 38)
    noFill()
    rect(490, 280, 10, 263)
