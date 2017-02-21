import csv


import jieba
import jieba.posseg
import numpy as np
'''
#找出ref_text內 人物名稱 跟地名
sentences=[]
count=0
for row in open('ref_text.txt','r',encoding='UTF-8'):
    
    seg = jieba.posseg.cut(row)
    name=[]
    l=[]
    #https://gist.github.com/luw2007/6016931
    for i in seg:
        if i.flag[:2]=='ns' or i.flag[:2]=='nr' :#地名
            name.append(i.word)
        l.append(i)

    name=list(set(name))#刪除重複人名/地名

    sentences.append(name)
    
    count=count+1
    print(count)
    #if count==100:
        #break

#存list
f = open("sentences.csv","w",encoding="UTF-8")  
w = csv.writer(f)  
w.writerows(sentences)  
f.close() 
'''
#讀list
loadsentences=[]
i=0
f = open('sentences.csv', 'r',encoding="UTF-8")  
for row in csv.reader(f):  
    if i%2==0:#奇數個都是空的,忽略
        #loadsentences 每一個都有1個index(name(human place))
        loadsentences.append(row)
    i=i+1
f.close()
#print(loadsentences[0])



train=[]
with open('train.csv', mode='r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        train.append(row)
        #train index分別是 [編號 人名 人名/地名 關係]

#print(train[1])

features=[]
index=["spouse"]
features.append(index)#spouse
index=["parent"]
features.append(index)#parent
index=["child"]
features.append(index)#child
index=["sibling"]
features.append(index)#sibling
index=["birthPlace"]
features.append(index)#birthPlace
index=["deathPlace"]
features.append(index)#deathPlace
index=["workPlace"]
features.append(index)#workPlace
#print(features)
#loadsentences 每一個都有1個index 編號(name(human place))
#train 每一個都有4個index 編號 (id 人名 人名/地名 關係)
for i in range(len(loadsentences)):
    for j in range(len(train)):
        #print(i)
        if (train[j][1] in loadsentences[i]) and (train[j][2] in loadsentences[i]):
            init=0
            for row in open('ref_text.txt','r',encoding='UTF-8'):
                if init==i:
                    print(train[j][3],row)
                    #從找到的關係中抽取出適當的term
                    seg = jieba.posseg.cut(row)
                    
                init=init+1
            
    

