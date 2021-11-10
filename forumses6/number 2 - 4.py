#number2
import os
os.getcwd()
k = open("fifo.txt",mode='r',encoding='utf-8')
b = open("newtext.txt",mode="x",encoding = "utf-8")
s = k.read().split('\n')
counter=1
for s in s :
    x.write(str(counter)+' '+s+'\n')
    counter+=1
#number3
import os
os.getcwd()
filename=("fifo.txt")
mybook=open(os.getcwd()+'\\'+filename,'r')
myAll = mybook.read()
s = (myAll)
a = len(s.split())
c = len(s)
def av_word(s):
    r=c/a
    return r
r = av_word(s)
print("The average word is :",r,"word")
#number4
import os
os.getcwd()
stc=("mrmiyagi.txt")
ss=open(os.getcwd()+'\\'+stc,'r',encoding="utf-8")
sss=ss.read().split()
z = ["Mr.","Jr.","Mrs.","Ms.","Dr."]
n=''
for i in sss:
    if "!" not in i and "?" not in i:
        n+=(i + " ")
        if "." in i[-1] and i not in z:
            n+="\n"
        if "." in i.strip(".") and i not in z:
            pass
    else:
        n+=(i+"\n")

print(n)
