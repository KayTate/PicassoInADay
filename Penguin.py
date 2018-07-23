def showPenguin():
    background(255)
    
#Penguin Body
    strokeWeight(7)
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
    strokeWeight(7)
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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # ellipse(350,350,50,40)                  #feet
    # ellipse(410,350,50,40)                 #feet
    # rect(330,140,100,200,50)                 #body
    # curve(100,200,75,66,20,170,300,300)    #left wing
    # curve(100,200,125,66,180,170,-100,300) #right wing
    # rect(350,90,60,70,50)                   #head
    # rect(350,180,60,130,50)                 #belly
    # line(20,169,50,110)
    # line(179,169,150,110)
    # strokeWeight(1)
    # eye = 20                               #sets eye radius
    # ellipse(368,37,eye,eye)                 #left eye
    # ellipse(492,37,eye,eye)                #right eye
    # fill(0)
    # ellipse(368,37,eye/2,eye/2)             #left pupil
    # ellipse(492,37,eye/2,eye/2)            #right pupil
    # fill(255)
    # noStroke()
    # triangle(370,52,380,67,390,52)          #nose
    # triangle(370,52,380,47,390,52)          #nose pt. 2
    # stroke(2)
    # line(370,52,380,67)
    # line(380,67,390,52)
    # line(370,52,380,47)
    # line(380,47,390,52)
