def showPenguin():
    strokeWeight(7)
    fill(255)
    ellipse(70,270,50,40)                  #feet
    ellipse(130,270,50,40)                 #feet
    rect(50,60,100,200,50)                 #body
    curve(100,200,75,66,20,170,300,300)    #left wing
    curve(100,200,125,66,180,170,-100,300) #right wing
    rect(70,10,60,70,50)                   #head
    rect(70,100,60,130,50)                 #belly
    line(20,169,50,110)
    line(179,169,150,110)
    
    
    
    strokeWeight(1)
    eye = 20                               #sets eye radius
    ellipse(88,37,eye,eye)                 #left eye
    ellipse(112,37,eye,eye)                #right eye
    fill(0)
    ellipse(88,37,eye/2,eye/2)             #left pupil
    ellipse(112,37,eye/2,eye/2)            #right pupil
    fill(255)
    noStroke()
    triangle(90,52,100,67,110,52)          #nose
    triangle(90,52,100,47,110,52)          #nose pt. 2
    stroke(2)
    line(90,52,100,67)
    line(100,67,110,52)
    line(90,52,100,47)
    line(100,47,110,52)
