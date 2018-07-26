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
    
def savePicture(rColor,gColor,bColor):
    font = loadFont("ArialMT-48.vlw")
    strokeWeight(1)
    fill(rColor,gColor,bColor)
    rect(560,480,120,50)
    textFont(font)
    textSize(48)
    fill(0)
    text("Save",565,523)
