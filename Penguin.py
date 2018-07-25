from colorSpace import *

def showPenguin():
    background(255) 
    colorBox()
    
    
#Penguin Body
    strokeWeight(2)
    fill(255)
    #Feet
    ellipse(350,415,50,30) #Left Foot
    ellipse(420,415,50,30) #Right Foot
    
    #Torso
    rect(330,180,110,230,50) #Body
    rect(350,220,70,150,50) #Tummy
    
    #Head; Note: line of symmetry for head = 385
    eyeSize = 20
    rect(350,120,70,80,50) #Head
    strokeWeight(1)
    ellipse(373,150, eyeSize, eyeSize) #Left Eye
    ellipse(397,150, eyeSize, eyeSize) #Right Eye
    noStroke()
    triangle(385,166,
             375,171,
             395,171) #Top of Nose
    triangle(385,181,
             375,171,
             395,171) #Bottom of Nose
    stroke(0)
    line(385,166,375,171)
    line(385,166,395,171)
    line(385,181,375,171)
    line(385,181,395,171)
    fill(0)
    ellipse(373,150, eyeSize/2, eyeSize/2) #Left Pupil
    ellipse(397,150, eyeSize/2, eyeSize/2) #Right Pupil
    
    #Wings
    strokeWeight(2)
    fill(255)
    curve(385,300, #Left Wing
          342,193,
          284,295,
          400,400) 
    line(342,193,284,295)
    curve(385,300, #Right Wing
          428,193,
          486,295,
          370,400)
    line(428,193,486,295)

    strokeWeight(1)
