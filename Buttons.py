def finishedButton():
    font = loadFont("ArialMT-10.vlw")
    strokeWeight(1)
    rect(630,20,50,50)
    textFont(font)
    textSize(10)
    fill(0)
    text("Finished",635,50)

def nextPage():
    font = loadFont("ArialMT-10.vlw")
    strokeWeight(1)
    noFill()
    rect(560,20,50,50)
    textFont(font)
    textSize(10)
    fill(0)
    text("Next",574,50)
