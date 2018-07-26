def more():
    img = loadImage("stripedStairs.jpg")
    background(255)
    image(img, 0, 0, 700, 550)
    
    #Header
    fill(51, 175, 255)
    noStroke()
    rect(0,0,700,100)
    
    fill(0)
    titleFont = loadFont("CurlzMT-48.vlw")
    subTitleFont = loadFont("Garamond-Bold-20.vlw")
    textFont(titleFont)
    textSize(100)
    text("Picasso in a Day", 45, 80)
