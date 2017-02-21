
import jieba
from hanziconv import HanziConv
import sys
import os
from collections import Counter
import json
from sklearn.feature_extraction.text import TfidfVectorizer
'''
#範例--------------------------------------
seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print( " ".join(seg_list).split(" "))  # 精确模式
#範例--------------------------------------

#範例--------------------------------------
print(HanziConv.toSimplified('繁簡轉換器'))
print(HanziConv.toTraditional('繁简转换器'))
#範例--------------------------------------
'''

f=open('C:\\Users\\Dannie\\Desktop\\source\\shortdoc.txt','r', encoding = 'UTF-8')

term=[]
docnum=-1
termU=[]
doc=[]
idfterm=[]
docunique=[]
for data in f.readlines():
    transform=HanziConv.toSimplified(data)
    seg_list1 = jieba.cut(transform, cut_all=False)
    seg_list2 = jieba.cut(transform, cut_all=False)
    idfterm.append(" ".join(seg_list1))
    term=" ".join(seg_list2).split(" ")  # 精确模式
    tforigin=Counter(term)#找到term頻率
    #Double normalization 0.5---------------------
    indexmax=[]
    docpartial=[]
    for index in tforigin:
        indexmax.append(tforigin[index])
        
    maxnum=max(indexmax)
    data={}
    for index in tforigin:        
        tforigin[index]=(0.5+0.5*tforigin[index]/maxnum)
        data[index]=tforigin[index]

    #Double normalization 0.5---------------------
    termU=list(set(termU)|set(term))#找所有doc中 term的聯集
    docunique.extend(list(set(term)))#找到所有的term
    doc.append(data)#每一個doc內每一個term的tf
    docnum=docnum+1



#tf寫入json檔案---------------------
with open('tf.json', 'w') as outfile:
    json.dump(doc, outfile)
#tf寫入json檔案---------------------


#讀取tf---------------------------
with open('tf.json', 'r') as f:
    data = json.load(f)
print(data[0]['出'])
#讀取tf---------------------------

#idf------------------------------

