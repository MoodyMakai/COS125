#HW 8 Moody-Broen
#Recieved help from: Zac, Monica Agneta (140 MLA), and Chloe Hodgden (140 MLA)
import random
from graphics import *
L = 512
H = 512
win = GraphWin("Window",L, H)
Pts = []
def points():
    for a in range(300):
        x = random.randint(0,(H-1))
        y = random.randint(0,(L-1))
        Pts.append([x,y])
def pDraw():
    for x in Pts:
        circ = Circle(Point(x[0],x[1]),2)
        circ.setFill("red")
        circ.draw(win)
def Pcheck(L,H,X,Y):
    n = 0
    for x in Pts:
        if (x[0] >= X and x[0] <= X+L) and (x[1] >= Y and x[1] <= Y+H):
            n = n+1
    print(n)
    return(n)
def slicer(x,y,l,h):
    print(x,y,l,h)
    a = []
    b = []
    if Pcheck(l,h,x,y) == 1:
        print('1 point')
        '''make rect white'''
        rec = Rectangle(Point(x,y),Point(l+x,h+y))
        rec.setOutline('black')
        rec.setFill('white')
        rec.draw(win)
    elif Pcheck(l,h,x,y) == 0:
        print('0 point')
        '''make rect grey'''
        rec = Rectangle(Point(x,y),Point(l+x,h+y))
        rec.setOutline('black')
        rec.setFill('grey')
        rec.draw(win)
    else:
        print(Pcheck(l,h,x,y))
        for i in Pts:
            print('TESTING FOR')
            if ((i[0] >= x) and (i[0] <= x+l)) and ((i[1] >= y) and (i[1] <= y+h)):
                print('Testing if')
                a.append(i[0])
                b.append(i[1])
        deltX = max(a) - min(a)
        deltY = max(b) - min(b)
        if deltX >= deltY:
            '''split vert'''
            slicer(x,y,l/2,h)
            slicer(x+(l/2),y,l/2,h)
            print('X called')
        else:
            '''split horiz'''
            slicer(x,y,l,h/2)
            slicer(x,y+(h/2),l,h/2)
            print('Y called')
points()   
slicer(0,0,L,H)
pDraw()
win.getMouse() # Pause to view result
win.close()    # Close window when done
