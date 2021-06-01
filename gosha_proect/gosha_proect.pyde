x = 300
y = 300
k = 0
def setup():
    size(1400,700)
    frameRate(50)

def draw():
    global k
    background (255)
    k=k+20   
    shar = loadImage('sharic.png')
    fon = loadImage('10.jpg')
    image (fon , 0,0,1500,700)
    push()
    translate(x,y)
    rotate(radians(k))  
    image (shar, -65/2, -50/2,135/1.5,100/1.5) 
    pop()


def keyPressed():
    global x, y
    if key == "w":
        y=y-10
    if key == "s":
        y=y+10
    if key == "a":
        x=x-10
    if key == "d":
        x=x+10
