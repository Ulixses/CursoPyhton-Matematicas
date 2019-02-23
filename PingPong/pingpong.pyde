import objetos
Raqueta1Y = 0 
Raqueta1X = 0
VelRaqueta1Y = 1  
XPelota = 0
YPelota =  0
VelPelotaX = 0
VelPelotaY = 0
Raqueta2Y = 0
Raqueta2X = 0
VelRaqueta2Y = 0
def setup():
    size(924,520)
    global Raqueta1Y,Raqueta1X,VelRaqueta1Y,XPelota,YPelota,VelPelotaX,VelPelotaY,Raqueta2Y,Raqueta2X,VelRaqueta2Y
    XPelota = width/2
    YPelota = height/2
    VelPelotaX = -5
    VelPelotaY = 0
    Raqueta1Y = height/2  
    Raqueta1X = 4
    VelRaqueta1Y = 0 
    Raqueta2Y = height/2  
    Raqueta2X = width-4
    VelRaqueta1Y = 0   
def draw():
    fill(0) 
    rect(0,0,width,height)
    global Raqueta1Y,Raqueta1X,VelRaqueta1Y,XPelota,YPelota,VelPelotaX,VelPelotaY,Raqueta2Y,Raqueta2X,VelRaqueta2Y
    VelRaqueta1Y = objetos.VelRaqueta1()
    VelRaqueta2Y = objetos.VelRaqueta2(Raqueta2Y,YPelota)
    Raqueta2Y = objetos.ModRaqOtro(VelRaqueta2Y,Raqueta2Y)
    Raqueta1Y = objetos.ModRaqYo(VelRaqueta1Y,Raqueta1Y)
    VelPelotaX = objetos.VelPelotaX(XPelota,YPelota,Raqueta1X,Raqueta1Y,Raqueta2X,Raqueta2Y,VelPelotaX)
    VelPelotaY = objetos.VelPelotaY(XPelota,YPelota,Raqueta1X,Raqueta1Y,Raqueta2X,Raqueta2Y,height,VelPelotaY)
    XPelota = objetos.PelotaX(XPelota,VelPelotaX)
    YPelota = objetos.PelotaY(YPelota,VelPelotaY)
    stroke(255)
    line(width/2,0,width/2,height)
    objetos.DibPelota(XPelota,YPelota)
    objetos.DibRaquetaYo(Raqueta1X,Raqueta1Y)
    objetos.DibRaquetaOtro(Raqueta2X,Raqueta2Y)
    print(Raqueta1Y,Raqueta1X,VelRaqueta1Y,"pelotax",XPelota,"pelotay",YPelota,"velpelotax",VelPelotaX,"velpelotay",VelPelotaY,Raqueta2Y,Raqueta2X,VelRaqueta2Y)
   
