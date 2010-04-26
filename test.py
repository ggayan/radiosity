from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from numpy import *
import sys
import math
import random
import time

from patch import *
from punto import *

windowId = -1
ESCAPE = '\033'

WIDTH = 600
HEIGHT = 600

N = 10
AMPLITUDE = 30
ANGLES = 0
ANGLES2 = 0
TIME = time.time()
SPEED = 10
D = 10
X = 3
Y = 3
Z = 3

# Configuramos OpenGL
def InitGL():
    
    glClearColor(0.0, 0.0, 0.0, 0.0)    # Color negro, sin transparencia
    
    glClear(GL_COLOR_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glViewport(0, 0, WIDTH, HEIGHT)
    glMatrixMode(GL_PROJECTION)
    #glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    #gluOrtho2D(-1, 1, -1, 1)
    
    #glOrtho(-1, 1, -1, 1, -10, 10)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    #glTranslatef(-100.0, 0.0, 0.0)
    
def Init():
    
    global ANGLES
    global ANGLES2
    
    ANGLES = 0
    ANGLES2 = 0
        
# Callback al cambiar el tamanio de la escena
def ReSizeGLScene(width, height):
    
    if height == 0:
        height = 1        # previene dividir por cero

    glClear(GL_COLOR_BUFFER_BIT)
    glViewport(0, 0, WIDTH, HEIGHT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    #gluOrtho2D(-1, 1, -1, 1)
    glOrtho(-1, 1, -1, 1, -10, 10)
    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
def star(points):

    glBegin(GL_LINES)
    glVertex2f(0.0, -1.0)
    glVertex2f(0.0, 1.0)
    glVertex2f(1.0, 0.0)
    glVertex2f(-1.0, 0.0)
    glEnd()
    
    factor = 0.5

    glBegin(GL_TRIANGLE_FAN)
    glVertex2f( 0, -1.0)
    for i in range(0, points+1):
        angle = 2*math.pi * i / points
        glVertex2f( factor * math.sin(angle), factor * math.cos(angle) - 1.0)
    glEnd()
        
    glBegin(GL_TRIANGLE_FAN)
    for i in range(0, points+1):
        angle = 2*math.pi * i / points
        glVertex2f( 0.5*factor * math.sin(angle), 0.5*factor * math.cos(angle) - 1.0 + factor)
    glEnd()

def test(dt):

    glPushMatrix()
    glTranslatef(-1.0, 0.0, 0.0)
    glColor(1, 1, 1)
    glRotatef(10*SPEED*(time.time()-TIME), 0.0, 0.0, 1.0)
    glutWireSphere(0.5,dt,dt)
    glPopMatrix();
    glPushMatrix()
    glTranslatef(1.0, 0.0, 0.0)
    glColor(0.5, 0.5, 0.5)
    glutSolidSphere(0.5,dt,dt)
    glPopMatrix();

def scenario():
    xo = 0
    yo = 0
    zo = -1
    size = 1.5
    glPushMatrix()
    glColor(0.7, 0.7, 0)
    glBegin(GL_QUADS)
    #bottom (Z)
    glVertex3f( -size+xo, -size+yo, 0 +zo)
    glVertex3f( -size+xo, size +yo, 0 +zo)
    glVertex3f(  size+xo, size +yo, 0 +zo)
    glVertex3f(  size+xo, -size+yo, 0 +zo)
    #right (X)
    glVertex3f( -size +xo, -size+yo, -size +zo +size)
    glVertex3f( -size +xo, size +yo, -size +zo +size)
    glVertex3f( -size +xo, size +yo, size +zo +size)
    glVertex3f( -size +xo, -size+yo, size +zo +size)
    #left (Y)
    glVertex3f( -size+xo, -size+yo, -size +zo +size)
    glVertex3f( -size+xo, -size +yo, size +zo +size)
    glVertex3f(  size+xo, -size +yo, size +zo +size)
    glVertex3f(  size+xo, -size+yo, -size +zo +size)
    
    glEnd()
    glColor(0.3,0.3,0.3)
    p1 = Punto(0,0,0)
    p2 = Punto(1,1,1)
    p3 = Punto(1,1,-1)
    p = Patch(p1,p2,p3)
    glBegin(GL_TRIANGLES)
    glVertex3f(p.p1.x,p.p1.y,p.p1.z)
    glVertex3f(p.p2.x,p.p2.y,p.p2.z)
    glVertex3f(p.p3.x,p.p3.y,p.p3.z)
    glEnd()
    
    glPopMatrix()

def axis():
    glPushMatrix()
    glBegin(GL_LINES)
    glColor(1, 0, 0) #rojo = X
    glVertex3f(2, 0, 0)
    glVertex3f(-2, 0, 0)
    glColor(0, 1, 0) #verde = Y
    glVertex3f(0, 2, 0)
    glVertex3f(0, -2, 0)
    glColor(0, 0, 1) #azul = Z
    glVertex3f(0,0,0)
    p = Punto(2,0,0).cruz(Punto(0,2,0))
    glVertex3f(p.x,p.y,p.z)
    #glVertex4f(0,0,4+4,math.sqrt(8*8))  #calculo de normal
    #glVertex3f(0, 0, 2)
    #glVertex3f(0, 0,-2)
    glEnd()
    glPopMatrix()

# Lo que se dibujar'a
def DrawGLScene():
    
    global AMPLITUDE
    global ANGLES
    global ANGLES2
    
    # Limpiamos los b'ufers de la iteraci'on anterior
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    #glTranslatef(0,0,1.0)
    zoomFactor = 5
    gluPerspective (50.0*zoomFactor, 1, -5, 5)
    gluLookAt(X,Y,Z, 0,0,0, 0,0,-1)
    
    
    glPushMatrix()
    #glTranslatef(X, Y, 0)
    glRotatef(SPEED*(time.time()-TIME), 0.0, 0.0, 1.0)
    #glScalef(SIZE, SIZE, 0)
    #glColor(1, 1, 1)
    test(D)
    glPopMatrix();

    scenario()
    axis()
       
    # glPushMatrix()
        
    # #glTranslatef(X, Y, 0)
    # glRotatef(AMPLITUDE*math.sin(ANGLES), 0.0, 0.0, 1.0)
    # glScalef(SIZE, SIZE, 0)
    # glColor(RED, GREEN, BLUE)
    # star(N)
        
    # ANGLES = ANGLES + 0.1
        
    # glPopMatrix();
    
    # glPushMatrix()
        
    # #glTranslatef(X, Y, 0)
    # glRotatef(AMPLITUDE*math.sin(ANGLES2), 0.0, 0.0, 1.0)
    # glScalef(SIZE, SIZE, 0)
    # glColor(RED, GREEN, BLUE)
    # star(N)
        
    # ANGLES2 = ANGLES2 - 0.1
        
    # glPopMatrix();
    
    #  Intercambiamos los b'ufers. Ahora lo visible es lo que acabamos de dibujar.
    glutSwapBuffers()

# Cuando el usuario presiene una tecla
def keyPressed(*args):
    key = args[0]
    global SPEED
    global D
    global X
    global Y
    global Z
    # Si presion'o ESCAPE, salir de la aplicaci'on. Liberar recursos antes.
    if key == ESCAPE:
        glutDestroyWindow(windowId)
        sys.exit()
    if key == '\152':
        SPEED = SPEED + 10
    if key == '\153':
        SPEED = SPEED - 10
    # (M,L) = cantidad de linas en circulos
    if key == '\154':
        D = D + 1
    if key == '\155':
        D = D - 1
    #(Q,A) = camara en X
    if key == '\161': #q
        X = X + 0.2
    if key == '\141': #a
        X = X - 0.2
    #(W,S) = camara en Y
    if key == '\167': #w
        Y = Y + 0.2
    if key == '\163': #s
        Y = Y - 0.2
    #(E,D) = camara en Z
    if key == '\145': #e
        Z = Z + 0.2
    if key == '\144': #d
        Z = Z - 0.2

# Nuestra funci'oprincipal
def main():
    global windowId

    # Configurar OpenGL
    glutInit(())

    # Mi modo de Display. Por ahora, no importa
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA )
    
    # Tamanio de la ventana.
    glutInitWindowSize(WIDTH, HEIGHT)
    
    # Donde queremos que se posicione la ventana al iniciar.
    glutInitWindowPosition(0, 0)
    
    windowId = glutCreateWindow("CC52B - proyecto")

    # Defino la funci'on que se encargar'a de dibujar
    glutDisplayFunc (DrawGLScene)
    
    # La funci'on cuando el programa este Idle. 
    # En un videoJuego, 'este ser'ia el lugar donde actualizo posiciones, calculo puntajes, etc.
    glutIdleFunc(DrawGLScene)
    
    # La funci'on a llamar cuando cambia el tamanio de la ventana.
    glutReshapeFunc (ReSizeGLScene)
    
    # La funci'on que se encarga de recibir el input desde teclado
    glutKeyboardFunc (keyPressed)

    # Configuramos OpenGL para trabajar al tamanio deseado.
    InitGL()
    
    # Configuramos data
    Init()

    # Loop infinito
    glutMainLoop()

print "Hit ESC key to quit."
main()
