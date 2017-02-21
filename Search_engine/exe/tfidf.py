from sklearn.feature_extraction.text import TfidfVectorizer
import jieba
from hanziconv import HanziConv
import sys
import os
from collections import Counter
import json
import deepdish as dd
import numpy as np
from scipy.sparse import csr_matrix, find
import scipy.sparse as sp
import heapq
import bottleneck
import csv

#找term-doc matrix 的sparse matrix 、 term對應編號 以及 各個term的idf
'''
f=open('C:\\Users\\Dannie\\Desktop\\source\\document.txt','r', encoding = 'UTF-8')
term=[]
num=0
for data in f.readlines():
    transform=HanziConv.toSimplified(data)#轉成簡體
    seg_list = jieba.cut(transform, cut_all=False)#把文章變成很多term
    term.append(" ".join(seg_list)) #把term變成一句用空白鍵隔開的句子，方便分析
    print("目前正在",num)#查看我跑到哪了
    num=num+1
    
#上面做完後就會有很多term組成的matrix
#ex: term[0]代表第一篇文章裡面所有term以空白隔開的句子
#下面是做doc tf-idf
vectorizer = TfidfVectorizer(min_df=1)
X = vectorizer.fit_transform(term)
idf = vectorizer.idf_
termname=vectorizer.get_feature_names()
dd.io.save('idf.h5', idf)#存idf
dd.io.save('sparse.h5', X)#存tf-idf的sparse matrix
dd.io.save('termname.h5', vectorizer.get_feature_names())#依照term的內容(就是中文片段)排列
#d = dd.io.load('C:\\Users\\Dannie\\Desktop\\source\\idf.h5')#各個term的idf
#d = dd.io.load('C:\\Users\\Dannie\\Desktop\\source\\sparse.h5')#tert-doc matrix 的sparse matrix 
#d = dd.io.load('C:\\Users\\Dannie\\Desktop\\source\\termname.h5')#term對應編號
#print(np.nonzero(d[0].toarray()))#非0項目
#print(d[doc的編號].toarray()[0][term的位置])


#Query--------------------------------------------------------------------------
'''
'''
f=open('C:\\Users\\Dannie\\Desktop\\source\\query.txt','r', encoding = 'UTF-8')
term=[]
num=-1
for data in f.readlines():
    transform=HanziConv.toSimplified(data)
    seg_list = jieba.cut(transform, cut_all=False)
    term.append(" ".join(seg_list))  # 精确模式
    print("目前正在",num+1)
    num=num+1
    print(term)
vectorizer = TfidfVectorizer(min_df=1)
Q = vectorizer.fit_transform(term)
qidf = vectorizer.idf_
qterm=vectorizer.get_feature_names()
'''
#dd.io.save('C:\\Users\\Dannie\\Desktop\\source\\qsparse.h5', Q)
#dd.io.save('C:\\Users\\Dannie\\Desktop\\source\\qidf.h5', qidf)
t = dd.io.load('C:\\Users\\Dannie\\Desktop\\source\\termname.h5')#quert term對應編號
s = dd.io.load('C:\\Users\\Dannie\\Desktop\\source\\sparse.h5')#term-doc matrix 的sparse matrix 
#dd.io.save('C:\\Users\\Dannie\\Desktop\\source\\qterm.h5', qterm)
qt = dd.io.load('C:\\Users\\Dannie\\Desktop\\source\\qterm.h5')

'''
qtodoc=[]

#print((set(qterm[10])&set(t))=={})
bit=True

#下面為找query term跟doc term 之間的編號轉換

tnum=0
for term in qterm:
    i=0
    for ti in t:
        if(term==ti):
            qtodoc.append(i)
            bit=False
            print("--------------------------------------------")
            break        
        i=i+1
    if(bit):
        qtodoc.append(-1)
    else:
        bit=True
    print(tnum)
    tnum=tnum+1

print(qtodoc)#ex qtodoc[0]=299代表在query第0個term對應到doc第299個term
#qt[i]=t[qtodocmatrix[i]]#qt[i]=t[qtodocmatrix[i]]

'''
#dd.io.save('C:\\Users\\Dannie\\Desktop\\source\\qtodoc.h5', qtodoc)
 


qtodocmatrix = dd.io.load('C:\\Users\\Dannie\\Desktop\\source\\qtodoc.h5')
Q = dd.io.load('C:\\Users\\Dannie\\Desktop\\source\\qsparse.h5')
qidf = dd.io.load('C:\\Users\\Dannie\\Desktop\\source\\qidf.h5')
S = dd.io.load('C:\\Users\\Dannie\\Desktop\\source\\sparse.h5')
idf = dd.io.load('C:\\Users\\Dannie\\Desktop\\source\\idf.h5')
termnum = dd.io.load('C:\\Users\\Dannie\\Desktop\\source\\termname.h5')#term對應編號
#print(qt[0]==termnum[qtodocmatrix[0]])
#print(qt[0]==termnum[qtodocmatrix[0]])
#--------------------------------------------------------------------------------------------
#下面是把Query的idf改成所有文件的idf，這樣Q才是對的query doc-term tf-idf
#print(find(Q[0])[1])
#for x in find(Q[0])[1]:
#    print(termnum[qtodocmatrix[x]])

'''
QN=len(Q.toarray())
#print(Q)
for j in range(QN):

    for i in find(Q[j])[1]:

        if(qtodocmatrix[i]>=0):

            Q[j,i]=(Q[j,i]/qidf[i])*idf[qtodocmatrix[i]]

#print("\n",Q)
#Query------------------------------------------------------------------------------------
'''
#Vector model---------------------------------------------------------------------------
#Doctitle---------------------------



f=open('C:\\Users\\Dannie\\Desktop\\source\\document.txt','r', encoding = 'UTF-8')
documenttitle=[]
for data in f.readlines():
    documenttitle.append(data.split('\t',1)[0])
'''

#Doctitle---------------------------

 

def dot(Dj,docindex,Q,qindex):
    summation=0
    for qw in find(Q[qindex])[1]:
        summation=summation+Q[qindex,qw]*Dj[docindex,qtodocmatrix[qw]]
    return summation
N=132173
qresult=[]
Qresult=[]
QN=30
print()
for qi in range(0,QN):
    for i in range(0,N):
        qresult.append(dot(S,i,Q,qi))
        print(qi,i,qresult[i])
        #if(i>11140):
            #break    
    Qresult.append(qresult)
    qresult=[]

#print(Qresult)
#z=0
#z = bottleneck.partsort(-np.array(Qresult[0]), 5)[:10] 
#print(z)
#y=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#arg = np.argsort(-np.array(Qresult[0]))[:100]
#print(arg)
#z = np.sort(-np.array(Qresult[0]))[:100]
#print(z)
'''

data=""
totaldata=[]
for qr in Qresult:
    z=0
    z = np.argsort(-np.array(qr))[:100]
    #print(z)
    for i in z:   
        print(documenttitle[i])
        data=data+documenttitle[i]+" "
        #print(i)  
    totaldata.append(data)
    #print(data)
    data=""
#print(totaldata)

headers = ['Id','Rel_News']
#print(rows)
id=len(totaldata)
with open('Final.csv','w') as f:
    f_csv = csv.writer(f,lineterminator='\n')
    f_csv.writerow(headers)
    for i in range(0,id):
        f_csv.writerows([(i+1,totaldata[i])])


