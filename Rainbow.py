from colorSpace import *

def rainbow():
    cloud = loadShape("cloud.svg")       #Loads shape for cloud
    
    colorBox()
    
    shape(cloud, 100, 300, 280, 200)
    shape(cloud, 415, 300, 280, 200)
    
    stroke(0)
    strokeWeight(7)
    arc(395, 440, 571, 754,              #Ellipse Definition
        PI+.0505, 2*PI-.09, OPEN)        #Arc Definition
    arc(395, 440, 500, 660,
        PI+.202, 2*PI-.19, OPEN)
    arc(395, 440, 429, 566,
        PI+.278, 2*PI-.35, OPEN)
    arc(395, 440, 358, 472,
        PI+.428, 2*PI-.43, OPEN)
    arc(395, 440, 287, 378,
        PI+.55, 2*PI-.43, OPEN)
    arc(395, 440, 216, 284,
        PI+.67, 2*PI-.55, OPEN)
    arc(395, 440, 145, 190,
        PI+.460, 2*PI-.55, OPEN)
    arc(395, 440, 74, 96,
        PI+.60, 2*PI-.55, OPEN)
