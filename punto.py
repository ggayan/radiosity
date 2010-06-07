import math

class Punto:

    def __init__(self,x1,y1,z1):
        self.x = x1
        self.y = y1
        self.z = z1
    
        #w es el factor de correcion
    def suma(self, p2, w):
        if w == 0:
            w = 1
        
        x = (self.x + p2.x) / w
        y = (self.y + p2.y) / w
        z = (self.z + p2.z) / w
        return Punto(x, y, z)
    
    #w es el factor de correcion
    def resta(self, p2, w):
        if w == 0:
            w = 1
        
        x = (self.x - p2.x) / w
        y = (self.y - p2.y) / w
        z = (self.z - p2.z) / w
        return Punto(x, y, z)
        
    def cruz(self, p2):
        #calculo los puntos segun la notacion matricial
        x = self.y * p2.z - self.z * p2.y
        y = self.z * p2.x - self.x * p2.z
        z = self.x * p2.y - self.y * p2.x
        #y lo retornamos como punto
        return Punto(x, y, z)
        
    # producto punto entre dos Puntos, como si fueran vectores
    def producto(self,p2):
        sx = self.x*p2.x
        sy = self.y*p2.y
        sz = self.z*p2.z
        
        return sx+sy+sz
        
    # modulo de Punto, como si fuera un vector
    def modulo(self):
        aux = math.sqrt(self.producto(self))
        # print aux
        return aux
    
    def imprimir(self, name):
        x = self.x
        y = self.y
        z = self.z
        
        print name + ": x = {0}, y = {1}, z = {2}".format(x, y, z)
        
    # calcula angulo entre dos puntos, como si fueran vectores
    def anguloEntre(self,p2):
        v = self
        w = p2
        acosval = (v.producto(w))/(v.modulo()*w.modulo())
        if( acosval < -1):
            acosval = -1
        if( acosval > 1 ):
            acosval = 1
        theta = math.acos(acosval)
        return theta
    
    def normalizar(self):
        mod = self.modulo()
        return Punto(self.x/mod , self.y/mod , self.z/mod)