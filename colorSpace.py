bS = 35
xC = 10
bS2 = 25
xC2 = 15

def colorBox(): 
    global page
    fill(255)
    stroke(0)
    strokeWeight(1)
    
    #Tool palette
    rect(5, 5, 80, 540)
    
    #Drawing space
    rect(100, 5, 595, 540)
    
    #Brown
    noStroke()
    fill(104, 67, 42) 
    rect(xC, 10, bS, bS)  
    
    #Black
    noStroke()
    fill(0)
    rect(bS, 52.5, bS, bS)
    
    #Pink
    fill(219, 112, 147)
    rect(xC, 95, bS, bS)
    
    #Purple
    fill(160, 32, 240)
    rect(bS, 137.5, bS, bS)
    
    #Green
    fill(0, 100, 0)
    rect(xC, 180, bS, bS)
    
    #Blue
    fill(0, 0, 255)
    rect(bS, 222.5, bS, bS)
    
    #Yellow
    fill(255, 255, 0)
    rect(xC, 265, bS, bS)
    
    #Orange
    fill(255, 140, 0) 
    rect(bS, 307.5, bS, bS) 
    
    #Red
    fill(255, 0, 0)
    rect(xC, 350, bS, bS)
    
    #Random color
    stroke(0)
    noFill()
    img = loadImage("question-mark.jpg")
    image(img, 30, 393.5, 45, 35)
    strokeWeight(1)
    rect(bS, 392.5, bS, bS)

    #medium stroke
    strokeWeight(3)
    ellipse(27.5, 447, xC, xC)
    strokeWeight(1)
    rect(xC2, 435, bS2, bS2)
    
    #thick stroke
    strokeWeight(5)
    ellipse(63, 447, xC, xC)
    strokeWeight(1)
    rect(50, 435, bS2, bS2)
    
    #thickest stroke
    strokeWeight(8)
    ellipse(27.5, 489, xC, xC)
    strokeWeight(1)
    rect(15, 477.5, bS2, bS2) 

    #Regular thin stroke weight
    strokeWeight(1)
    ellipse(63, 489, xC, xC)
    rect(50, 477.5, bS2, bS2) 
    
    #Clear Box
    titleFont = loadFont("CurlzMT-48.vlw")
    textFont(titleFont)
    textSize(18);
    text("CLEAR", 15, 535);
    rect(xC, 515, 65, bS2)
