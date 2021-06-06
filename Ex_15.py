numSequence = input('Enter an input sequence :')
numList = numSequence.split(',')
even = []
odd = []
for x in range(len(numList)):
    if int(numList[x]) % 2 == 0:
        even.append[int(numList[x])]
    else : 
        odd.append[int(numList[x])]
print(f'Odd numbers are {odd}')
