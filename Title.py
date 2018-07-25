# img = loadImage("Star-Transparent-PNG.png")

def titlePage():
    img = loadImage("stripes.png")
    background(255)
    image(img, 0, 0, 700, 550)
    #Header
    fill("#8AA8E8")
    noStroke()
    rect(0,0,700,100)
    
    fill(0)
    titleFont = loadFont("CurlzMT-48.vlw")
    textFont(titleFont)
    textSize(100)
    text("Picasso in a Day", 45, 80)
    
    
    #Penguin Box
    penguin = loadImage("penguin.PNG")
    stroke(0)
    rect(40.5,129,151,151)
    image(penguin,41.5,130,150,150)
    textSize(25)
    text("Polly the Penguin",37,315)
    
    #Ice Cream Box
    iceCream = loadImage("icecream.png")
    stroke(0)
    rect(273.5,129,151,151)
    image(iceCream,274.5,130,150,150)
    text("World's Best Ice Cream",243,315)
    
    #Lollipop Box
    lollipop = loadImage("lollipop.png")
    stroke(0)
    rect(506.5,129,151,151)
    image(lollipop,507.5,130,150,150)
    text("Lollipop Land",520,315)
    
    #Rainbow Box
    rainbow = loadImage("rainbow.png")
    stroke(0)
    rect(40.5,344,151,151)
    image(rainbow,41.5,345,150,150)
    text("Mysticla Rainbow",37,530)
    
    #House Box
    house = loadImage("house.png")
    stroke(0)
    rect(273.5,344,151,151)
    image(house,274.5,345,150,150)
    text("Castle of Magic",280,530)
