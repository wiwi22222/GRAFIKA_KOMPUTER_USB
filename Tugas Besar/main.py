import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_house():
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_QUADS)
    glVertex2f(100, 500)
    glVertex2f(100, 300)
    glVertex2f(300, 300)
    glVertex2f(300, 500)
    glEnd()

    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_QUADS)
    glVertex2f(300, 500)
    glVertex2f(300, 300)
    glVertex2f(700, 300)
    glVertex2f(700, 400)
    glEnd()

    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_QUADS)
    glVertex2f(350, 300)
    glVertex2f(200, 100)
    glVertex2f(600, 200)
    glVertex2f(700, 300)
    glEnd()

    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(50, 300)
    glVertex2f(200, 100)
    glVertex2f(350, 300)
    glEnd()

    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_QUADS)
    glVertex2f(175, 400)
    glVertex2f(175, 500)
    glVertex2f(225, 500)
    glVertex2f(225, 400)
    glEnd()

    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_QUADS)
    glVertex2f(105, 475)
    glVertex2f(105, 425)
    glVertex2f(145, 425)
    glVertex2f(145, 475)
    glEnd()

    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_LINES)
    glVertex2f(105, 450)
    glVertex2f(145, 450)
    glEnd()

    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_LINES)
    glVertex2f(125, 425)
    glVertex2f(125, 475)
    glEnd()

    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_QUADS)
    glVertex2f(255, 475)
    glVertex2f(255, 425)
    glVertex2f(295, 425)
    glVertex2f(295, 475)
    glEnd()

    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_LINES)
    glVertex2f(255, 450)
    glVertex2f(295, 450)
    glEnd()

    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_LINES)
    glVertex2f(275, 425)
    glVertex2f(275, 475)
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluOrtho2D(0, display[0], display[1], 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_house()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
