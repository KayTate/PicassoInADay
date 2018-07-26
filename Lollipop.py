from colorSpace import *

def lollipop():
    colorBox()
    
    strokeWeight(2)
    noFill()
    
    #Left Big Lollipop
    ellipse(255, 225, 110, 110)
    ellipse(255, 225, 74, 74)
    ellipse(255, 225, 38, 38)
    rect(252, 280, 10, 263)
    
    #Small Center Lollipop
    ellipse(375, 320, 80, 80)
    ellipse(375,320,54,54)
    ellipse(375,320,28,28)
    rect(373, 360, 7, 183)
    
    #Small Left Lollipop
    ellipse(150, 320, 80, 80)
    ellipse(150,320,54,54)
    ellipse(150,320,28,28)
    rect(148, 360, 7, 183)
    
    #Small Right Lollipop
    ellipse(600, 320, 80, 80)
    ellipse(600,320,54,54)
    ellipse(600,320,28,28)
    rect(597, 360, 7, 183)

    #Right Big Lollipop
    ellipse(495, 225, 110, 110)
    ellipse(495, 225, 74, 74)
    ellipse(495, 225, 38, 38)
    rect(490, 280, 10, 263)
