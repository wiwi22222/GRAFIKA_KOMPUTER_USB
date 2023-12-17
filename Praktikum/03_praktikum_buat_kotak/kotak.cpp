#include <Windows.h>
#ifdef APPLE

#else
#include <GL/glut.h>
#endif // APPLE
#include<stdio.h>
#include <stdlib.h>
#include <math.h>

void init(void);
void display(void);

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
    glutInitWindowSize(800, 800);
    glutInitWindowPosition(10, 10);
    glutCreateWindow("My First OpenGL Application");
    init();
    glutDisplayFunc(display);
    glutMainLoop();
    return 0;
}

void init(void) {
    glClearColor(1.0, 1.0, 1.0, 1.0);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0, 1000, 0, 1000);
}

void display(void) {
    glClear(GL_COLOR_BUFFER_BIT);

    // Menghitung koordinat pusat layar
    int centerX = 400;
    int centerY = 400;

    // Menghitung koordinat untuk membuat kotak di tengah
    int width = 600;  // Lebar kotak
    int height = 600; // Tinggi kotak

    int left = centerX - width / 2;
    int right = centerX + width / 2;
    int top = centerY - height / 2;
    int bottom = centerY + height / 2;

    // Gambar kotak pertama dengan warna hitam dan garis tebal
    glLineWidth(3.0);  // Mengatur lebar garis menjadi 3.0
    glBegin(GL_LINE_LOOP);
    glColor3f(0.0, 0.0, 0.0);  // Warna hitam
    glVertex2f(left, top);
    glVertex2f(right, top);
    glVertex2f(right, bottom);
    glVertex2f(left, bottom);
    glEnd();

    glFlush();
    glutSwapBuffers();
}
