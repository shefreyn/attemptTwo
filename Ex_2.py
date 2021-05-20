inputfact = 0
fact=1
noOfFact = 0
numFact = int(input('No of times you want to perform a factorial : '))
factArray = []

for x in range(numFact):
    factNumber = int(input('Enter your factorial Number : '))
    factArray.append(factNumber)


for x in factArray:
    inputfact = x
    for i in range(1,inputfact+1):
        fact = fact * i
    print(fact)
    fact=1





