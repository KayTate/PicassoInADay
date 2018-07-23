def titlePage():
    background(255)
    
    #Header
    fill("#CA7AE0")
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
    
    #Ice Cream Box
    iceCream = loadImage("icecream.png")
    stroke(0)
    rect(273.5,199,151,151)
    image(iceCream,274.5,200,150,150)
