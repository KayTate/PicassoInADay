from colorSpace import *

def Snowman():
    colorBox()

#Body
    ellipse(375, 442, 200, 200)
    ellipse(375, 268, 150, 150)
    ellipse(375, 144, 100, 100)
    
#Hat
    rect(325, 80, 100, 15)
    rect(342, 25, 70, 55)
    
#Eyes
    ellipse(350, 130, 15, 15)
    ellipse(400, 130, 15, 15)
    
#Nose
    triangle(375, 144, 375, 155, 400, 155)
    
#Smile
    curve(375, 140, 350, 165, 390, 165, 350, 140)
    
#Buttons
    ellipse(375, 238, 15, 15)
    ellipse(375, 268, 15, 15)
    ellipse(375, 298, 15, 15)
    
#Left arm
    line(200, 300, 300, 268)
    line(200, 268, 220, 295)
    line(210, 325, 220, 293)
    
#Right arm
    line(450, 268, 550, 295)
    line(526, 287, 547, 267)
    line(525, 287, 543, 315)
