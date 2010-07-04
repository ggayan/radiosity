from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from numpy import *

import Image
import cPickle
import os
import sys
import math
import time

from time import gmtime, strftime

from patch import *
from punto import *
from functions import *
from cuerpos import *
from variables import *

def init(width, height):              
    global FormFactors
    global Visibilidad
    ITIME = time.time()
    
    #llamo la funcion que genera los planos
    generarPlanos()
    
    #llamo a la funcion que aniade cuerpos a la escena
    generarCuerpos()
    
    # generamos las fuentes luminosas
    aniadirFuentesLuminosas()
    
    # ajuste de parametros de luz
    cambiarLuminosidad()
    
    # FormFactors = [[-1 for col in range(len(patchesList))] for row in range(len(patchesList))]
    # Visibilidad = [[-1 for col in range(len(patchesList))] for row in range(len(patchesList))]
    FormFactors = [[-1]*len(patchesList) for row in range(len(patchesList))]
    Visibilidad = [[-1]*len(patchesList) for row in range(len(patchesList))]
        
    print strftime("%a, %d %b %Y %H:%M:%S ", gmtime(time.time()-3600*4))
    if( VSB == 1):
        print "Computar Visibilidades"
        computeVisibilidad()
    else:
        print "Cargar Visibilidades"
        loadVisibilidad()
    print "OK visibilidades"
    if( FFT == 1):
        print "Computar FormFactors"
        computeFormFactors()
    else:
        print "Cargar FormFactors"
        loadFormFactors()
    print "OK FormFactors"
    print "Ejecutar ",shoots," iteraciones"
    RadiosityIteration(shoots)

    print "segundos= ",time.time()-ITIME
    print strftime("%a, %d %b %Y %H:%M:%S", gmtime(time.time()-3600*4))

    LoadTextures()
    glEnable(GL_TEXTURE_2D) 
    glClearColor(0.0, 0.0, 0.0, 0.0)    # Color negro, sin transparencia
    
    glClearDepth(1.0)                   # Enables Clearing Of The Depth Buffer
    glDepthRange(0.0, 0.85)
    glDepthFunc(GL_LESS)                # The Type Of Depth Test To Do
    glEnable(GL_DEPTH_TEST)             # Enables Depth Testing
    glShadeModel(GL_SMOOTH)             # Enables Smooth Color Shading
    glTexEnvf( GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE )
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()                    # Reset The Projection Matrix
                                        # Calculate The Aspect Ratio Of The Window
    gluPerspective(45.0, float(width) / float(height), 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)

