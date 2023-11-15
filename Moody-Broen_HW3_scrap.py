print('What is the radius of this circle')
r = int(input())
d = 2*r
def filler():
    y=0
    x = ' * '
    e = 0
    rem = (d/2) - 4
    while e < rem:
        while y < d:
                y=y+1
                x = x +' * '
                while y == int((d/2)-1):
                    y=y+1
                    x = x+' | '
        print(x)
        e=e+1
def midLine():
    y=0
    x = ' - '
    while y < d:
            y=y+1
            x = x +' - '
            while y == int((d/2)-1):
                y=y+1
                x = x+' + '
    print(x)
def firstLine():
    y=0
    x = ''
    while y < d:
        y=y+1
        if y == int((1/2)*d):
             x = x+' | '
        if y <= int((1/3)*d):
             x=x+'   '
        if y >= int((1/3)*d) and y < int((2/3)*d):
             x=x+' * '
        if y >= int((2/3)*d):
             x = x+'   '
    print(x)
def medLine():
    y=0
    x = ''
    while y < d:
        y=y+1
        if y == int((1/2)*d):
             x = x+' | '
        if y <= int((1/4)*d):
             x=x+'   '
        if y >= int((1/4)*d) and y < int((3/4)*d):
             x=x+' * '
        if y >= int((3/4)*d):
             x = x+'   ' 
    print(x)
    y=0
    x = ''
    while y < d:
        y=y+1
        if y == int((1/2)*d):
             x = x+' | '
        if y <= int((1/6)*d):
             x=x+'   '
        if y >= int((1/6)*d) and y < int((5/6)*d):
             x=x+' * '
        if y >= int((5/6)*d):
             x = x+'   '
    print(x)
    y=0
    x = ''
    while y < d:
        y=y+1
        if y == int((1/2)*d):
             x = x+' | '
        if y <= int((1/8)*d):
             x=x+'   '
        if y >= int((1/8)*d) and y < int((7/8)*d):
             x=x+' * '
        if y >= int((7/8)*d):
             x = x+'   '
    print(x)
    y=0
    x = ''
    while y < d:
        y=y+1
        if y == int((1/2)*d):
             x = x+' | '
        if y <= int((1/12)*d):
             x=x+'   '
        if y >= int((1/12)*d) and y < int((11/12)*d):
             x=x+' * '
        if y >= int((11/12)*d):
             x = x+'   '         
    print(x)
    y=0
    x = ''
    while y < d:
        y=y+1
        if y == int((1/2)*d):
             x = x+' | '
        if y <= int(1):
             x=x+'   '
        if y >= int(1) and y < int(d-1):
             x=x+' * '
        if y >= int(d-1):
             x = x+'   '         
    print(x)
def botLine():
    y=0
    x = ''
    while y < d:
        y=y+1
        if y == int((1/2)*d):
             x = x+' | '
        if y <= int(1):
             x=x+'   '
        if y >= int(1) and y < int(d-1):
             x=x+' * '
        if y >= int(d-1):
             x = x+'   '         
    print(x)
    y=0
    x = ''
    while y < d:
        y=y+1
        if y == int((1/2)*d):
             x = x+' | '
        if y <= int((1/12)*d):
             x=x+'   '
        if y >= int((1/12)*d) and y < int((11/12)*d):
             x=x+' * '
        if y >= int((11/12)*d):
             x = x+'   '
    print(x)
    y=0
    x = ''
    while y < d:
        y=y+1
        if y == int((1/2)*d):
             x = x+' | '
        if y <= int((1/8)*d):
             x=x+'   '
        if y >= int((1/8)*d) and y < int((7/8)*d):
             x=x+' * '
        if y >= int((7/8)*d):
             x = x+'   '
    print(x)
    y=0
    x = ''
    while y < d:
        y=y+1
        if y == int((1/2)*d):
             x = x+' | '
        if y <= int((1/6)*d):
             x=x+'   '
        if y >= int((1/6)*d) and y < int((5/6)*d):
             x=x+' * '
        if y >= int((5/6)*d):
             x = x+'   '
    print(x)
    y=0
    x = ''
    while y < d:
        y=y+1
        if y == int((1/2)*d):
             x = x+' | '
        if y <= int((1/4)*d):
             x=x+'   '
        if y >= int((1/4)*d) and y < int((3/4)*d):
             x=x+' * '
        if y >= int((3/4)*d):
             x = x+'   ' 
    print(x)
     
firstLine()
medLine()
filler()
midLine()
filler()
botLine()
firstLine()