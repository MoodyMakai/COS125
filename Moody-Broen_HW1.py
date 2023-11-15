#Makai Moody-Broen

ReqO = 1
ReqS = 2.56
ReqL = 9
ReqP = 14.44


print('Hello, Please enter the length and width of your garden in meters.')
L = int(input())
W = int(input())
D = L*W
print('The dimensions of this garden is ' + str(D) + ' Meters')


print('Now please indicate the percentage breakdown of the following crop.')
print('Onion')
O = float(input())
print('Spinach')
S = float(input())
print('Lettuce')
L = float(input())
print('Peppers')
P = float(input())
Tot = O+S+L+P
if Tot == 1:
    pass
else:
    print('The total percentages did not add up')

TotO = ((D*O)/ReqO)*100
TotS = ((D*S)/ReqS)*100
TotL = ((D*L)/ReqL)*100
TotP = ((D*P)/ReqP)*100


print(f' The total allocation of onions equals {TotO:.1f} in {(D*O):.1f} Sq m')
print(f' The total allocation of spinach equals {TotS:.1f} in {(D*S):.1f} Sq m')
print(f' The total allocation of lettuce equals {TotL:.1f} in {(D*L):.1f} Sq m')
print(f' The total allocation of peppers equals {TotP:.1f} in {(D*P):.1f} Sq m')