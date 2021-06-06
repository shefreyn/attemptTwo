import operator
tupleList = []

noOfEmployees = int(input('Enter the number of employees : '))
for noOftimes in range(noOfEmployees):
    io = input('Enter name,age and height :')
    ioSplit = io.split(',')
    ioSplit = tuple(ioSplit)
    tupleList.append(ioSplit)
tupleList.sort(key=operator.itemgetter(0,1,2))
print(tupleList)