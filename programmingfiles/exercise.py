import os
os.getcwd()
mybook=open("fifo.txt","r")
myAll = mybook.read()
#funtion
Str=(myAll)
def countword(Str):
    myWord = {}
    for word in Str.split():
        myWord[word] = myWord.get(word,0)+1
    return myWord
myDict=countword(Str)
print("These are the HAPAX:")
for key in myDict:
    if myDict[key]==1:
        print(myDict[key],key)
