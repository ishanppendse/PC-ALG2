import nltk
from nltk.tokenize import RegexpTokenizer
l=["BS19B002_Q1.txt","BS19B002_Q2.txt","BS19B002_Q3.txt","BS19B009_Q1.txt","BS19B009_Q2.txt","BS19B009_Q3.txt","BS19B012_Q1.txt","BS19B012_Q2.txt","BS19B012_Q3.txt","BS19B014_Q1.txt","BS19B014_Q2.txt","BS19B014_Q3.txt","BS19B020_Q1.txt","BS19B020_Q2.txt","BS19B020_Q3.txt","BS19B022_Q1.txt","BS19B022_Q2.txt","BS19B022_Q3.txt","BS19B023_Q1.txt","BS19B023_Q2.txt","BS19B023_Q3.txt","BS19B025_Q1.txt","BS19B025_Q2.txt","BS19B025_Q3.txt","BS19B028_Q1.txt","BS19B028_Q2.txt","BS19B028_Q3.txt","BS19B029_Q1.txt","BS19B029_Q2.txt","BS19B029_Q3.txt","BS19B030_Q1.txt","BS19B030_Q2.txt","BS19B030_Q3.txt","BS19B031_Q1.txt","BS19B031_Q2.txt","BS19B031_Q3.txt"]
for i in l:
    f=open(i,'r')
    text=f.read()
    text=text.lower()
    tokenizer = RegexpTokenizer(r'\w+')
    text = tokenizer.tokenize(text)
    print(text,'\n\n')
f.close()
