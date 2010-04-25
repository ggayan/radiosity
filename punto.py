class Punto:

    def __init__(self,x1,y1,z1):
        self.x = x1
        self.y = y1
        self.z = z1
        
def cruz(p1, p2):
    #calculo los puntos segun la notacion matricial
    x = p1.y * p2.z - p1.z * p2.y
    y = p1.z * p2.x - p1.x * p2.z
    z = p1.x * p2.y - p1.y * p2.x
    #y lo retornamos como punto
    return Punto(x, y, z)
