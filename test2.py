from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time
import sys
import math

from patch import *
from punto import *

windowId = -1
ESCAPE = '\033'
ARRIBA = '\152' #j
ABAJO = '\153' #k
X = 0
Y = 0
Z = 2
WIDTH = 800
HEIGHT = 600

#variables de las esferas
MINSECTIONS = 20 #secciones triangulares minimas para representar cada 
SECTIONS = MINSECTIONS #number of triangles to use to estimate a circle

# Configuramos OpenGL
def InitGL(width, height):              
    
    glClearColor(0.0, 0.0, 0.0, 0.0)    # Color negro, sin transparencia
    
    glClearDepth(1.0)                   # Enables Clearing Of The Depth Buffer
    glDepthFunc(GL_LESS)                # The Type Of Depth Test To Do
    glEnable(GL_DEPTH_TEST)             # Enables Depth Testing
    glShadeModel(GL_SMOOTH)             # Enables Smooth Color Shading
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()                    # Reset The Projection Matrix
                                        # Calculate The Aspect Ratio Of The Window
    gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)

# Callback al cambiar el tamanio de la escena
def ReSizeGLScene(width, height):
    
    if height == 0:
        height = 1        # previene dividir por cero

    # No importa por ahora
    glViewport(0, 0, width, height) 
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

# Lo que se dibujar'a
def DrawGLScene():
    global X
    global Y
    global Z
    
    # Limpiamos los buffers de la iteracion anterior
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    gluLookAt(X, Y, Z,
              0.0, 0.0, 0.0,
              0.0, 1.0, 0.0)
    axis()
    scenario()

    #  Intercambiamos los buffers. Ahora lo visible es lo que acabamos de dibujar.
    glutSwapBuffers()
    
def scenario():
    #el origen de cada plano
    size = 1
    glColor(0.5, 0, 0)
    
    glBegin(GL_QUADS)
    
    #plano XY, dentro de la pantalla
    glVertex3f(0, 0, -size)
    glVertex3f(size, 0, -size)
    glVertex3f(size, size, -size)
    glVertex3f(0, 0 + size, -size)
    
    glColor(0, 0.5, 0)
    #plano YZ, dentro de la pantalla
    glVertex3f(0, 0, 0)
    glVertex3f(0, size, 0)
    glVertex3f(0, size, -size)
    glVertex3f(0, 0, -size)
    
    glColor(0, 0, 0.5)
    #plano XZ
    glVertex3f(0, 0, 0)
    glVertex3f(size, 0, 0)
    glVertex3f(size, 0, -size)
    glVertex3f(0, 0, -size)
    
    glEnd()
    
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

#Presionar una tecla
def keyPressed(*args):
    global X
    global Y
    global Z
    global SECTIONS
    global MINSECTIONS
    
    key = args[0]
    
    # Si presiono ESCAPE, salir de la aplicacion. Liberar recursos antes.
    if key == ESCAPE:
        glutDestroyWindow(windowId)
        sys.exit()
    if key == ARRIBA:
        SECTIONS+= 1 #Aumento el detalle
    if key == ABAJO and SECTIONS > MINSECTIONS:
        SECTIONS-= 1 #decremento el detalle
    if key == '\161': #q
        X = X + 0.2
        print "X =", X
    if key == '\141': #a
        X = X - 0.2
        print "X =", X
    #(W,S) = camara en Y
    if key == '\167': #w
        Y = Y + 0.2
        print "Y =",Y
    if key == '\163': #s
        Y = Y - 0.2
        print "Y =",Y
    #(E,D) = camara en Z
    if key == '\145': #e
        Z = Z + 0.2
        print "Z =",Z
    if key == '\144': #d
        Z = Z - 0.2
        print "Z =",Z
        
    

# Nuestra funcion principal
def main():
    global windowId
    global WIDTH
    global HEIGHT
    
    # Configurar OpenGL
    glutInit(())

    # Mi modo de Display. Por ahora, no importa
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    
    # Tamano de la ventana.
    glutInitWindowSize(WIDTH, HEIGHT)
    
    # Donde queremos que se posicione la ventana al iniciar.
    glutInitWindowPosition(0, 0)
    
    windowId = glutCreateWindow("CC52B - Tarea 1 - Gabriel Gayan")

    glutDisplayFunc (DrawGLScene)
    glutIdleFunc(DrawGLScene)
    glutReshapeFunc (ReSizeGLScene)
    glutKeyboardFunc (keyPressed)
    InitGL(WIDTH, HEIGHT)

    # Loop infinito
    glutMainLoop()

print "Hit ESC key to quit."
main()
