lines = str(input('Enter multiple lines seperated by a comma'))
lineList = lines.split(', ')
print(lineList)
for x in range(len(lineList)):
    print(lineList[x].upper())
    