from colorSpace import *

def Snowman():
    colorBox()
    #the body
    ellipse(375, 442, 200, 200)
    ellipse(375, 268, 150, 150)
    ellipse(375, 144, 100, 100)
    
    #the Accesories
        #the hat
    rect(325, 80, 100, 15)
    rect(342, 25, 70, 55)
        #eyes
    ellipse(350, 130, 15, 15)
    ellipse(400, 130, 15, 15)
        #nose
    triangle(375, 144, 375, 155, 400, 155)
        #smile
    curve(375, 140, 350, 165, 390, 165, 350, 140)
        #buttons
    ellipse(375, 238, 15, 15)
    ellipse(375, 268, 15, 15)
    ellipse(375, 298, 15, 15)
        #the left arm
    line(200, 300, 300, 268)
    line(200, 268, 220, 295)
    line(210, 325, 220, 293)
        #the right arm
    line(450, 268, 550, 295)
    line(526, 287, 547, 267)
    line(525, 287, 543, 315)
