def titlePage():
    #Background
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
    
    #Penguin Box
    penguin = loadImage("penguin.PNG")
    stroke(0)
    rect(40.5,129,151,151)
    image(penguin,41.5,130,150,150)
    textFont(subTitleFont)
    textSize(25)
    fill(51, 175, 255)
    text("Polly the Penguin",37,315)
    
    #Ice Cream Box
    iceCream = loadImage("icecream.png")
    stroke(0)
    rect(273.5,129,151,151)
    image(iceCream,274.5,130,150,150)
    textFont(subTitleFont)
    text("World's Best Ice Cream",243,315)
    
    #Lollipop Box
    lollipop = loadImage("lollipop.png")
    stroke(0)
    rect(506.5,129,151,151)
    image(lollipop,507.5,130,150,150)
    textFont(subTitleFont)
    text("Lollipop Land",520,315)
    
    #Rainbow Box
    rainbow = loadImage("rainbow.png")
    stroke(0)
    rect(40.5,344,151,151)
    image(rainbow,41.5,345,150,150)
    textFont(subTitleFont)
    text("Mysticla Rainbow",37,530)
    
    #House Box
    house = loadImage("house.png")
    stroke(0)
    rect(273.5,344,151,151)
    image(house,274.5,345,150,150)
    textFont(subTitleFont)
    text("Castle of Magic",280,530)
    
    #More Box
    stroke(0)
    fill(255)
    rect(506.5,345,151,151)
    fill(0)
    triangle(540, 370,
             540, 470,
             620, 420)
    fill(51, 175, 255)
    text("More Drawings",520,530)
