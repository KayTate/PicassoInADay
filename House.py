def house():
    
    size(500,500)
    background(255)
    fill(255)
    ellipse(0,0,200,200)              #sun
    fill(255)
    rect(0, 400, 500, 100)            #grass
    fill(255)
    rect(260,175,230,260)             #house
    fill(255)
    triangle(260,175,375,10,490,175) #roof
    fill(255)
    rect(340,300,50,125)              #door
    fill(255)
    ellipse(380,370,10,10)            #door handle
    stroke(0,0,0)
    fill(255)
    rect(270,240,55,60)               #window 1
    rect(404,240,55,60)               #window 2
    line(297,240,297,300)             #window1 vline
    line(431,240,431,300)             #window2 vline
    line(270,270,325,270)             #window1 hline
    line(404,270,459,270)             #window2 hline
