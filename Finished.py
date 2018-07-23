def finished():
    background(255)
    i = 0
    
    frame1 = loadImage("frame_000")
    frame2 = loadImage("frame_001")
    frame3 = loadImage("frame_002")
    frame4 = loadImage("frame_003")
    frame5 = loadImage("frame_004")
    frame6 = loadImage("frame_005")
    frame7 = loadImage("frame_006")
    frame8 = loadImage("frame_007")
    frame9 = loadImage("frame_008")
    frame10 = loadImage("frame_009")
    frame11 = loadImage("frame_010")
    
    while i < 10:
        image(frame1,0,0,700,550)
        image(frame2,0,0,700,550)
        image(frame3,0,0,700,550)
        image(frame4,0,0,700,550)
        image(frame5,0,0,700,550)
        image(frame6,0,0,700,550)
        image(frame7,0,0,700,550)
        image(frame8,0,0,700,550)
        image(frame9,0,0,700,550)
        image(frame10,0,0,700,550)
        image(frame11,0,0,700,550)
        i += 1
