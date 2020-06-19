from nltk.tokenize import sent_tokenize
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


def condense(s,d):
    outlist=[]
    j=-1
    for i in range(0,len(s)):
        if i%d==0:
            outlist.append(s[i])
            j+=1
        else:
            outlist[j]=outlist[j]+s[i]
    return outlist


def levens(a, b, thresh):
    if len(a) < len(b):
        a, b = b, a
    # We will have the length of the smaller string as the number of cols, this makes space complexity as min(len(a),
    # len(b))
    lena = len(a)
    lenb = len(b)
    even = list(range(0, lenb + 1))
    odd = list(range(0, lenb + 1))
    temp = 1
    indic=0
    while indic==0 and temp <= lena:
        count = 0
        if temp % 2:
            while count <= lenb:
                if count == 0:
                    odd[0] = temp
                else:
                    val = (a[temp - 1] != b[count - 1])
                    odd[count] = min(odd[count - 1] + 1, even[count] + 1, even[count - 1] + val)
                count += 1
            if min(odd)/len(a)>thresh:
                indic+=1
        else:
            while count <= lenb:
                if count == 0:
                    even[0] = temp
                else:
                    val = (a[temp - 1] != b[count - 1])
                    even[count] = min(even[count - 1] + 1, odd[count] + 1, odd[count - 1] + val)
                count += 1
            if min(even)/len(a)>thresh:
                indic+=1
        temp += 1
    if indic==0:
        if lena % 2:
            return odd[-1] / lena
        else:
            return even[-1] / lena
    else:
        return(1)


def main(thresh,div):
    for li in [l1, l2, l3]:
        for doc in li:
            for i in range(0, len(doc)):
                doc[i] = condense(doc[i], div)
    for li in [l1, l2, l3]:
        print('Question Starts')
        print('Mean no. of Sentences=%f' % np.array(list(len(doc) for doc in li)).mean())
        for x in range(0, len(li) - 1):
            for y in range(x + 1, len(li)):
                doc1 = li[x]
                doc2 = li[y]
                len1 = len(doc1)
                len2 = len(doc2)
                matrix = np.zeros((len1, len2))
                for i in range(0, len1):
                    for j in range(0, len2):
                        matrix[i, j] = levens(doc1[i], doc2[j],thresh)
                # print(matrix)
                if matrix.min() < thresh:
                    print(x, y)
                    print(matrix.min())
                    loc = np.where(matrix < thresh)
                    pos = np.array([loc[0], loc[1]]).transpose()
                    for i in pos:
                        print(doc1[i[0]], doc2[i[1]], matrix[i[0], i[1]], '\n\n')

main(0.7,2)

end=perf_counter()
print('Time= %f'%(end-start))
