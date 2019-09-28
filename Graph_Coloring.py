from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import numpy as np
from math import *
from collections import defaultdict
import time


name = 'Assignment'
counter=0
mouseX=0
mouseY=0
FirstX=0
SecondX=0
FirstY=0
SecondY=0
node_listX=[]
node_listY=[]
graph = defaultdict(list)
oneNode=0
adjacency_matrix = []
list1=[]
list_counter=0
node_counter=0
color_check=0



color_dict = {
    1: [1, 0, 0],
    2: [0, 1, 0],
    3: [0, 0, 1],
    4: [1, 1, 0],
    5: [1, 0, 1],
    6: [0, 1, 1],
    7: [0.5, 0.5, 0.5],
    8: [0.2, 0.5, 0.8],
    9: [0.8, 0.5, 0.2],
}


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(800,800)
    glutCreateWindow(name)
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutMouseFunc(myMouse)
    glutIdleFunc(Render)
    glutMainLoop()
    return


def reshape(w,h):
    glClearColor(255, 255, 255, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    gluOrtho2D(0, 800, 800, 0)
    glViewport(0,0,800,800)
    glFlush()
    return


def keyboard(key, x, y):
    global color_check
    key = key.decode('ASCII')
    if key == 'w':
        convert()
    if key == 'e':
        color_check = 1


def myMouse(button,state,x,y):
    global mouseX, mouseY, FirstX, SecondX, FirstY, SecondY, counter, node_listX, node_listY, graph, oneNode
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        mouseX = x
        mouseY = y
        drawCircle(x,y)
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        if counter==0:
            for i in range(len(node_listX)):
                if distance(x, node_listX[i] ,y, node_listY[i])<50:
                    FirstX=node_listX[i]
                    FirstY=node_listY[i]
                    counter=1
                    oneNode=i+1
                    break
        elif counter==1:
            for i in range(len(node_listX)):
                if distance(x, node_listX[i] ,y, node_listY[i])<50:
                    SecondX=node_listX[i]
                    SecondY=node_listY[i]
                    connect(FirstX, FirstY, SecondX, SecondY)
                    counter=0
                    graph[oneNode].append(i+1)
                    graph[i+1].append(oneNode)
                    break


def connect(X1, Y1, X2, Y2):
    glBegin(GL_LINES)
    glVertex2f(X1, Y1)
    glVertex2f(X2, Y2)
    glEnd();
    glFlush();


def drawCircle(x,y):
    global node_listX, node_listY
    node_listX.append(x)
    node_listY.append(y)
    glColor(0,0,0);
    glBegin(GL_LINE_LOOP)
    sides = 50
    radius = 50
    for i in range(sides):
        cosine = radius * cos(i * 2 * pi / sides) + x
        sine = radius * sin(i * 2 * pi / sides) + y
        glVertex2f(cosine, sine)
    glEnd();
    glFlush();


def convert():
    global graph, adjacency_matrix, node_listX, list1, color_check
    print(graph)
    print(graph, adjacency_matrix, node_listX)
    x = len(node_listX)
    adjacency_matrix = np.zeros([x, x], dtype=int)
    for k, v in graph.items():
        for values in v:
            adjacency_matrix[k - 1][values - 1] = 1
    print(adjacency_matrix)
    no_of_colors = int(input())
    colors = [0]*x
    graphColoringUtil(adjacency_matrix, no_of_colors, colors, 0)
    print(colors, list1)


def distance(xi, xii, yi, yii):
    sq1 = (xi - xii) * (xi - xii)
    sq2 = (yi - yii) * (yi - yii)
    return sqrt(sq1 + sq2)


def display():
    return


def is_safe(n, graph, colors, c):
    for i in range(n):
        if graph[n][i] and c == colors[i]:
            return False
    return True


def graphColoringUtil(graph, color_nb, colors, n):
    global node_listX, list1

    if len(node_listX) == n:
        return True

    for c in range(1, color_nb+1):
        if is_safe(n, graph, colors, c):
            colors[n] = c
            list1.append(c)
            if graphColoringUtil(graph, color_nb, colors, n+1):
                return True
            colors[n] = 0
            list1.append(0)


def color_node():
    global node_counter, list1, node_listX, node_listY, list_counter
    if list_counter<len(list1):
        if list1[list_counter]==0:
            node_counter-=1
            glColor(1,1,1)
            x = node_listX[node_counter]
            y = node_listY[node_counter]
            glBegin(GL_POLYGON)
            sides = 50
            radius = 50
            for i in range(sides):
                cosine = radius * cos(i * 2 * pi / sides) + x
                sine = radius * sin(i * 2 * pi / sides) + y
                glVertex2f(cosine, sine)
            glEnd()
            glColor(0, 0, 0)
            glBegin(GL_LINE_LOOP)
            sides = 50
            radius = 50
            for i in range(sides):
                cosine = radius * cos(i * 2 * pi / sides) + x
                sine = radius * sin(i * 2 * pi / sides) + y
                glVertex2f(cosine, sine)
            glEnd()
            glFlush()
            list_counter+=1

        else:
            j = color_dict[list1[list_counter]]
            r = j[0]
            g= j[1]
            b= j[2]
            glColor(r,g,b)
            x = node_listX[node_counter]
            y=node_listY[node_counter]
            glBegin(GL_POLYGON)
            sides = 50
            radius = 50
            for i in range(sides):
                cosine = radius * cos(i * 2 * pi / sides) + x
                sine = radius * sin(i * 2 * pi / sides) + y
                glVertex2f(cosine, sine)
            glEnd()
            glFlush()
            node_counter+=1
            list_counter+=1

def Render():
    global color_check
    if color_check==1:
        color_node()
        time.sleep(0.5)


if __name__ == '__main__':
    main()
