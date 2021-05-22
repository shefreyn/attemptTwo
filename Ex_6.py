import math
C = 50
H = 30

print("Here's the Formulae \n")
print('Q = square root of [(2 x C x D) / H]')

valueD = str(input('Enter comma seperated values of D : '))
valueDlist = valueD.split(',')
print(valueDlist)
print(len(valueDlist))

for x in range(len(valueDlist)):
    D = int(valueDlist[x])
    Q = math.sqrt((2*C*D)/H)
    Q = round(Q)
    print(f"Value of {D} with the formula is {Q}")