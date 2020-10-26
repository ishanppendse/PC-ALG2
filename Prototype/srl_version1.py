import nltk
import nlpnet
from nltk.tokenize import sent_tokenize

text = ["BS19B002_Q1.txt", "BS19B002_Q2.txt", "BS19B002_Q3.txt", "BS19B009_Q1.txt",
"BS19B009_Q2.txt", "BS19B009_Q3.txt", "BS19B012_Q1.txt", "BS19B012_Q2.txt",
"BS19B012_Q3.txt", "BS19B014_Q1.txt", "BS19B014_Q2.txt", "BS19B014_Q3.txt",
"BS19B020_Q1.txt", "BS19B020_Q2.txt", "BS19B020_Q3.txt", "BS19B022_Q1.txt",
"BS19B022_Q2.txt", "BS19B022_Q3.txt",
"BS19B023_Q1.txt", "BS19B023_Q2.txt", "BS19B023_Q3.txt", "BS19B025_Q1.txt",
"BS19B025_Q2.txt", "BS19B025_Q3.txt", "BS19B028_Q1.txt", "BS19B028_Q2.txt",
"BS19B028_Q3.txt", "BS19B029_Q1.txt", "BS19B029_Q2.txt", "BS19B029_Q3.txt",
"BS19B030_Q1.txt", "BS19B030_Q2.txt", "BS19B030_Q3.txt", "BS19B031_Q1.txt",
"BS19B031_Q2.txt", "BS19B031_Q3.txt"]

text=text.lower()
text=sent_tokenize(text)
def punc(ftext):
    punctuations = '''!()-[]{};:'"\,<>/?@#$%^&*~.'''
    for i in punctuations:
        ftext=ftext.replace(i,'')
    return(ftext)
for i in range(len(text)):
    text[i]=punc(text[i])
print(text)

l1 = []
l2 = []
l3 = []
for i in range(int(len(text))):
    if(i % 3 == 0):
        l1.append(text[i])
    elif(i % 3 == 1):
        l2.append(text[i])
    else:
        l3.append(text[i])

tagger=nlpnet.SRLTagger()
A=tagger.tag(text)

def srl_group(A):
    P=[]
    A1=[]
    A2=[]
    V=[]
    for i,j in A:
        if(j=='A0'):
            A1.append(i)
        if(j=='A1'):
            A2.append(i)
        if(j=='V'):
            V.append(i)
    P.append(A1)
    P.append(A2)
    P.append(V)

b=[]
interlen=[]
c=[]
unionlen=[]
def intersection(l,m):
    for i in range(3):
        a=[]
        for word in l[i]:
            if(word in m[i]):
                a.append(word)
        b.append(a)
        interlen.append(len(b[i]))
    return(b)
b=intersection(l1,m1)
print(b,'\n',interlen)

def union(l,m):
    for i in range(3):
        c.append(list(set(l[i])|set(m[i])))
        unionlen.append(len(c[i]))
    return(c)
c=union(l1,m1)
print(c,'\n',unionlen)

Score=[]
score=0
for i in range(3):
    score=score+interlen[i]/unionlen[i]
Score.append(score)
print(Score)
