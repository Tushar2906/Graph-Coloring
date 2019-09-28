from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import numpy as np
from math import *
from collections import defaultdict


name = 'Graph Coloring'
counter = 0
mouseX = 0
mouseY = 0
FirstX = 0
SecondX = 0
FirstY = 0
SecondY = 0
node_listX = []
node_listY = []
graph = defaultdict(list)
oneNode = 0
adjacency_matrix = []
list1=[]
list_counter=0
node_counter=0
color_change=0
no_of_colors=0


color_dict = {
    1: [1, 0, 0],
    2: [0, 1, 0],
    3: [0, 0, 1],
    4: [1, 1, 0],
    5: [1, 0, 1],
    6: [0, 1, 1],
    7: [1, 0, 0],
    8: [0, 1, 0],
    9: [0, 0, 1]
}


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(1200,800)
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
    gluOrtho2D(0, 1200, 800, 0)
    glViewport(0,0,1200,800)
    glFlush()
    return


def keyboard(key, x, y):
    key = key.decode('ASCII')
    if key == 'w':
        convert()
    elif key=='a':
        color_node()



def myMouse(button,state,x,y):
    global mouseX, mouseY, FirstX, SecondX, FirstY, SecondY, counter, node_listX, node_listY, graph, oneNode, no_of_colors
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if x<1000:
            mouseX = x
            mouseY = y
            drawRect(x, y)
        else:
            if y>100 and y<150:
                no_of_colors=2
            elif y>200 and y<250:
                no_of_colors=3
            elif y>300 and y<350:
                no_of_colors=4
            elif y>400 and y<450:
                no_of_colors=5
            elif y>500 and y<550:
                no_of_colors=6
            elif y>600 and y<650:
                no_of_colors=7


    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        if counter == 0:
            for i in range(len(node_listX)):
                if distance(x, node_listX[i], y, node_listY[i]) < 50:
                    FirstX = node_listX[i]
                    FirstY = node_listY[i]
                    counter = 1
                    oneNode = i+1
                    break
        elif counter == 1:
            for i in range(len(node_listX)):
                if distance(x, node_listX[i] ,y, node_listY[i])<50:
                    SecondX = node_listX[i]
                    SecondY = node_listY[i]
                    connect(FirstX, FirstY, SecondX, SecondY)
                    counter = 0
                    graph[oneNode].append(i+1)
                    graph[i+1].append(oneNode)
                    break


def connect(X1, Y1, X2, Y2):
    glColor(0,0,0)
    glLineWidth(10)
    glBegin(GL_LINES)
    glVertex2f(X1, Y1)
    glVertex2f(X2, Y2)
    glEnd()
    glFlush()


def drawRect(x,y):
    global node_listX, node_listY
    node_listX.append(x)
    node_listY.append(y)
    block_no = "Block No. " + str(len(node_listX))
    glColor(0,0,0)
    glRasterPos2i(x-50,y+75)
    for i in block_no:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(str(i)))
    glFlush()
    glColor(0,0,0);
    glBegin(GL_POLYGON)
    glVertex(x-50,y-50)
    glVertex(x + 50, y - 50)
    glVertex(x + 50, y + 50)
    glVertex(x - 50, y + 50)
    glEnd()
    glFlush()


def convert():
    global graph, adjacency_matrix, node_listX, no_of_colors
    x = len(node_listX)
    adjacency_matrix = np.zeros([x, x], dtype=int)
    for k, v in graph.items():
        for values in v:
            adjacency_matrix[k - 1][values - 1] = 1
    if no_of_colors==0:
        print("Enter number of colors")
        no_of_colors = int(input())
    colors = [0]*x
    graphColoringUtil(adjacency_matrix, no_of_colors, colors, 0)
    print(colors)


def distance(xi, xii, yi, yii):
    sq1 = (xi - xii) * (xi - xii)
    sq2 = (yi - yii) * (yi - yii)
    return sqrt(sq1 + sq2)


