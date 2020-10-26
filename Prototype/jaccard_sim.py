import math
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 
ps = PorterStemmer() 
stop_words = set(stopwords.words('english')) 
def pre(files):
    lists = []
    for i in files:
        f = open(i, 'r')
        text = f.read()
        text = text.lower()
        tokenizer = RegexpTokenizer(r'\w+')
        text = tokenizer.tokenize(text)
        lists.append(text)
    for i in range(len(lists)):
        filtered_sentence = [w for w in lists[i] if not w in stop_words]
        lists[i]=filtered_sentence
    for docs in lists:
        for i in range(len(docs)):
            docs[i]=ps.stem(docs[i])
    return lists


def Freq(wordlist):
    freqmp = {}
    for word in wordlist:
        if word in freqmp:
            freqmp[word] += 1
        else:
            freqmp[word] = 1
    return freqmp


def Dot_Product(V1, V2):
    ans = 0.0
    for word in V1:
        if word in V2:
            ans += (V1[word]*V2[word])
    return ans


def jaccard_sim(V1, V2):
    ans = 0.0
    ans = (Dot_Product(V1, V2)) / (Dot_Product(V1,V1)+Dot_Product(V2,V2)-Dot_Product(V1,V2))
    return ans


def Sim(wordlist1, wordlist2):
    freqmp1 = Freq(wordlist1)
    freqmp2 = Freq(wordlist2)
    return jaccard_sim(freqmp1, freqmp2)


def Sort_Tuple(tup):
    tup.sort(key=lambda x: x[1], reverse=True)
    return tup


l = ["BS19B002_Q1.txt", "BS19B002_Q2.txt", "BS19B002_Q3.txt", "BS19B009_Q1.txt", "BS19B009_Q2.txt", "BS19B009_Q3.txt", "BS19B012_Q1.txt", "BS19B012_Q2.txt", "BS19B012_Q3.txt", "BS19B014_Q1.txt", "BS19B014_Q2.txt", "BS19B014_Q3.txt", "BS19B020_Q1.txt", "BS19B020_Q2.txt", "BS19B020_Q3.txt", "BS19B022_Q1.txt", "BS19B022_Q2.txt", "BS19B022_Q3.txt",
     "BS19B023_Q1.txt", "BS19B023_Q2.txt", "BS19B023_Q3.txt", "BS19B025_Q1.txt", "BS19B025_Q2.txt", "BS19B025_Q3.txt", "BS19B028_Q1.txt", "BS19B028_Q2.txt", "BS19B028_Q3.txt", "BS19B029_Q1.txt", "BS19B029_Q2.txt", "BS19B029_Q3.txt", "BS19B030_Q1.txt", "BS19B030_Q2.txt", "BS19B030_Q3.txt", "BS19B031_Q1.txt", "BS19B031_Q2.txt", "BS19B031_Q3.txt"]
l1 = []
l2 = []
l3 = []
for i in range(int(len(l))):
    if(i % 3 == 0):
        l1.append(l[i])
    elif(i % 3 == 1):
        l2.append(l[i])
    else:
        l3.append(l[i])

print("Q1:")
arr1 = pre(l1)
ans1 = [[None for i in range(len(arr1))] for j in range((len(arr1)))]
for i in range(len(arr1)):
    for j in range(i, len(arr1)):
        ans1[i][j] = Sim(arr1[i], arr1[j])
        ans1[j][i] = ans1[i][j]
for r in ans1:
    for c in r:
        print("%.4f" % c, end=" ")
    print()
ans = []
for i in range(len(ans1)):
    for j in range(i+1, len(ans1[i])):
        tup = (i+1, j+1), (ans1[i][j])
        ans.append(tup)
Sort_Tuple(ans)
for i in range(4):
    print("Doc %s and Doc %s = %f" % (l1[ans[i][0][0]-1], l1[ans[i][0][1]-1], ans[i][1]))
# BS12 and BS31 possible
print("Q2:")
arr2 = pre(l2)
ans2 = [[None for i in range(len(arr2))] for j in range((len(arr2)))]
for i in range(len(arr2)):
    for j in range(i, len(arr2)):
        ans2[i][j] = Sim(arr2[i], arr2[j])
        ans2[j][i] = ans2[i][j]
for r in ans2:
    for c in r:
        print("%.4f" % c, end=" ")
    print()
ans = []
for i in range(len(ans2)):
    for j in range(i+1, len(ans2[i])):
        tup = (i+1, j+1), (ans2[i][j])
        ans.append(tup)
Sort_Tuple(ans)
for i in range(4):
    print("Doc %s and Doc %s = %f" % (l2[ans[i][0][0]-1], l2[ans[i][0][1]-1], ans[i][1]))
# BS25 and BS31 possible/definite
print("Q3:")
arr3 = pre(l3)
ans3 = [[None for i in range(len(arr3))] for j in range((len(arr3)))]
for i in range(len(arr3)):
    for j in range(i, len(arr3)):
        ans3[i][j] = Sim(arr3[i], arr3[j])
        ans3[j][i] = ans3[i][j]
for r in ans3:
    for c in r:
        print("%.4f" % c, end=" ")
    print()
ans = []
for i in range(len(ans3)):
    for j in range(i+1, len(ans3[i])):
        tup = (i+1, j+1), (ans3[i][j])
        ans.append(tup)
Sort_Tuple(ans)
for i in range(4):
    print("Doc %s and Doc %s = %f" % (l3[ans[i][0][0]-1], l3[ans[i][0][1]-1], ans[i][1]))
# BS02 and BS25
