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
