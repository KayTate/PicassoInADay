def titlePage():
    background(255)
    
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
    rect(40.5,199,151,151)
    image(penguin,41.5,200,150,150)
    textSize(25)
    text("Polly the Penguin",37,385)
    
    #Ice Cream Box
    iceCream = loadImage("icecream.png")
    stroke(0)
    rect(273.5,199,151,151)
    image(iceCream,274.5,200,150,150)
    text("World's Best Ice Cream",243,385)
    
    #Lollipop Box
    lollipop = loadImage("lollipop.png")
    stroke(0)
    rect(506.5,199,151,151)
    image(lollipop,507.5,200,150,150)
    text("Lollipop Land",520,385)