# Callback al cambiar el tamanio de la escena
def ReSizeGLScene(width, height):
    
    if height == 0:
        height = 1        # previene dividir por cero

    # No importa por ahora
    glViewport(0, 0, width, height) 
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(width) / float(height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

# Lo que se dibujar'a
def DrawGLScene():
    
    # Limpiamos los buffers de la iteracion anterior
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    gluLookAt(VIEWPOINT_X, VIEWPOINT_Y, VIEWPOINT_Z,
              LOOK_AT_X, LOOK_AT_Y, LOOK_AT_Z,
              UP_VECTOR_X, UP_VECTOR_Y, UP_VECTOR_Z)
    
    #dibujo los ejes
    #axis()
    
    #dibujo el escenario
    escenario()
    #print formfactor(patchesList[0],patchesList[len(patchesList)-1])

    #  Intercambiamos los buffers. Ahora lo visible es lo que acabamos de dibujar.
    glutSwapBuffers()
    
#las figuras a dibujar
def escenario():
    
    glBegin(GL_QUADS)
    dibujarListaParches()
    glEnd()
    
#funcion que genera los planos a dibujar
def generarPlanos():
    
    #planoXY
    x0 = 0
    y0 = 0
    
    iterations = (int)(SECTIONS*size)
    
    for i in range(0, iterations): #eje horizonal
        for j in range(0, iterations): #eje vertical
            
            patch = None # variable temporal para cada patch
            
            p1 = Punto(x0, y0, 0.0)
            p2 = Punto(x0 + step, y0, 0.0)
            p3 = Punto(x0, y0 + step, 0.0)
            p4 = Punto(x0 + step, y0 + step, 0.0)
            patch = Patch(p1, p2, p4, p3)
            y0 += step
                
            patch.coords = 'XY'
            patch.reflectance_red = XY_reflectance_red
            patch.reflectance_green = XY_reflectance_green
            patch.reflectance_blue = XY_reflectance_blue
            # asocio el parche recien creado a la lista
            patchesList.append(patch)
        x0 += step
        y0 = 0
    
    #planoXZ
    x0 = 0
    z0 = 0
    
    for i in range(0, iterations): #eje horizonal
        for j in range(0, iterations): #eje vertical
            
            patch = None # variable temporal para cada patch
            
            p1 = Punto(x0, 0.0, z0)
            p2 = Punto(x0, 0.0, z0 + step)
            p3 = Punto(x0 + step, 0.0, z0)
            p4 = Punto(x0 + step, 0.0, z0 + step)
            patch = Patch(p1, p2, p4, p3)
            z0 += step
                
            patch.coords = 'XZ'
            patch.reflectance_red = XZ_reflectance_red
            patch.reflectance_green = XZ_reflectance_green
            patch.reflectance_blue = XZ_reflectance_blue
            # asocio el parche recien creado a la lista
            patchesList.append(patch)
        x0 += step
        z0 = 0
        
    #planoYZ
    y0 = 0
    z0 = 0
    
    for i in range(0, iterations): #eje horizonal
        for j in range(0, iterations): #eje vertical
            
            patch = None # variable temporal para cada patch
            
            p1 = Punto( 0.0, y0, z0)
            p2 = Punto( 0.0, y0 + step, z0)
            p3 = Punto( 0.0, y0, z0 + step)
            p4 = Punto( 0.0, y0 + step, z0 + step)
            patch = Patch(p1, p2, p4, p3)
            y0 += step
                
            patch.coords = 'YZ'
            patch.reflectance_red = YZ_reflectance_red
            patch.reflectance_green = YZ_reflectance_green
            patch.reflectance_blue = YZ_reflectance_blue
            # asocio el parche recien creado a la lista
            patchesList.append(patch)
        z0 += step
        y0 = 0

# funcion que llama a los metodos de cuerpos.py
def generarCuerpos():
    global patchesList
    patchesList.extend( patchesCubo( Punto(4,1,4) , 2.0 , 2.0 , 1.0 , 0.0 , [0.7,0.1,0.1]) )
    patchesList.extend( patchesCubo( Punto(1,0,1) , 1.0 , 1.0 , 1.0 , 0.0 , [0.7,0.7,0.1]) )
    # patchesList.extend( patchesCubo( Punto(4,1,4),2,2,1,0,[0.8,0.2,0.2]) )

def aniadirFuentesLuminosas():
    global patchesList
    global lightsList
    
    # fuente1 = Patch(Punto(5.0,4.0,4.0),Punto(4.0,5.0,4.0),Punto(4.0,4.0,5.0))
    fuente1 = Patch(Punto(5.5,4.0,12.0),Punto(5.5,4.5,12.0),Punto(5.0,4.5,12.0),Punto(5.0,4.0,12.0))
    # fuente2 = Patch(Punto(12.0,4.0,5.0),Punto(12.0,4.5,5.0),Punto(12.0,4.5,5.5),Punto(12.0,4.0,5.5))
    
    # bloqueo1 = Patch(Punto(2.0,2.0,2.0),Punto(2.0,2.0,1.5),Punto(2.5,1.5,2.0))
    # bloqueo1.reflectance_red = 0.2
    # bloqueo1.reflectance_green = 0.2
    # bloqueo1.reflectance_blue = 0.2
    # patchesList.append(bloqueo1)
    
    lightsList.append(fuente1)
    # lightsList.append(fuente2)
    
    # las amarramos a la lista de parches
    patchesList.extend(lightsList)

def cambiarLuminosidad():
    global lightsList
    
    for light in lightsList:
        light.emmision_red = INITINTEN+INTENSITY  #emisividad roja
        light.emmision_green = INITINTEN+INTENSITY  #emisividad verde
        light.emmision_blue = INITINTEN+INTENSITY  #emisividad azul
  
def loadVisibilidad():
    global Visibilidad
    Visibilidad = cPickle.load(open('visibilidad.dat', 'rb'))

def computeVisibilidad():
    global Visibilidad
    for x in xrange(0,len(patchesList)):
        for y in xrange(0,x+1):
            if(x == y):
                Visibilidad[x][y] = 1.0
            else:
                # Visibilidad[x][y] = visibility(x,y)
                Visibilidad[x][y] = visibility3(x,y)
    cPickle.dump(Visibilidad, open('visibilidad.dat', 'wb')) 

def getVisibilidad(i,j):
    if(Visibilidad[i][j] == -1):
        return Visibilidad[j][i]
    else:
        return Visibilidad[i][j]
 
def loadFormFactors():
    global FormFactors
    FormFactors = cPickle.load(open('formfactors.dat', 'rb'))
               
def computeFormFactors():
    global FormFactors
    for x, patch_1 in enumerate(patchesList):
        for y, patch_2 in enumerate(patchesList):
            FormFactors[x][y] = formfactor(x, y, getVisibilidad(x,y))
    cPickle.dump(FormFactors, open('formfactors.dat', 'wb'))

def getFormFactor(i,j):
    if(FormFactors[i][j] == -1):
        return FormFactors[j][i]
    else:
        return FormFactors[i][j]

def RadiosityIteration(iterations):
    for x in xrange(0,iterations):
        print "iteration ",x
        #shoot()
        collect()
        
def shoot():
    for index_x, patch_1 in enumerate(patchesList):
        for index_y, patch_2 in enumerate(patchesList):
            if( index_x == index_y):
                continue
            ff = getFormFactor(index_x, index_y)
            if(ff==0):
                continue
            patch_2.incident_red += patch_1.excident_red * ff
            patch_2.incident_green += patch_1.excident_green * ff
            patch_2.incident_blue += patch_1.excident_blue * ff
        # calculo de luz excedente (color) de cada parche
    for patch in patchesList:
        patch.excident_red = patch.emmision_red + patch.incident_red * patch.reflectance_red
        patch.excident_green = patch.emmision_green + patch.incident_green * patch.reflectance_green
        patch.excident_blue = patch.emmision_blue + patch.incident_blue * patch.reflectance_blue 
    
def collect():
    for index_x, patch_1 in enumerate(patchesList):
        aux_r = 0
        aux_g = 0
        aux_b = 0
        for index_y, patch_2 in enumerate(patchesList):
            ff = getFormFactor(index_x, index_y)
            if(ff==0):
                continue
            aux_r = aux_r + patch_2.excident_red * ff
            aux_g = aux_g + patch_2.excident_green * ff
            aux_b = aux_b + patch_2.excident_blue * ff
        patch_1.incident_red = aux_r
        patch_1.incident_green = aux_g
        patch_1.incident_blue = aux_b
        
    # calculo de luz excedente (color) de cada parche
    for patch in patchesList:
        patch.excident_red = patch.emmision_red + patch.incident_red * patch.reflectance_red
        patch.excident_green = patch.emmision_green + patch.incident_green * patch.reflectance_green
        patch.excident_blue = patch.emmision_blue + patch.incident_blue * patch.reflectance_blue
        
def calc_incident_light(patch):
    total_light = 0.0

def dibujarListaParches():
    for patch in patchesList:
        #if patchesList[i].coords == 'XY':
        # glColor(1.0 * BVectorRed[i],1.0 * BVectorGreen[i], 1.0 * BVectorBlue[i])
        glColor(patch.excident_red, patch.excident_green, patch.excident_blue)
        patch.draw()
    
def axis():
    axsize = 1
    glBegin(GL_LINES)
    glColor(1, 0, 0) #rojo = X
    glVertex3f(axsize, 0, 0)
    glVertex3f(-axsize, 0, 0)
    glColor(0, 1, 0) #verde = Y1
    glVertex3f(0, axsize, 0)
    glVertex3f(0, -axsize, 0)
    glColor(0, 0, 1) #azul = Z
    glVertex3f(0, 0, axsize)
    glVertex3f(0, 0, -axsize)
    glEnd()

def keyPressed(*args): #Presionar una tecla
    global VIEWPOINT_X
    global VIEWPOINT_Y
    global VIEWPOINT_Z
    global LOOK_AT_X
    global LOOK_AT_Y
    global LOOK_AT_Z
    
    global SECTIONS
    # global MINSECTIONS
    global INTENSITY
    
    key = args[0]
    speed = 0.4
    
    # Si presiono ESCAPE, salir de la aplicacion. Liberar recursos antes.
    if key == '\033':
        glutDestroyWindow(windowId)
        sys.exit()
    
    if key == '\162': # reset camara
        VIEWPOINT_X = IVX
        VIEWPOINT_Y = IVY
        VIEWPOINT_Z = IVZ
        LOOK_AT_X = LAX
        LOOK_AT_Y = LAY
        LOOK_AT_Z = LAZ
    if key == '\161': #q
        VIEWPOINT_X = VIEWPOINT_X + speed
        # print "VIEWPOINT_X =", VIEWPOINT_X
    if key == '\141': #a
        VIEWPOINT_X = VIEWPOINT_X - speed
        # print "VIEWPOINT_X =", VIEWPOINT_X
    #(W,S) = camara en Y
    if key == '\167': #w
        VIEWPOINT_Y = VIEWPOINT_Y + speed
        # print "VIEWPOINT_Y =", VIEWPOINT_Y
    if key == '\163': #s
        VIEWPOINT_Y = VIEWPOINT_Y - speed
        # print "VIEWPOINT_Y =", VIEWPOINT_Y
    #(E,D) = camara en Z
    if key == '\145': #e
        VIEWPOINT_Z = VIEWPOINT_Z + speed
        # print "VIEWPOINT_Z =", VIEWPOINT_Z
    if key == '\144': #d
        VIEWPOINT_Z = VIEWPOINT_Z - speed
        # print "VIEWPOINT_Z =", VIEWPOINT_Z
    if key == '\165': #u
        LOOK_AT_X = LOOK_AT_X + speed
        # print "LOOK_AT_X =", LOOK_AT_X
    if key == '\152': #j
        LOOK_AT_X = LOOK_AT_X - speed
        # print "LOOK_AT_X =", LOOK_AT_X
    #(W,S) = camara en Y
    if key == '\151': #i
        LOOK_AT_Y = LOOK_AT_Y + speed
        # print "LOOK_AT_Y =", LOOK_AT_Y
    if key == '\153': #k
        LOOK_AT_Y = LOOK_AT_Y - speed
        # print "LOOK_AT_Y =", LOOK_AT_Y
    #(E,D) = camara en Z
    if key == '\157': #o
        LOOK_AT_Z = LOOK_AT_Z + speed
        # print "LOOK_AT_Z =", LOOK_AT_Z
    if key == '\154': #l
        LOOK_AT_Z = LOOK_AT_Z - speed
        # print "LOOK_AT_Z =", LOOK_AT_Z
    if key == '\053':
        #shoot()
        collect()
        #print "SHOOT!"
        print "COLLECT!"

def LoadTextures():
    #global texture
    image = Image.open("texture.jpg")
    
    ix = image.size[0]
    iy = image.size[1]
    image = image.tostring("raw", "RGBX", 0, -1)
    
    # Create Texture    
    # There does not seem to be support for this call or the version of PyOGL I have is broken.
    #glGenTextures(1, texture)
    #glBindTexture(GL_TEXTURE_2D, texture)   # 2d texture (x and y size)
    
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

def main(): #Nuestra funcion principal
    global windowId
    
    glutInit(())
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutInitWindowPosition(0, 0)
    windowId = glutCreateWindow("CC52B - Radiosity")
    glutDisplayFunc (DrawGLScene)
    glutIdleFunc(DrawGLScene)
    glutReshapeFunc (ReSizeGLScene)
    glutKeyboardFunc (keyPressed)
    
    init(WIDTH, HEIGHT)

    # Loop infinito
    glutMainLoop()

print "Hit ESC key to quit."
main()

