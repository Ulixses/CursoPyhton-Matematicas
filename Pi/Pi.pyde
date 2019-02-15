radio = 600
total = 0
circulo = 0

def setup():
    size(radio * 2,radio * 2)
    background(255,255, 0)
    fill(255,100,100)
    #ellipse(height/2,width/2,radio*2,radio*2)
    frameRate(360)
    
def draw():
    global total,circulo

    for x in range(100000):
        Rx = random(radio*2)
        Ry = random(radio*2)
        point(Rx,Ry)
        distancia = pow(radio - Rx, 2) + pow(radio - Ry, 2)
        total += 1
        if (distancia <= radio * radio):
            circulo = circulo + 1
            stroke(0,255,0)
        else:
            stroke(255,0,0)
            
        point(Rx,Ry)
    println(float(circulo)/total * float(4))
    
