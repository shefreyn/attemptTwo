from typing import List


wordFreq = input('Enter a string to check frequency of words')
words = [] #list
dictCount = {}  #Dict
wordList = wordFreq.split(' ') #wordlist
wordSet = set(wordList) #wordSet
for setItem in wordSet:
    wordCount = 0                   # hello hi what is up
    for listItem in wordList:       # hello hello hi what is up
        if listItem == setItem:
            wordCount += 1 
    dictCount.update({setItem:wordCount})

for x in dictCount:
    print(x,dictCount[x])