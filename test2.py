from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from numpy import *
import time
import sys
import math
import random

from patch import *
from punto import *
from functions import *

windowId = -1

#parametros del punto de vista

#el punto desde el cual miro
VIEWPOINT_X = 1.2
VIEWPOINT_Y = 0.8
VIEWPOINT_Z = 1.6

#el punto al cual miro
LOOK_AT_X = 0
LOOK_AT_Y = 0
LOOK_AT_Z = 0

#el vector que indica hacia donde es 'arriba' para la camara
UP_VECTOR_X = 0
UP_VECTOR_Y = 1
UP_VECTOR_Z = 0

#resolucion de la ventana
WIDTH = 800
HEIGHT = 600

#variables de los planos
SECTIONS = 16 #numero de triangulos por columna de un plano

#las filas tienen la mitad de secciones

#planos, son arreglos dobles
planoXY = [[0 for col in range(SECTIONS)] for row in range(SECTIONS / 2)]
planoYZ = [[0 for col in range(SECTIONS)] for row in range(SECTIONS / 2)]
planoXZ = [[0 for col in range(SECTIONS)] for row in range(SECTIONS / 2)]

#lista completa de los parches
patchesList = []

#limites de los planos


# Configuramos OpenGL
def InitGL(width, height):              
    
    #llamo la funcion que genera los planos
    generarPlanos()
    
    generarListaDeParches()
    
    glClearColor(0.0, 0.0, 0.0, 0.0)    # Color negro, sin transparencia
    
    glClearDepth(1.0)                   # Enables Clearing Of The Depth Buffer
    glDepthFunc(GL_LESS)                # The Type Of Depth Test To Do
    glEnable(GL_DEPTH_TEST)             # Enables Depth Testing
    glShadeModel(GL_SMOOTH)             # Enables Smooth Color Shading
    glDisable(GL_CULL_FACE)
    
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
    print formfactor(patchesList[0],patchesList[1])

    #  Intercambiamos los buffers. Ahora lo visible es lo que acabamos de dibujar.
    glutSwapBuffers()
    
#las figuras a dibujar
def escenario():
    glBegin(GL_TRIANGLES)
    glColor(0.5, 0, 0)
    dibujarPlano(planoXY)
    glColor(0, 0.5, 0)
    dibujarPlano(planoXZ)
    glColor(0, 0, 0.5)
    dibujarPlano(planoYZ)
    glEnd()
    
#funcion que genera los planos a dibujar
def generarPlanos():
    global planoXY
    global planoXZ
    global planoYZ
    
    size = 1.0
    step = size / SECTIONS
    
    #planoXY
    x0 = 0
    y0 = 0
    
    for i in range(0, SECTIONS / 2): #eje horizonal
        for j in range(0, SECTIONS): #eje vertical
            if j % 2 == 0: #pares
                p1 = Punto(x0, y0, 0)
                p2 = Punto(x0, y0 + step, 0)
                p3 = Punto(x0 + step, y0, 0)
                planoXY[i][j] = Patch(p1, p2, p3)
            else:
                #segundo triangulo
                p1 = Punto(x0, y0 + step, 0)
                p2 = Punto(x0 + step, y0 + step, 0)
                p3 = Punto(x0 + step, y0, 0)
                planoXY[i][j] = Patch(p1, p2, p3)
                y0 += step
        x0 += step
        y0 = 0
    
    #planoXZ
    x0 = 0
    z0 = 0
    
    for i in range(0, SECTIONS / 2): #eje horizonal
        for j in range(0, SECTIONS): #eje vertical
            if j % 2 == 0: #pares
                p1 = Punto(x0, 0, z0)
                p2 = Punto(x0, 0, z0 + step)
                p3 = Punto(x0 + step, 0, z0)
                planoXZ[i][j] = Patch(p1, p2, p3)
            else:
                #segundo triangulo
                p1 = Punto(x0, 0, z0 + step)
                p2 = Punto(x0 + step, 0, z0 + step)
                p3 = Punto(x0 + step, 0, z0)
                planoXZ[i][j] = Patch(p1, p2, p3)
                z0 += step
        x0 += step
        z0 = 0
        
    #planoYZ
    y0 = 0
    z0 = 0
    
    for i in range(0, SECTIONS / 2): #eje horizonal
        for j in range(0, SECTIONS): #eje vertical
            if j % 2 == 0: #pares
                p1 = Punto(0, y0, z0)
                p2 = Punto(0, y0 + step, z0)
                p3 = Punto(0, y0, z0 + step)
                planoYZ[i][j] = Patch(p1, p2, p3)
            else:
                #segundo triangulo
                p1 = Punto(0, y0 + step, z0)
                p2 = Punto(0, y0 + step, z0 + step)
                p3 = Punto(0, y0, z0 + step)
                planoYZ[i][j] = Patch(p1, p2, p3)
                y0 += step
        z0 += step
        y0 = 0
        
