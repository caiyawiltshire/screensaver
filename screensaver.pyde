x = 0
def setup():
    size (536,1218)
    background (230, 196, 64)
    
def draw():
    global x
    if x % 50 == 0:
        while x <= 550:
            y = 0
            noLoop()
            while y <= 1250:
                fill (0,0,random(255))
                rect (x,y,50,100)
                y += 100
            x += 50
       
        
