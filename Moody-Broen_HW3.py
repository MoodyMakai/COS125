#Makai Moody-Broen
#Recieved help from: Professor Zach 
import math
import random
print('What is the radius of this circle')
r = int(input())
c = [r-1,r-1]
def delta(x,y):
    delt = math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)
    return delt
def delta2(x,y):
    i = (y-(y+1))/(x-(x+1))
    return i


for y in range(r*2-1):
    for x in range(r*2-1):
        p = [y,x]
        d = delta(c,p)
        q = delta2(x,y)
        if d > r:
            print('   ',end='')
        elif x == r-1:
            if y == r-1:
                print(' + ',end='')
            else:
                print(' | ', end='')
        elif y == r-1:
                print(' - ',end='')
        elif x-(r-1) == -1 * (y-(r-1)) :
            print(' / ', end='')
        elif x == y:
            print(' \ ', end='')
        else:
            print(' * ',end = '')
    print()  


        




