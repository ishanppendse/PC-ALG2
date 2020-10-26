import math
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from glob import glob
import os
ps = PorterStemmer() 
stop_words = set(stopwords.words('english')) 
lemmatizer = WordNetLemmatizer()

def pre(files):
    lists = []
    enc="utf-8"
    for i in files:
        f = open(i, 'r',encoding=enc)
        text = f.read()
        text = text.lower()
        tokenizer = RegexpTokenizer(r'\w+')
        text = tokenizer.tokenize(text)
        lists.append(text)
    for i in range(len(lists)):
        filtered_sentence = [w for w in lists[i] if not w in stop_words]
        lists[i]=filtered_sentence
    #for docs in lists:
    #    for i in range(len(docs)):
    #        docs[i]=ps.stem(docs[i])
    for docs in lists:
        for i in range(len(docs)):
            docs[i]=lemmatizer.lemmatize(docs[i])
    return lists

def Pos(m):
   a=[];
   nouns1=[]
   others1=[]
   verbs1=[]
   adjectives1=[]
   adverbs1=[]
   for i,j in pos_tag(m):
     if (j == 'NN' or j == 'NNP' or j == 'NNS' or j == 'NNPS'):
             nouns1.append(i)
     if (j == 'JJ' or j == 'JJR' or j == 'JJS'):
             adjectives1.append(i)
     if (j == 'VB' or j == 'VBG' or j == 'VBD' or j == 'VBN' or j == 'VBP' or j == 'VBz'):
             verbs1.append(i)
     if(j=='RB' or j=='RBR' or j=='RBS'):
             adverbs1.append(i)
     if(j=='CC' or j=='CD' or j=='DT' or j=='EX' or j=='FW' or j=='LS' or j=='MD' or j=='PDT' or j=='UH'):
             others1.append(i)
   a.append(nouns1)
   a.append(others1)
   a.append(verbs1)
   a.append(adjectives1)
   a.append(adverbs1)
   return a;

def Pos_CosSim(arr1):
   for i in range(len(arr1)):
     arr1[i]=Pos(arr1[i])
   nouns=[]
   others=[]
   verbs=[]
   adjectives=[]
   adverbs=[]
 
   idfnouns={}
   idfothers={}
   idfverbs={}
   idfadjectives={}
   idfadverbs={}

   for i in range(len(arr1)):
     nouns.append(arr1[i][0])
     others.append(arr1[i][1])
     verbs.append(arr1[i][2])
     adjectives.append(arr1[i][3])
     adverbs.append(arr1[i][4])

   idfnouns=Idf(nouns)
   idfothers=Idf(others)
   idfverbs=Idf(verbs)
   idfadjectives=Idf(adjectives)
   idfadverbs=Idf(adverbs)

   #print(0.4*Sim(arr1[0][0],arr1[7][0],idfnouns)+0.2*Sim(arr1[0][1],arr1[7][1],idfothers)+0.2*Sim(arr1[0][2],arr1[7][2],idfverbs)+0.1*Sim(arr1[0][3],arr1[7][3],idfadjectives)+0.1*Sim(arr1[0][4],arr1[7][4],idfadverbs))
   #print(arr1[0][0])
   #print(arr1[7][0])
   ans1= [[None for i in range(len(arr1))] for j in range((len(arr1)))]
   for i in range(len(arr1)):
    for j in range(i, len(arr1)):
        ans1[i][j] = 0.4*Sim(arr1[i][0],arr1[j][0],idfnouns)+0.2*Sim(arr1[i][1],arr1[j][1],idfothers)+0.2*Sim(arr1[i][2],arr1[j][2],idfverbs)+0.1*Sim(arr1[i][3],arr1[j][3],idfadjectives)+0.1*Sim(arr1[i][4],arr1[j][4],idfadverbs)
        ans1[j][i] = ans1[i][j]
  
   ans = []
   for i in range(len(ans1)):
    for j in range(i+1, len(ans1[i])):
        tup = (i+1, j+1), (ans1[i][j])
        ans.append(tup)  
   Sort_Tuple(ans)
   #for i in range(4):
   # print("Doc %s and Doc %s = %f" % (l2[ans[i][0][0]-1], l2[ans[i][0][1]-1], ans[i][1]))
   return ans1

   
   



