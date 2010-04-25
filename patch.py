from punto import *

#implementado como triangulo
class Patch:

    #x = 0
    #y = 0
    #z = 0
    r = 0  # reflectividad
    e = 0  # emisividad

    def __init__(self,p1,p2,p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    #retorna el baricentro del parche
    def center(self):
        x = (self.p1.x + self.p2.x + self.p3.x) / 3
        y = (self.p1.y + self.p2.y + self.p3.y) / 3
        z = (self.p1.z + self.p2.z + self.p3.z) / 3
        
        return Punto(x, y, z)
        
    def normal(self):
        return cruz(self.p1, self.p2)
