bS = 35
xC = 10
bS2 = 25
xC2 = 15
# add 42.5 to every y cordinate ( for the outer color box)

# rainbowMode = False


def colorBox(): 
    global page
    fill(255)
    stroke(0)
    strokeWeight(1)
    rect(5, 5, 80, 540)    # xCoordinate, yCoordinate, width, height//side color selector
    rect(100, 5, 595, 540) # color space box
    noStroke()
    fill(104, 67, 42) # brown
    rect(xC, 10, bS, bS)   # x, y, w, h
    noStroke()
    fill(0) # black
    rect(bS, 52.5, bS, bS) # x, y, w, h//outer box
    fill(219, 112, 147) # pink
    rect(xC, 95, bS, bS)
    fill(160, 32, 240) # purple
    rect(bS, 137.5, bS, bS) # outer box
    fill(0, 100, 0) #  green
    rect(xC, 180, bS, bS)
    fill(0, 0, 255) # blue
    rect(bS, 222.5, bS, bS) # outer box
    fill(255, 255, 0) # yellow
    rect(xC, 265, bS, bS)
    fill(255, 140, 0) # orange
    rect(bS, 307.5, bS, bS) # outer box
    fill(255, 0, 0) # red
    rect(xC, 350, bS, bS)
    stroke(0)
    noFill()
    img = loadImage("question-mark.jpg")
<<<<<<< HEAD
    image(img, bS, 392.5, 20, 15)
=======
    image(img, 30, 393.5, 45, 35)
    strokeWeight(1)
>>>>>>> 45cbaba4824e298d9aefb7dc96395f45e5975763
    rect(bS, 392.5, bS, bS) # outer box//random colors
                   # EDITTING TOOLS
    strokeWeight(3)
    ellipse(27.5, 447, xC, xC)
    strokeWeight(1)
    rect(xC2, 435, bS2, bS2) # medium stroke
    
    strokeWeight(5)
    ellipse(63, 447, xC, xC)
    strokeWeight(1)
    rect(50, 435, bS2, bS2) # thick stroke
    
    strokeWeight(8)
    ellipse(27.5, 489, xC, xC)
    strokeWeight(1)
    rect(15, 477.5, bS2, bS2) # thickest stroke

    strokeWeight(1)
    ellipse(63, 489, xC, xC)
    rect(50, 477.5, bS2, bS2) # regular thin stroke weight
    
    titleFont = loadFont("CurlzMT-48.vlw")
    textFont(titleFont)
    textSize(18);
    text("CLEAR", 15, 535);
    rect(xC, 515, 65, bS2) # CLEAR box
    
    
# def setRainbowMode():
#     global rainbowMode
#     rainbowMode = True
    
    
# def updateRainbowColor():
#     stroke(random(255), random(255), random(255))
