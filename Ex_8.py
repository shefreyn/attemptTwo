inpSeq = str(input('Enter a comma seperated sequence of words:'))
inpSeqList = inpSeq.split(',')
print(inpSeqList)
for x in range(len(inpSeqList)):
    print(inpSeqList[x],end=',')