import math


def DibPelota(x,y):
    ellipseMode(RADIUS)
    fill(255)
    ellipse(x,y,4,4)
def DibRaquetaYo(x,y):
    rectMode(RADIUS)
    fill(255)
    rect(x,y,3,15)
def DibRaquetaOtro(x,y):
    rectMode(RADIUS)
    fill(255)
    rect(x,y,3,15)
def ModRaqYo(vely , y):
    y = y + vely
    return y
def ModRaqOtro(vely , y):
    y = y + vely
    return y
def VelRaqueta1():
    if (keyPressed):
        if(key == 's'):
            return 1
        elif(key== 'w'):
            return -1
        else:
            return 0
        
    else:
        return 0
def VelRaqueta2(y,pelotay):
    if(pelotay > y):
        return 1
    elif(pelotay<y):
        return -1
    else:
        return 0

def VelPelotaY(x,y,xraqueta1,yraqueta1,xraqueta2,yraqueta2,alto,velY):
    if(x - 4 <= xraqueta1 and y <= yraqueta1 + 15 and y >= yraqueta1 - 15 ):
        return randint(-5,5)
    elif(x + 4 >= xraqueta2 and y <= yraqueta2 + 15 and y >= yraqueta2 - 15):
        return randint(-5,5)
    if (y - 3 <= 0):
        return velY*(-1)
    elif((y + 3 )>= alto ):
        return velY*(-1)
    return velY
def VelPelotaX(x,y,xraqueta1,yraqueta1,xraqueta2,yraqueta2,velX):
    if(x - 4 <= xraqueta1 and y <= yraqueta1 + 15 and y >= yraqueta1 - 15 ):
        return 5
    elif(x + 4 >= xraqueta2 and y <= yraqueta2 + 15 and y >= yraqueta2 - 15):
        return -5
    else:
        return velX
def PelotaX(x,velx = 1):
    x = x + velx
    return x
def PelotaY(y,vely):
    print(vely)
    y = y + vely  
    print(y)  
    return y 
    
    
    
