dictOP = {} 
dictNum = int(input('Enter a number'))
for counter in range(dictNum + 1):
    dictOP[counter]=counter*counter
print(dictOP)