def generarListaDeParches():
    global patchesList
    for i in range(0, SECTIONS / 2): #filas
        patchesList.extend(planoXY[i])
        patchesList.extend(planoXZ[i])
        patchesList.extend(planoYZ[i])

def dibujarListaParches():
    for i in range(0, len(patchesList)):
        patchesList[i].dibujar()

def dibujarPlano(plano):
    for i in range(0, SECTIONS / 2): #filas
        for j in range(0, SECTIONS): #columnas
            plano[i][j].dibujar()
    
    
def axis():
    glBegin(GL_LINES)
    glColor(1, 0, 0) #rojo = X
    glVertex3f(1, 0, 0)
    glVertex3f(-1, 0, 0)
    glColor(0, 1, 0) #verde = Y
    glVertex3f(0, 1, 0)
    glVertex3f(0, -1, 0)
    glColor(0, 0, 1) #azul = Z
    glVertex3f(0, 0, 1)
    glVertex3f(0, 0, -1)
    glEnd()

def keyPressed(*args): #Presionar una tecla
    global VIEWPOINT_X
    global VIEWPOINT_Y
    global VIEWPOINT_Z
    global SECTIONS
    global MINSECTIONS
    
    key = args[0]
    
    # Si presiono ESCAPE, salir de la aplicacion. Liberar recursos antes.
    if key == '\033':
        glutDestroyWindow(windowId)
        sys.exit()
    if key == '\152': #j
        SECTIONS += 1 #Aumento el detalle
    if key == '\153' and SECTIONS > MINSECTIONS: #k
        SECTIONS -= 1 #decremento el detalle
    if key == '\161': #q
        VIEWPOINT_X = VIEWPOINT_X + 0.2
        print "VIEWPOINT_X =", VIEWPOINT_X
    if key == '\141': #a
        VIEWPOINT_X = VIEWPOINT_X - 0.2
        print "VIEWPOINT_X =", VIEWPOINT_X
    #(W,S) = camara en Y
    if key == '\167': #w
        VIEWPOINT_Y = VIEWPOINT_Y + 0.2
        print "VIEWPOINT_Y =", VIEWPOINT_Y
    if key == '\163': #s
        VIEWPOINT_Y = VIEWPOINT_Y - 0.2
        print "VIEWPOINT_Y =", VIEWPOINT_Y
    #(E,D) = camara en Z
    if key == '\145': #e
        VIEWPOINT_Z = VIEWPOINT_Z + 0.2
        print "VIEWPOINT_Z =", VIEWPOINT_Z
    if key == '\144': #d
        VIEWPOINT_Z = VIEWPOINT_Z - 0.2
        print "VIEWPOINT_Z =", VIEWPOINT_Z

def main(): #Nuestra funcion principal
    global windowId
    
    # Configurar OpenGL
    glutInit(())

    # Mi modo de Display. Por ahora, no importa
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    
    # Tamano de la ventana.
    glutInitWindowSize(WIDTH, HEIGHT)
    
    # Donde queremos que se posicione la ventana al iniciar.
    glutInitWindowPosition(0, 0)
    
    windowId = glutCreateWindow("CC52B - Radiosity")

    glutDisplayFunc (DrawGLScene)
    glutIdleFunc(DrawGLScene)
    glutReshapeFunc (ReSizeGLScene)
    glutKeyboardFunc (keyPressed)
    InitGL(WIDTH, HEIGHT)

    # Loop infinito
    glutMainLoop()

print "Hit ESC key to quit."
main()

