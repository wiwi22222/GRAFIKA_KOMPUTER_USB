#include <windows.h>
#if def_APPLE_
#include <GLUT/glut.h>
#else
#include <GL/glut.h>
#endif
#include <stdlib.h>

void init(void);
void display(void);

int main(int argc, char** argv)
{
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
	glutInitWindowSize(250, 250);
	glutInitWindowPosition(100, 100);
	glutCreateWindow("my first openGL application");
	init();
	glutDisplayFunc(display);
	glutMainLoop();
	return 0;
}


void init(void)
{
	glClearColor(1.0, 1.0, 1.0, 1.0);
	glColor3f(0.0, 0.0, 1.0);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	glOrtho(-100.0, 100.0, -100.0, 100.0, -100.0, 100.0);
}

void display(void)
{
	glClear(GL_COLOR_BUFFER_BIT);

	// GL_LINE_LOOP
	glBegin(GL_LINE_LOOP);
	glVertex2i(20, 10);
	glVertex2i(50, 10);
	glVertex2i(20, 80);
	glVertex2i(50, 80);
	glEnd();

	glutSwapBuffers();
}
