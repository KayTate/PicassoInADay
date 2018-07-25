from colorSpace import *

def house():

    colorBox()
    fill(255)
    stroke(0)
    
    rect(100, 400, 595, 145)          #grass
    rect(360,175,230,260)             #house
    triangle(360,175,475,10,590,175)  #roof
    rect(440,300,50,125)              #door
    ellipse(480,370,10,10)            #door handle
    rect(370,240,55,60)               #window 1
    rect(504,240,55,60)               #window 2
    line(397,240,397,300)             #window1 vline
    line(531,240,531,300)             #window2 vline
    line(370,270,425,270)             #window1 hline
    line(504,270,559,270)             #window2 hline
