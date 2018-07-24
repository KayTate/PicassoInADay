def finished():
    
    #Loads GIF frames
    frame1 = loadImage("frame_000.png")
    frame2 = loadImage("frame_001.png")
    frame3 = loadImage("frame_002.png")
    frame4 = loadImage("frame_003.png")
    frame5 = loadImage("frame_004.png")
    frame6 = loadImage("frame_005.png")
    frame7 = loadImage("frame_006.png")
    frame8 = loadImage("frame_007.png")
    frame9 = loadImage("frame_008.png")
    frame10 = loadImage("frame_009.png")
    frame11 = loadImage("frame_010.png")
    
    #image(frame1,0,0,700,550) #Temporarily displays the first frame of the GIF
    for i in range(100):
        background(255)
        image(frame1,0,0,700,550)
        background(255)
        image(frame2,0,0,700,550)
        background(255)
        image(frame3,0,0,700,550)
        background(255)
        image(frame4,0,0,700,550)
        background(255)
        image(frame5,0,0,700,550)
        background(255)
        image(frame6,0,0,700,550)
        background(255)
        image(frame7,0,0,700,550)
        background(255)
        image(frame8,0,0,700,550)
        background(255)
        image(frame9,0,0,700,550)
        background(255)
        image(frame10,0,0,700,550)
        background(255)
        image(frame11,0,0,700,550)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #List for motivational quotes
    motivation = [
            "You're a winner!",         #0
            "That was beautiful!",      #1
            "You're the new Picasso!"   #2
            ]
    
    # if listIndexSet == False:
    #     number = int(random(0,len(motivation)-1)) #randomly generates item number from list
    #     listIndexSet = True
    listIndex = 2
    
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
