from OpenGL.GL import glVertex3f
import math

#implementado como triangulo
class Patch:

    #x = 0
    #y = 0
    #z = 0
    rr = 0  # reflectividad roja
    er = 0  # emisividad roja
    rv = 0  # reflectividad verde
    ev = 0  # emisividad verde
    rb = 0  # reflectividad azul
    eb = 0  # emisividad azul

    def __init__(self,p1,p2,p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.nr = self.normal()
        self.cn = self.center()
        self.ar = self.area()

    #retorna el baricentro del parche
    def center(self):
        #x = (self.p1.x + self.p2.x + self.p3.x) / 3
        #y = (self.p1.y + self.p2.y + self.p3.y) / 3
        #z = (self.p1.z + self.p2.z + self.p3.z) / 3
        
        #return Punto(x, y, z)
        return self.p1.suma(self.p2.suma(self.p3,1),3) # == (p1 + ((p2 + p3) / 1)) / 3
        
    #no es necesario normalizar, basta la direccion
    def normal(self):
        b_menos_a = self.p2.resta(self.p1, 1) # == (p2 - p1) / 1
        c_menos_a = self.p3.resta(self.p1, 1) # == (p3 - p1) / 1
        return b_menos_a.cruz(c_menos_a)
    
    def area(self):
        p1 = self.p1
        p2 = self.p2
        p3 = self.p3

        lado1 = math.sqrt(math.pow(p1.x-p2.x,2)+math.pow(p1.y-p2.y,2)+math.pow(p1.z-p2.z,2)) #p1, p2
        lado2 = math.sqrt(math.pow(p3.x-p2.x,2)+math.pow(p3.y-p2.y,2)+math.pow(p3.z-p2.z,2)) #p2, p3
        lado3 = math.sqrt(math.pow(p1.x-p3.x,2)+math.pow(p1.y-p3.y,2)+math.pow(p1.z-p3.z,2)) #p3, p1
        s = 0.5*(lado1 + lado2 + lado3)
        
        return math.sqrt(s*(s-lado1)*(s-lado2)*(s-lado3))
    
    #atajo para dibujar cada patch
    def dibujar(self):
        p1 = self.p1
        p2 = self.p2
        p3 = self.p3
        glVertex3f(p1.x, p1.y, p1.z)
        glVertex3f(p2.x, p2.y, p2.z)
        glVertex3f(p3.x, p3.y, p3.z)