def Idf(doclist):    
 terms = set()
 for doc in doclist:
    for item in doc:
         terms.add(item)
 idf = dict()
 temp = dict()
 for term in terms:
    temp[term] = 0
    for doc in doclist:
        if term in doc:
           temp[term]+=1
    idf[term] = 1+math.log(20/temp[term])
 return idf

def Freq(wordlist,idf):
    freqmp = {}
    a=len(wordlist)
    for word in wordlist:
        if word in freqmp:
            freqmp[word] += 1
        else:
            freqmp[word] = 1
    for word in freqmp:
        freqmp[word]=freqmp[word]/a
        freqmp[word]=freqmp[word]*idf[word]
    return freqmp


def Dot_Product(V1, V2):
    ans = 0.0
    for word in V1:
        if word in V2:
            ans += (V1[word]*V2[word])
    
    return ans


def Cosine_Sim(V1, V2):
    ans = 0.0
    if(len(V1)==0 or len(V2)==0):
      return 0
    else:
     ans = (Dot_Product(V1, V2)) / \
        (math.sqrt(Dot_Product(V1, V1)*Dot_Product(V2, V2)))
    return ans


def Sim(wordlist1, wordlist2,idf):
    if(len(wordlist1)==0 or len(wordlist2)==0):
     return 0
    else:
     freqmp1 = Freq(wordlist1,idf)
     freqmp2 = Freq(wordlist2,idf)
     return Cosine_Sim(freqmp1, freqmp2)


def Sort_Tuple(tup):
    tup.sort(key=lambda x: x[1], reverse=True)
    return tup

def final(all,pre,ans):
    docs = list(zip(all, pre))
    finallist = []
    i = 0
    while i < len(docs) - 1:
        j = i + 1
        while j < len(docs):
            score=ans[i][j]
            finallist.append([score,[docs[i][0],docs[j][0]]])
            j += 1
        i+=1
    return(finallist)

#l = ["BS19B002_Q1.txt", "BS19B002_Q2.txt", "BS19B002_Q3.txt", "BS19B009_Q1.txt", "BS19B009_Q2.txt", "BS19B009_Q3.txt", "BS19B012_Q1.txt", "BS19B012_Q2.txt", "BS19B012_Q3.txt", "BS19B014_Q1.txt", "BS19B014_Q2.txt", "BS19B014_Q3.txt", "BS19B020_Q1.txt", "BS19B020_Q2.txt", "BS19B020_Q3.txt", "BS19B022_Q1.txt", "BS19B022_Q2.txt", "BS19B022_Q3.txt",
#    "BS19B023_Q1.txt", "BS19B023_Q2.txt", "BS19B023_Q3.txt", "BS19B025_Q1.txt", "BS19B025_Q2.txt", "BS19B025_Q3.txt", "BS19B028_Q1.txt", "BS19B028_Q2.txt", "BS19B028_Q3.txt", "BS19B029_Q1.txt", "BS19B029_Q2.txt", "BS19B029_Q3.txt", "BS19B030_Q1.txt", "BS19B030_Q2.txt", "BS19B030_Q3.txt", "BS19B031_Q1.txt", "BS19B031_Q2.txt", "BS19B031_Q3.txt"]
all_docs=sorted(glob(os.path.join(r'D:\PC-ALG2-master\PC-ALG2-master\Prototype\temp_shortlist','*.txt')))
print("Q1:")
pre_docs = pre(all_docs)
ans=Pos_CosSim(pre_docs)

l1=final(all_docs,pre_docs,ans)
l1.sort(key=lambda x:x[0], reverse=True)
for i in range(0,10):
    print(l1[i][0])
    print(l1[i][1][0])
    print(l1[i][1][1])
    
