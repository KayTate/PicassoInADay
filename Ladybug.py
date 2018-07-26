from colorSpace import *

#Functions to draw spots
def bigDot(xCoordinate, yCoordinate):
    ellipse(xCoordinate, yCoordinate, 75, 75)
def smallDot(xCoordinate, yCoordinate):
    ellipse(xCoordinate, yCoordinate, 25, 25)

def ladybug():
    colorBox()
    
    fill(255)
    
    arc(400,350,350,350,PI, 2*PI, CLOSE) #Body
    
    ellipse(575,300,100,100)             #Head
    
    ellipse(560,280,25,25)               #Eyes
    ellipse(590,280,25,25)
    
    arc(540,180,25,25,PI/1.7,2*PI)       #Left Antenna
    ellipse(537,192,5,5)
    line(552,179,566,251)
    
    arc(610,180,25,25,PI,2.5*PI)        #Right Antenna
    ellipse(613,192,5,5)
    line(597,179,584,251)
    
    bigDot(312,260)                     #Spots
    bigDot(460,295)
    smallDot(440,206)
    smallDot(386,280)
    smallDot(267,326)
    
    fill(0)                             #Pupils
    ellipse(560,280,10,10)
    ellipse(590,280,10,10)
    
    noFill()
    strokeWeight(2)
    arc(575,310,75,50,0,PI)             #Smile
    
    line(263,350,276,371)               #Legs
    line(276,371,271,392)
    ellipse(276,392,10,5)
    
    line(288,350,301,371)
    line(301,371,296,392)
    ellipse(301,392,10,5)
    
    line(463,350,476,371)
    line(476,371,471,392)
    ellipse(476,392,10,5)
    
    line(488,350,501,371)
    line(501,371,496,392)
    ellipse(501,392,10,5) 
    
    strokeWeight(1)
