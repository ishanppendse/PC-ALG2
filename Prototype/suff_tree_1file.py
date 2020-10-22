import nltk
from suffix_trees import STree
from nltk.tokenize import RegexpTokenizer
import numpy as np

def pre(files):
    lists = []
    for i in files:
        f = open(i, 'r')
        text = f.read()
        text = text.lower()
        tokenizer = RegexpTokenizer(r'\w+')
        text = tokenizer.tokenize(text)
        lists.append(text)
        return lists

f=open("BS19B012_Q1.txt",'r')
text1=f.read()
text1=text1.lower()
tokenizer = RegexpTokenizer(r'\w+')
text1 = tokenizer.tokenize(text1)
s1=""
for i in text1:
    s1+=i
# print(s1)

f=open("BS19B031_Q1.txt",'r')
text2=f.read()
text2=text2.lower()
tokenizer = RegexpTokenizer(r'\w+')
text2 = tokenizer.tokenize(text2)
s2=""
for i in text2:
    s2+=i
# print(s2)

mark=np.zeros(len(text2))
k=4
temp=""
st=STree.STree(s1)

for i in range(len(text2)-k):
    temp=""
    for j in range(k):
        temp+=text2[i+j]
    if st.find(temp)!=-1:
        for j in range(k):
            mark[i+j]=1
ans=""
for i in range(len(text2)):
    if mark[i]==1:
        ans+=text2[i]
        ans+=" "
    else:
        if ans!="":
            print(ans)
            ans=""
