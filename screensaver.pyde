x = 0
def setup():
    size (536,1218)
    background (230, 196, 64)
    
def draw():
    global x
    if x % 50 == 0:
        noStroke()
        while x <= 550:
            y = 0
            noLoop()
            while y <= 1250:
                fill (255,random(225,240),random(0,125))
                rect (x,y,50,100)
                y += 100
            x += 50
    textSize (60)
    fill (76,136,245)
    text ("G", 150,400)
    textSize (60)
    fill (222,82,70)
    text ("O", 200,400)
    textSize (60)
    fill (255,206,68)
    text ("O", 250,400)
    textSize (60)
    fill (76,136,245)
    text ("G", 300,400)
    textSize (60)
    fill (26,162,96)
    text ("L", 350,400)
    textSize (60)
    fill (222,82,70)
    text ("E", 400,400)
