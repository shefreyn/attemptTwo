whiteSeq = input('Enter a sentence with words seperated using spaces :')
whiteSeqList = whiteSeq.split(' ')
print(whiteSeqList)
for x in range(len(whiteSeqList)):
    print(whiteSeqList[x])
listSet = set(whiteSeqList)
print('list to set \n ', whiteSeqList)