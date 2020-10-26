import os
from glob import glob
import math
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
ps = PorterStemmer()
stop_words = set(stopwords.words('english'))
from nltk.corpus import wordnet
import shutil

def pre(files):
    lists = []
    enc = 'utf-8'
    for i in files:
        f = open(i, 'r', encoding= enc)
        text = f.read()
        text = text.lower()
        tokenizer = RegexpTokenizer(r'\w+')
        text = tokenizer.tokenize(text)
        lists.append(text)
    for i in range(len(lists)):
        filtered_sentence = [w for w in lists[i] if not w in stop_words]
        lists[i]=filtered_sentence
    for i in range(len(lists)):
        lists[i]=vocab(lists[i])
    return lists


def vocab(li):
    voc = []
    for word in li:
        for syn in wordnet.synsets(word):
            for l in syn.lemmas():
                voc.append(l.name())
    voc = set(voc)
    return(voc)


def eval(v1,v2):
    return((len(v1 & v2))/min(len(v1),len(v2)))


all_docs=[]
for i in [r"C:\Users\hp\PycharmProjects\CSD\version_2\pan-plagiarism-corpus-2011\pan-plagiarism-corpus-2011\external-detection-corpus\source-document",r"C:\Users\hp\PycharmProjects\CSD\version_2\pan-plagiarism-corpus-2011\pan-plagiarism-corpus-2011\external-detection-corpus\suspicious-document"]:
    for j in ['part1','part2','part3','part4']:
        all_docs += sorted(glob(os.path.join(i,j,'*.txt')))
pre_docs = pre(all_docs)


def final(all,pre):
    docs = list(zip(all, pre))
    finallist = []
    i = 0
    while i < len(docs) - 1:
        j = i + 1
        while j < len(docs):
            score=eval(docs[i][1], docs[j][1])
            finallist.append([score,[docs[i][0],docs[j][0]]])
            j += 1
        i+=1
    return(finallist)


l1 = final(all_docs,pre_docs)
l1.sort(key=lambda x:x[0], reverse=True)
l2=[]
i=0
while len(l2)<200:
    l2.append(l1[i][1][0])
    l2.append(l1[i][1][1])
    l2=list(set(l2))
    i+=1
for f in l2:
    shutil.copy(f,r"C:\Users\hp\PycharmProjects\CSD\version_2\preprocessed_docs")







