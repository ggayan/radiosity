from OpenGL.GL import glVertex3f
import math

#implementado como triangulo
class Patch:

    rr = 0  # reflectividad roja
    rg = 0  # reflectividad verde
    rb = 0  # reflectividad azul
    
    er = 0  # emisividad roja
    eg = 0  # emisividad verde
    eb = 0  # emisividad azul
    
    cr = 0  # color (luz excedente) roja
    cg = 0  # color (luz excedente) verde
    cb = 0  # color (luz excedente) azul
    
    ir = 0  # luz incidente roja
    ig = 0  # luz incidente verde
    ib = 0  # luz incidente azul

    def __init__(self,p1,p2,p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.nr = self.normal()
        self.cn = self.center()
        self.ar = self.area()
        self.pr = self.pradio()

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
        cruz = b_menos_a.cruz(c_menos_a)
        mod = math.sqrt(cruz.x*cruz.x + cruz.y*cruz.y + cruz.z*cruz.z)
        cruz.x = cruz.x/mod
        cruz.y = cruz.y/mod
        cruz.z = cruz.z/mod
        
        return cruz
    
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
        
    # retorna el radio de la circunferencia circunscrita
    def pradio(self):
        d1 = self.cn.resta(self.p1,1).modulo()
        d2 = self.cn.resta(self.p2,1).modulo()
        d3 = self.cn.resta(self.p3,1).modulo()
        return max(d1,d2,d3)
