import nltk
from nltk.corpus import stopwords

st = set(stopwords.words('english'))

l = []
count={}
inp = input("Enter the text : ")
inp.strip()
text = inp.split()
for word in text:
    if word not in st:
        word = word.lower()
        word = word.replace(".","")
        word = word.replace("'","")
        word = word.replace("'s","")
        word = word.replace('"',"")
        word = word.replace(":","")
        word = word.replace(",","")
        word = word.replace(";","")
        word = word.replace("(","")
        word = word.replace(")","")
        flag = 0
        for i in l:
            if(i==word):
                count[word]+=1
                flag = 1
                break
        if(flag==0):
            count[word]=1
            l.append(word)
#print (count)

s = inp.split(".")
s.remove("")
score = {}
for i in s:
    score[i]=0
    n=0
    for j in i.split():
        if j not in st:
            j = j.lower()
            j = j.replace("'","")
            j = j.replace('"',"")
            j = j.replace("'s","")
            j = j.replace(":","")
            j = j.replace(";","")
            j = j.replace(",","")
            j = j.replace("(","")
            j = j.replace(")","")
            score[i] += count[j]
            n += 1
    score[i] /= n

print ("\nSummary:\n")
for i in s:
    if score[i] > 1.1:
        print (i,end=".")
