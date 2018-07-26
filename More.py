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
    
      #Ladybug Box
    penguin = loadImage("penguin.PNG")
    stroke(0)
    rect(40.5,129,151,151)
    image(penguin,41.5,130,150,150)
    textFont(subTitleFont)
    textSize(25)
    fill(51, 175, 255)
    text("Larry the Ladybug",37,315)
    
    #Robot Box
    robot = loadImage("robot.png")
    stroke(0)
    rect(273.5,129,151,151)
    image(robot,274.5,130,150,150)
    textFont(subTitleFont)
    text("Mr. Tin Man",250,315)
    
    #Snowman Box
    snowman = loadImage("snowman.png")
    stroke(0)
    rect(506.5,129,151,151)
    image(snowman,507.5,130,150,150)
    textFont(subTitleFont)
    text("Frosty",550,315)
    
    #Bee Box
    rainbow = loadImage("rainbow.png")
    stroke(0)
    rect(40.5,344,151,151)
    image(rainbow,41.5,345,150,150)
    textFont(subTitleFont)
    text("Buzzy Bee",37,530)
    
    # back button
    stroke(0)
    fill(255)
    rect(273.5,344,151,151)
    fill(0)
    triangle(380, 370,
             380, 470,
             300, 420)
    fill(51, 175, 255)
    textFont(subTitleFont)
    text("Back",280,530)
    
