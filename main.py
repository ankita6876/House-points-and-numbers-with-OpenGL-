from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
def draw_points(x, y):
    glPointSize(20)
    glBegin(GL_POINTS)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(x,y)
    glEnd()


def iterate():
    glViewport(0, 0, 800, 300)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 800, 0.0, 300, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def draw_Lines():
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_LINES)
    #2
    glColor3f(1.0, 0.0, 1.0)
    glVertex2f(30,130)
    glColor3f(1.0, 0.0, 1.0)
    glVertex2f(80,130)
    #b to c
    glColor3f(1.0, 0.0, 1.0)
    glVertex2f(80,130)
    glColor3f(1.0, 0.0, 1.0)
    glVertex2f(80,90)
    #c to d
    glColor3f(1.0, 0.0, 1.0)
    glVertex2f(80,90)
    glColor3f(1.0, 0.0, 1.0)
    glVertex2f(30,90)
    #a to d
    glColor3f(1.0, 0.0, 1.0)
    glVertex2f(30,90)
    glColor3f(1.0, 0.0, 1.0)
    glVertex2f(30,50)
    #c to f
    glColor3f(1.0, 0.0, 1.0)
    glVertex2f(30,50)
    glColor3f(1.0, 0.0, 1.0)
    glVertex2f(80,50)

    # 3
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(110,50)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(160,50)
    # b to c
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(160,50)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(160,90)
    # c to d
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(160,90)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(110, 90)
    # a to d
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(160,90)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(160,130)
    # c to f
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(160,130)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(110,130)

    #1
    glColor3f(0.0, 1.0, 1.0)
    glVertex2f(190,50)
    glColor3f(0.0, 1.0, 1.0)
    glVertex2f(190,130)

    #4
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(220,130)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(220,90)
    # b to c
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(220,90)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(270,90)
    # c to d
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(270,90)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(270,130)
    # a to d
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(270,90)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(270,50)

    #1
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(300,50)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(300,130)

    #0
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(330,50)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(380,50)
    # b to c
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(380,50)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(380,130)
    # c to d
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(380,130)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(330,130)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(330,130)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(330,50)

    # 5
    glColor3f(1.0, 1.0, 0.0)
    glVertex2f(410,50)
    glColor3f(1.0, 1.0, 0.0)
    glVertex2f(460,50)
    # b to c
    glColor3f(1.0, 1.0, 0.0)
    glVertex2f(460,50)
    glColor3f(1.0, 1.0, 0.0)
    glVertex2f(460, 90)
    # c to d
    glColor3f(1.0, 1.0, 0.0)
    glVertex2f(460, 90)
    glColor3f(1.0, 1.0, 0.0)
    glVertex2f(410, 90)
    # a to d
    glColor3f(1.0, 1.0, 0.0)
    glVertex2f(410, 90)
    glColor3f(1.0, 1.0, 0.0)
    glVertex2f(410, 130)
    # c to f
    glColor3f(1.0, 1.0, 0.0)
    glVertex2f(410, 130)
    glColor3f(1.0, 1.0, 0.0)
    glVertex2f(460, 130)

    # 9
    glColor3f(1.0, 1.0, 0.0)
    glVertex2f(490,50)
    glColor3f(0.0, 1.0, 1.0)
    glVertex2f(540,50)
    # b to c
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(540,50)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(540, 90)
    # c to d
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(540, 90)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(490, 90)
    # a to d
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(490, 90)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(490, 130)
    # c to f
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(490, 130)
    glColor3f(1.0, 1.0, 0.0)
    glVertex2f(540, 130)
    glColor3f(0.0, 1.0, 1.0)
    glVertex2f(540, 130)
    glColor3f(1.0, 1.0, 0.0)
    glVertex2f(540, 90)

    glEnd()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    #glColor3f(1.0, 0.0, 1.0)
    draw_Lines()
    glutSwapBuffers()
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 300) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)
glutMainLoop()