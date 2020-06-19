from nltk.tokenize import sent_tokenize
from lev1 import levens
import numpy as np
from time import perf_counter

start=perf_counter()


l = ["BS19B002_Q1.txt", "BS19B002_Q2.txt", "BS19B002_Q3.txt", "BS19B009_Q1.txt", "BS19B009_Q2.txt", "BS19B009_Q3.txt",
     "BS19B012_Q1.txt", "BS19B012_Q2.txt", "BS19B012_Q3.txt", "BS19B014_Q1.txt", "BS19B014_Q2.txt", "BS19B014_Q3.txt",
     "BS19B020_Q1.txt", "BS19B020_Q2.txt", "BS19B020_Q3.txt", "BS19B022_Q1.txt", "BS19B022_Q2.txt", "BS19B022_Q3.txt",
     "BS19B023_Q1.txt", "BS19B023_Q2.txt", "BS19B023_Q3.txt", "BS19B025_Q1.txt", "BS19B025_Q2.txt", "BS19B025_Q3.txt",
     "BS19B028_Q1.txt", "BS19B028_Q2.txt", "BS19B028_Q3.txt", "BS19B029_Q1.txt", "BS19B029_Q2.txt", "BS19B029_Q3.txt",
     "BS19B030_Q1.txt", "BS19B030_Q2.txt", "BS19B030_Q3.txt", "BS19B031_Q1.txt", "BS19B031_Q2.txt", "BS19B031_Q3.txt"]
lbig = []
for i in l:
    f = open(i, 'r')
    text = f.read()
    text = text.lower()
    text = sent_tokenize(text)


    def punc(text):
        punctuations = '''!()-[]{};:'"\,<>/?@#$%^&*~. =+-|`\n'''
        for i in range(len(text)):
            strb = ''
            for char in text[i]:
                if char not in punctuations:
                    strb = strb + char
                else:
                    strb = strb
            text[i] = strb
        return (text)


    text = punc(text)
    # print(text,'\n\n')
    lbig.append(text)

f.close()

l1 = list(lbig[3 * i] for i in range(0, 12))
l2 = list(lbig[(3 * i) + 1] for i in range(0, 12))
l3 = list(lbig[(3 * i) + 2] for i in range(0, 12))

for li in [l1,l2,l3]:
    print('Question Starts')
    print('Mean no. of Sentences=%f'%np.array(list(len(doc) for doc in li)).mean())
    for x in range(0,len(li)-1):
        for y in range(x+1,len(li)):
            doc1=li[x]
            doc2=li[y]
            len1=len(doc1)
            len2=len(doc2)
            matrix = np.zeros((len1, len2))
            for i in range(0, len1):
                for j in range(0, len2):
                    matrix[i, j] = levens(doc1[i], doc2[j])
            # print(matrix)
            if matrix.min()<0.5:
                print(x,y)
                print(matrix.min())
                loc = np.where(matrix < 0.5)
                pos = np.array([loc[0], loc[1]]).transpose()
                for i in pos:
                    print(doc1[i[0]], doc2[i[1]], matrix[i[0], i[1]], '\n\n')

end=perf_counter()
print('Time= %f'%(end-start))


# print(l1[0][loc[0][0]], l1[1][loc[1][0]])
# print(type(loc))
# print(loc)
