def finished(number):
    background(255)
    titleFont = loadFont("CurlzMT-48.vlw")
    textFont(titleFont)
        
    #Loads and displays image
    frame1 = loadImage("frame_000.png")
    image(frame1,0,0,700,550)
    
    #List for motivational quotes
    motivation = [
            "You're a winner!",         #0
            "That was beautiful!",      #1
            "You're the new Picasso!"   #2
            ]
    
    listIndex = number
    
    #Rectangle containing text at the center of the screen
    strokeWeight(3)
    stroke("#E88AD8")
    fill(255,255,255,200)
    rect(87.5,137.5,525,275,50)
    
    #Displays text in the center of the rectangle
    fill("#E88AD8")
    textSize(45)
    if listIndex == 0:
        text(motivation[0], 175, 275)
    if listIndex == 1:
        text(motivation[1], 145, 275)
    if listIndex == 2:
        text(motivation[2], 92, 275)
    
    #Start over button
    stroke("#E88AD8")
    fill(255,255,255,200)
    rect(580,490,100,50,15)
    
    #Start over text
    textSize(20)
    fill("#E88AD8")
    text("Start Over",582,520)
