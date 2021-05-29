binaryInput = input('Enter comma seperated binary number, Eg - 1011 : ')
binaryInputList = binaryInput.split(',')
for x in range(len(binaryInputList)):
    if int(binaryInputList[x]) % 2 == 0:
        print(binaryInputList[x])