from OpenGL.GL import glVertex3f
import math
from variables import *

#implementado como triangulo
class Patch:

    reflectance_red = 0.0  # reflectividad roja
    reflectance_green = 0.0  # reflectividad verde
    reflectance_blue = 0.0  # reflectividad azul
    
    emmision_red = 0.0  # emisividad roja
    emmision_green = 0.0  # emisividad verde
    emmision_blue = 0.0  # emisividad azul
    
    excident_red = 0.0  # color (luz excedente) roja
    excident_green = 0.0  # color (luz excedente) verde
    excident_blue = 0.0  # color (luz excedente) azul
    
    incident_red = 0.0  # luz incidente roja
    incident_green = 0.0  # luz incidente verde
    incident_blue = 0.0  # luz incidente azul

    #los puntos del parche deben especificarse en orden (antihorario=>normal +).
    #en teoria debieran ser coplanares
    def __init__(self,p1,p2,p3,p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.normal = self._normal()
        self.center = self._center()
        self.area = self._area()
        self.pradio = self._pradio()
        self.pmradio = self._pmradio()
        self.oclussion = False
        
    #retorna el baricentro del parche
    def _center(self):
        return self.p1.suma(self.p3,2) # punto medio entre vertices opuestos
        
    def _normal(self):
        b_menos_a = self.p2.resta(self.p1, 1) # == (p2 - p1) / 1
        c_menos_a = self.p3.resta(self.p1, 1) # == (p3 - p1) / 1
        if(b_menos_a.modulo() == 0 or c_menos_a.modulo()==0):
            print " normal es cero"
        cruz = b_menos_a.cruz(c_menos_a)
        return cruz.normalizar()
    
    def _area(self):
        p1 = self.p1
        p2 = self.p2
        p3 = self.p3
        p4 = self.p4

        lado1 = math.sqrt(math.pow(p1.x-p2.x,2)+math.pow(p1.y-p2.y,2)+math.pow(p1.z-p2.z,2)) #p1, p2
        lado2 = math.sqrt(math.pow(p3.x-p2.x,2)+math.pow(p3.y-p2.y,2)+math.pow(p3.z-p2.z,2)) #    p2, p3
        # lado3 = math.sqrt(math.pow(p1.x-p3.x,2)+math.pow(p1.y-p3.y,2)+math.pow(p1.z-p3.z,2)) #p1,     p3
        # lado4 = math.sqrt(math.pow(p3.x-p4.x,2)+math.pow(p3.y-p4.y,2)+math.pow(p3.z-p4.z,2)) #        p3, p4
        # lado5 = math.sqrt(math.pow(p1.x-p4.x,2)+math.pow(p1.y-p4.y,2)+math.pow(p1.z-p4.z,2)) #p1,         p4
        # s1 = 0.5*(lado1 + lado2 + lado3)
        # s2 = 0.5*(lado4 + lado5 + lado3)
        # s1 = 0.5*(lado1 + lado2 + lado3)
        # s2 = 0.5*(lado4 + lado5 + lado3)
        # return math.sqrt(s1*(s1-lado1)*(s1-lado2)*(s1-lado3)) + math.sqrt(s2*(s2-lado4)*(s2-lado5)*(s2-lado3))
        return lado1*lado2
    
    #atajo para dibujar cada patch
    def draw(self):
        p1 = self.p1
        p2 = self.p2
        p3 = self.p3
        p4 = self.p4
        glVertex3f(p1.x, p1.y, p1.z)
        glVertex3f(p2.x, p2.y, p2.z)
        glVertex3f(p3.x, p3.y, p3.z)
        glVertex3f(p4.x, p4.y, p4.z)
        
    # retorna el radio de la circunferencia circunscrita
    def _pradio(self):
        # d1 = self.center.resta(self.p1,1).modulo()
        # d2 = self.center.resta(self.p2,1).modulo()
        # d3 = self.center.resta(self.p3,1).modulo()
        # d4 = self.center.resta(self.p4,1).modulo()
        # return max(d1,d2,d3,d4)
        return (1/SECTIONS)*0.5*(2**0.5)
        
    # retorna el radio de la circunferencia inscrita
    def _pmradio(self):
        d1 = self.center.resta(self.p1,1).modulo()
        d2 = self.center.resta(self.p2,1).modulo()
        d3 = self.center.resta(self.p3,1).modulo()
        d4 = self.center.resta(self.p4,1).modulo()
        return max(d1,d2,d3,d4)*0.5*(2**0.5)
#        return min(d1,d2,d3,d4)
