#Makai Moody-Broen
#HW 5
import random

def main():
    print('uniq list normal test')
    UniqueRandList(3,18,15)
    print('b<a')
    UniqueRandList(10,3,7)
    print('amt < range')
    UniqueRandList(3,5,5)
    print('amt > range')
    UniqueRandList(3,10,5)
    print('amt < range')
    UniqueRandList(0,1,3)
    print('uniq 0 test')
    UniqueRandList(0,0,0)
    print('median test odd')
    FindMedian([2.4,32.5,55.2,3.4,5.3])
    print('median test even')
    FindMedian([2.4,32.5,55.2,3.4])
    print('median empty test')
    FindMedian([])
    print('Add test L1 < L2')
    EleAdd([1,2],[1,2,3,4,5,6,7,8])
    print('Add test L1 > L2')
    EleAdd([1,32,402,44,1],[1,2])
    print('Add test L1 = L2')
    EleAdd([1,2,3,4],[1,2,3,4])
    print('Add test both empty')
    EleAdd([],[])
    print('Add test one empty')
    EleAdd([1,2,3,4],[])

def UniqueRandList(a, b, amt):
    L = []
    if amt > (b-a):
        print(L)
    elif amt < (b-a):
        print(L)
    elif b < a:
        print(L)
    elif amt == (b-a):
        while len(L) < amt:
            z = random.randint(a,b)
            if z not in L:
                L.append(z)     
        print(L)

def FindMedian(arr):
    if arr == []:
        print([])
    elif len(arr)%2 == 0:
        x = len(arr)//2
        y = (len(arr)//2) - 1
        print((arr[x]+arr[y])/2)
    else:
        print(arr[len(arr)//2])

def EleAdd(L1, L2):
    L = []
    if len(L1) > len(L2):
        for x in range(len(L2)):
            y = L1[x] + L2[x]
            L.append(y)
        z = len(L1) - len(L2)
        L1.reverse()
        for x in range(z-1,-1,-1):
            L.append(L1[x])
    elif len(L1) < len(L2):
        for x in range(len(L1)):
            y = L1[x] + L2[x]
            L.append(y)
        z = len(L2) - len(L1)
        L2.reverse()
        for x in range(z-1,-1,-1):
            L.append(L2[x])
    elif len(L1) == len(L2):
        for x in range(len(L1)):
            y = L1[x] + L2[x]
            L.append(y)
    print(L)

main()