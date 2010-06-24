from punto import *
from patch import *
from variables import *

def patchesCubo(origin,lengthx,lengthy,lengthz,lum,color):
    
    patchesCubo = []
    
    iterationsx = (int)(SECTIONS*lengthx)
    iterationsy = (int)(SECTIONS*lengthy)
    iterationsz = (int)(SECTIONS*lengthz)
    
    x0 = origin.x
    y0 = origin.y
    z0 = origin.z
    
    for i in xrange(0, iterationsx): #eje horizonal
        for j in xrange(0, iterationsy): #eje vertical
            
            patch = None # variable temporal para cada patch
            
            p1 = Punto(x0, y0, z0)
            p2 = Punto(x0 + step, y0, z0)
            p3 = Punto(x0, y0 + step, z0)
            p4 = Punto(x0 + step, y0 + step, z0)
            patch = Patch(p3, p4, p2, p1)
            y0 += step
                
            patch.reflectance_red = color[0]
            patch.reflectance_green = color[1]
            patch.reflectance_blue = color[2]
            # asocio el parche recien creado a la lista
            patchesCubo.append(patch)
        x0 += step
        y0 = origin.y
    #planoXZ
    x0 = origin.x
    y0 = origin.y
    z0 = origin.z
    
    for i in xrange(0, iterationsx): #eje horizonal
        for j in xrange(0, iterationsz): #eje vertical
            
            patch = None # variable temporal para cada patch
            
            p1 = Punto(x0, y0, z0)
            p2 = Punto(x0, y0, z0 + step)
            p3 = Punto(x0 + step, y0, z0)
            p4 = Punto(x0 + step, y0, z0 + step)
            patch = Patch(p3, p4, p2, p1)
            z0 += step
                
            patch.reflectance_red = color[0]
            patch.reflectance_green = color[1]
            patch.reflectance_blue = color[2]
            # asocio el parche recien creado a la lista
            patchesCubo.append(patch)
        x0 += step
        z0 = origin.z
        
        ############################################################
    x0 = origin.x
    y0 = origin.y
    z0 = origin.z
    
    for i in xrange(0, iterationsx): #eje horizonal
        for j in xrange(0, iterationsy): #eje vertical
            
            patch = None # variable temporal para cada patch
            
            p1 = Punto(x0, y0, z0+lengthz)
            p2 = Punto(x0 + step, y0, z0+lengthz)
            p3 = Punto(x0, y0 + step, z0+lengthz)
            p4 = Punto(x0 + step, y0 + step, z0+lengthz)
            patch = Patch(p1, p2, p4, p3)
            y0 += step
                
            patch.reflectance_red = color[0]
            patch.reflectance_green = color[1]
            patch.reflectance_blue = color[2]
            # asocio el parche recien creado a la lista
            patchesCubo.append(patch)
        x0 += step
        y0 = origin.y
        
    #planoYZ
    x0 = origin.x
    y0 = origin.y
    z0 = origin.z
    
    for i in xrange(0, iterationsz): #eje horizonal
        for j in xrange(0, iterationsy): #eje vertical
            
            patch = None # variable temporal para cada patch
            
            p1 = Punto( x0+lengthx, y0, z0)
            p2 = Punto( x0+lengthx, y0 + step, z0)
            p3 = Punto( x0+lengthx, y0, z0 + step)
            p4 = Punto( x0+lengthx, y0 + step, z0 + step)
            patch = Patch(p1, p2, p4, p3)
            y0 += step
                
            patch.reflectance_red = color[0]
            patch.reflectance_green = color[1]
            patch.reflectance_blue = color[2]
            # asocio el parche recien creado a la lista
            patchesCubo.append(patch)
        z0 += step
        y0 = origin.y
        
    #planoXZ
    x0 = origin.x
    y0 = origin.y
    z0 = origin.z
    
    for i in xrange(0, iterationsx): #eje horizonal
        for j in xrange(0, iterationsz): #eje vertical
            
            patch = None # variable temporal para cada patch
            
            p1 = Punto(x0, y0+lengthy, z0)
            p2 = Punto(x0, y0+lengthy, z0 + step)
            p3 = Punto(x0 + step, y0+lengthy, z0)
            p4 = Punto(x0 + step, y0+lengthy, z0 + step)
            patch = Patch(p1, p2, p4, p3)
            z0 += step
                
            patch.reflectance_red = color[0]
            patch.reflectance_green = color[1]
            patch.reflectance_blue = color[2]
            # asocio el parche recien creado a la lista
            patchesCubo.append(patch)
        x0 += step
        z0 = origin.z
        
    #planoYZ
    x0 = origin.x
    y0 = origin.y
    z0 = origin.z
    
    for i in xrange(0, iterationsz): #eje horizonal
        for j in xrange(0, iterationsy): #eje vertical
            
            patch = None # variable temporal para cada patch
            
            p1 = Punto( x0, y0, z0)
            p2 = Punto( x0, y0 + step, z0)
            p3 = Punto( x0, y0, z0 + step)
            p4 = Punto( x0, y0 + step, z0 + step)
            patch = Patch(p3, p4, p2, p1)
            y0 += step
                
            patch.reflectance_red = color[0]
            patch.reflectance_green = color[1]
            patch.reflectance_blue = color[2]
            # asocio el parche recien creado a la lista
            patchesCubo.append(patch)
        z0 += step
        y0 = origin.y
        
    for patch in patchesCubo:
    	patch.oclussion = True
	return patchesCubo
    
