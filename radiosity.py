from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from numpy import *
import sys
import math
import time

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
    
    FormFactors = [[-1 for col in range(0,len(patchesList))] for row in range(len(patchesList))]
    Visibilidad = [[-1 for col in range(0,len(patchesList))] for row in range(len(patchesList))]
    
    print "Computar Visibilidades"
    computeVisibilidad()
    print "OK visibilidades, computar FormFactors"
    computeFormFactors()
    print "OK FormFactors, calcular iteraciones"
    # passIteration(40)
    RadiosityIteration(1)
    print "segundos= ",time.time()-ITIME
    
    glClearColor(0.0, 0.0, 0.0, 0.0)    # Color negro, sin transparencia
    
    glClearDepth(1.0)                   # Enables Clearing Of The Depth Buffer
    glDepthFunc(GL_LESS)                # The Type Of Depth Test To Do
    glEnable(GL_DEPTH_TEST)             # Enables Depth Testing
    glShadeModel(GL_SMOOTH)             # Enables Smooth Color Shading
    
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
    axis()
    
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
            
            p1 = Punto(x0, y0, 0)
            p2 = Punto(x0 + step, y0, 0)
            p3 = Punto(x0, y0 + step, 0)
            p4 = Punto(x0 + step, y0 + step, 0)
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
            
            p1 = Punto(x0, 0, z0)
            p2 = Punto(x0, 0, z0 + step)
            p3 = Punto(x0 + step, 0, z0)
            p4 = Punto(x0 + step, 0, z0 + step)
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
            
            p1 = Punto(0, y0, z0)
            p2 = Punto(0, y0 + step, z0)
            p3 = Punto(0, y0, z0 + step)
            p4 = Punto(0, y0 + step, z0 + step)
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
    patchesList.extend( patchesCubo( Punto(2,1,2),2,3,1,0,[0.8,0.2,0.2]) )
    # patchesList.extend( uvsphere(2 , 3 , 1.5 , 0.4, 0, [0.9,0.5,0.5]) )
    # patchesList.extend( uvsphere(4 , 2 , 1.5 , 0.5, 0, [0.9,0.5,0.5]) )
    # patchesList.extend( patchesIcosaedro_2(2 , 3 , 1.5 , 0.4, 0, [0.8,0.5,0.5]) )
    # patchesList.extend( patchesIcosaedro_2(2 , 2 , 4   , 0.4, 0, [0.5,0.8,0.4]) )
    # patchesList.extend( patchesIcosaedro_2(2 , 1 , 1   , 0.4, 0, [0.8,0.8,0.8]) )
    # patchesList.extend( patchesCubo(2 , 1 , 1 , 0.4, 0) )

def aniadirFuentesLuminosas():
    global patchesList
    global lightsList
    
    # fuente1 = Patch(Punto(5.0,4.0,4.0),Punto(4.0,5.0,4.0),Punto(4.0,4.0,5.0))
    fuente1 = Patch(Punto(5.5,4.0,8.0),Punto(5.5,4.5,8.0),Punto(5.0,4.5,8.0),Punto(5.0,4.0,8.0))
    # fuente2 = Patch(Punto(4.0,2.2,2.1),Punto(3.8,2.6,2.2),Punto(3.9,2.4,2.4))
    
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
  
def computeVisibilidad():
    global Visibilidad
    for x in range(0,len(patchesList)):
        for y in range(0,x+1):
            if(x == y):
                Visibilidad[x][y] = 1
            else:
                Visibilidad[x][y] = visibility(x,y)

def getVisibilidad(i,j):
    if(Visibilidad[i][j] == -1):
        return Visibilidad[j][i]
    else:
        return Visibilidad[i][j]
            
def computeFormFactors():
    global FormFactors
    for x, patch_1 in enumerate(patchesList):
        for y, patch_2 in enumerate(patchesList):
            FormFactors[x][y] = formfactor(x, y, getVisibilidad(x,y))

def getFormFactor(i,j):
    if(FormFactors[i][j] == -1):
        return FormFactors[j][i]
    else:
        return FormFactors[i][j]

def RadiosityIteration(iterations):
    for x in xrange(0,iterations):
        print "iteration ",x
        # shoot()
        collect()
        
def shoot():
    for index_x, patch_1 in enumerate(patchesList):
        for index_y, patch_2 in enumerate(patchesList):
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
    
    # Si presiono ESCAPE, salir de la aplicacion. Liberar recursos antes.
    if key == '\033':
        glutDestroyWindow(windowId)
        sys.exit()
    # if key == '\152': #j
    #     SECTIONS += 1 #Aumento el detalle
    # if key == '\153' and SECTIONS > MINSECTIONS: #k
    #     SECTIONS -= 1 #decremento el detalle
    if key == '\162': # reset camara
        VIEWPOINT_X = IVX
        VIEWPOINT_Y = IVY
        VIEWPOINT_Z = IVZ
        LOOK_AT_X = LAX
        LOOK_AT_Y = LAY
        LOOK_AT_Z = LAZ
    if key == '\161': #q
        VIEWPOINT_X = VIEWPOINT_X + 0.2
        # print "VIEWPOINT_X =", VIEWPOINT_X
    if key == '\141': #a
        VIEWPOINT_X = VIEWPOINT_X - 0.2
        # print "VIEWPOINT_X =", VIEWPOINT_X
    #(W,S) = camara en Y
    if key == '\167': #w
        VIEWPOINT_Y = VIEWPOINT_Y + 0.2
        # print "VIEWPOINT_Y =", VIEWPOINT_Y
    if key == '\163': #s
        VIEWPOINT_Y = VIEWPOINT_Y - 0.2
        # print "VIEWPOINT_Y =", VIEWPOINT_Y
    #(E,D) = camara en Z
    if key == '\145': #e
        VIEWPOINT_Z = VIEWPOINT_Z + 0.2
        # print "VIEWPOINT_Z =", VIEWPOINT_Z
    if key == '\144': #d
        VIEWPOINT_Z = VIEWPOINT_Z - 0.2
        # print "VIEWPOINT_Z =", VIEWPOINT_Z
    if key == '\165': #u
        LOOK_AT_X = LOOK_AT_X + 0.2
        # print "LOOK_AT_X =", LOOK_AT_X
    if key == '\152': #j
        LOOK_AT_X = LOOK_AT_X - 0.2
        # print "LOOK_AT_X =", LOOK_AT_X
    #(W,S) = camara en Y
    if key == '\151': #i
        LOOK_AT_Y = LOOK_AT_Y + 0.2
        # print "LOOK_AT_Y =", LOOK_AT_Y
    if key == '\153': #k
        LOOK_AT_Y = LOOK_AT_Y - 0.2
        # print "LOOK_AT_Y =", LOOK_AT_Y
    #(E,D) = camara en Z
    if key == '\157': #o
        LOOK_AT_Z = LOOK_AT_Z + 0.2
        # print "LOOK_AT_Z =", LOOK_AT_Z
    if key == '\154': #l
        LOOK_AT_Z = LOOK_AT_Z - 0.2
        # print "LOOK_AT_Z =", LOOK_AT_Z
    # (+,-) intensidad de la luz
    # if key == '\053':
    #     INTENSITY = INTENSITY + 10
    #     cambiarLuminosidad()
    #     print "INTENSITY =",INTENSITY
    # if key == '\055' and INTENSITY-10<INITINTEN:
    #     INTENSITY = INTENSITY - 10
    #     cambiarLuminosidad()
    #     print "INTENSITY =",INTENSITY
    if key == '\053':
        shoot()
        print "SHOOT!"
            

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

