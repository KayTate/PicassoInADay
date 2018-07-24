bS = 35
xC = 10
bS2 = 25
xC2 = 15
# add 42.5 to every y cordinate ( for the outer color box)

def colorBox(): 
    fill(255)
    rect(5, 5, 80, 540)    # xCoordinate, yCoordinate, width, height//side color selector
    rect(100, 5, 595, 540) # color space box
    
    rect(xC, 10, bS, bS)   # x, y, w, h//white
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
    rect(bS, 392.5, bS, bS) # outer box//random colors
                # EDITTING TOOLS
    strokeWeight(3)
    ellipse(27.5, 447, xC, xC)
    strokeWeight(1)
    rect(xC2, 435, bS2, bS2) # medium stroke
    strokeWeight(5)
    ellipse(63, 447, xC, xC)
    strokeWeight(1)
    img = loadImage("Eraser.png")
    image(img, 8, 470, 45, 45)
    rect(xC2, 477.5, bS2, bS2) # eraser
    rect(50, 435, bS2, bS2) # thick stroke
    rect(50, 477.5, bS2, bS2) # paint bucket 
    textSize(18);
    text("CLEAR", 15, 535);
    rect(xC, 515, 65, bS2) # CLEAR box
    
    
    

    

def mouseClicked():
    if mouseX > 10 and mouseX < 45 and mouseY > 10 and mouseY < 45:
        print("yellow")
        stroke(255, 255, 0)
    elif mouseX > 35 and mouseX < 70 and mouseY > 52.5 and mouseY < 87.5:
        stroke(0, 0, 0)
    elif mouseX > 10 and mouseX < 45 and mouseY > 95 and mouseY < 130:
        stroke(219, 112, 147)
    elif
        
        
        
        
        
        
        
        
        
        
        
        
        
        