def display():
    glColor(0,0,0)
    glBegin(GL_POLYGON)
    glVertex(1050, 100)
    glVertex(1050, 150)
    glVertex(1150, 150)
    glVertex(1150, 100)
    glEnd()
    glColor(1,1,1)
    glRasterPos2i(1090, 125)
    text = "2"
    for i in text:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(str(i)))
    glColor(0,0,0)
    glBegin(GL_POLYGON)
    glVertex(1050, 200)
    glVertex(1050, 250)
    glVertex(1150, 250)
    glVertex(1150, 200)
    glEnd()
    glColor(1,1,1)
    glRasterPos2i(1090, 225)
    text = "3"
    for i in text:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(str(i)))
    glColor(0,0,0)
    glBegin(GL_POLYGON)
    glVertex(1050, 300)
    glVertex(1050, 350)
    glVertex(1150, 350)
    glVertex(1150, 300)
    glEnd()
    glColor(1,1,1)
    glRasterPos2i(1090, 325)
    text = "4"
    for i in text:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(str(i)))
    glColor(0,0,0)
    glBegin(GL_POLYGON)
    glVertex(1050, 400)
    glVertex(1050, 450)
    glVertex(1150, 450)
    glVertex(1150, 400)
    glEnd()
    glColor(1,1,1)
    glRasterPos2i(1090, 425)
    text = "5"
    for i in text:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(str(i)))
    glColor(0,0,0)
    glBegin(GL_POLYGON)
    glVertex(1050, 500)
    glVertex(1050, 550)
    glVertex(1150, 550)
    glVertex(1150, 500)
    glEnd()
    glColor(1,1,1)
    glRasterPos2i(1090, 525)
    text = "6"
    for i in text:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(str(i)))
    glColor(0,0,0)
    glBegin(GL_POLYGON)
    glVertex(1050, 600)
    glVertex(1050, 650)
    glVertex(1150, 650)
    glVertex(1150, 600)
    glEnd()
    glColor(1,1,1)
    glRasterPos2i(1090, 625)
    text = "7"
    for i in text:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(str(i)))
    glFlush()
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
            r=g=b=1
            glColor(1,1,1)
            x = node_listX[node_counter]
            y = node_listY[node_counter]
            z = 50
            glColor(r, g, b)
            glBegin(GL_POLYGON)
            glVertex(x - z, y - z)
            glVertex(x + z, y - z)
            glVertex(x + z, y + z)
            glVertex(x - z, y + z)
            glEnd()
            glFlush()
            glColor(0, 0, 0)
            glBegin(GL_POLYGON)
            glVertex(x - 50, y - 50)
            glVertex(x + 50, y - 50)
            glVertex(x + 50, y + 50)
            glVertex(x - 50, y + 50)
            glEnd()
            list_counter+=1

        else:
            j = color_dict[list1[list_counter]]
            r = j[0]
            g= j[1]
            b= j[2]
            glColor(r,g,b)
            x = node_listX[node_counter]
            y=node_listY[node_counter]
            z=50
            while z:
                glColor(r, g, b)
                glBegin(GL_POLYGON)
                glVertex(x - z, y - z)
                glVertex(x + z, y - z)
                glVertex(x + z, y + z)
                glVertex(x - z, y + z)
                glEnd()
                glFlush()
                z-=1
                if r>0.5:
                    r-=0.05
                if g > 0.5:
                    g -= 0.05
                if b>0.5:
                    b -= 0.05
            node_counter+=1
            list_counter+=1


def Render():
    global color_change
    if color_change%150==0:
        glColor(1, 0, 0)
    elif color_change%100==0:
        glColor(0, 1, 0)
    elif color_change % 50 == 0:
        glColor(0, 0, 1)
    glRasterPos2i(450, 25)
    text = "Graph Coloring Problem"
    for i in text:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(str(i)))
    glRasterPos2i(1030, 75)
    text = "No. of Colors"
    for i in text:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(str(i)))
    glFlush()
    color_change+=1


if __name__ == '__main__':
    main()
