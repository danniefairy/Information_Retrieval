import csv
train=[]
#jupyter 不要用encoding
import jieba
import jieba.posseg
import matplotlib.pyplot as plt
import numpy as np
#建立好feature
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
'''

i=0
ref_doc=[]
for row in open('split_text.txt','r',encoding="UTF-8"):
    #print(row.split(" "))
    ref_doc.append(row.split(" "))
    print(i)
    i=i+1
    
f = open("ref_doc.csv","w",encoding="UTF-8")  
w = csv.writer(f)  
w.writerows(ref_doc)  
f.close()
'''
i=0
loadsentences=[]
f = open('ref_doc.csv', 'r',encoding="UTF-8")  
for row in csv.reader(f):  
    if i%2==0:
        loadsentences.append(row)
    i=i+1
f.close()
#print(len(loadsentences))

#讀取train
with open('train.csv', mode='r',encoding="UTF-8") as f:
    reader = csv.reader(f)
    for row in reader:
        train.append(row)
#print(len(train))
#print((train[1][1] in loadsentences[1311])and (train[1][2] in loadsentences[1311]))
'''
#找到7個種類的各種features
for t in range(len(train)-1):
    for s in range(len(loadsentences)):
        if (train[t+1][1] in loadsentences[s])and (train[t+1][2] in loadsentences[s]):
            #print(train[t+1][1],train[t+1][2],loadsentences[s])
            #print(train[t+1][3])
            for f in features:
                #print(f[0])
                if f[0]==train[t+1][3]:
                    for sterm in loadsentences[s]:
                        f.append(sterm)
  
    print(t+1)
    


for fin in range(7):
    temp=[]
    temp=features[fin][1:]
    temp=set(temp)
    del features[fin][1:]
    features[fin].append(temp)

f = open("features.csv","w",encoding="UTF-8")  
w = csv.writer(f)  
w.writerows(features)  
f.close()
'''

loadfeatures=[]
f = open('features.csv', 'r',encoding="UTF-8")  
for row in csv.reader(f):  
    if len(row)!=0:
        loadfeatures.append(row)
f.close()
'''
#0~6 features種類 1features內容
#print("消失" in(loadfeatures[0][1]))
spouselen=[]
parentlen=[]
childlen=[]
siblinglen=[]
birthPlacelen=[]
deathPlacelen=[]
workPlacelen=[]
#print(loadfeatures[4][0])
#print(train[1][3])
#print(train[1])
#print(train[2])
#print(train[3])
#print(train[497])
i=0

newtrain=[]
for t in range(len(train)-1):
    #print(train[i])
    #seg1 = jieba.cut(train[t+1][1], cut_all=False)
    #seg2=  jieba.cut(train[t+1][2], cut_all=False)
    #for s1 in seg1:
    #    train[t+1][1]=s1
    #    break
    #for s2 in seg2:
    #    train[t+1][2]=s2
    #    break
    temps=[]
    for s in range(len(loadsentences)):
        if (train[t+1][1] in loadsentences[s])and (train[t+1][2] in loadsentences[s]):
            temps.extend(loadsentences[s])
    temps=list(set(temps))
    temps.insert(0,train[t+1][3])
    newtrain.append(temps)
    i=i+1
    print(i)



print(newtrain[0])

f = open("newtrain.csv","w",encoding="UTF-8")  
w = csv.writer(f)  
w.writerows(newtrain)  
f.close()
'''

            
loadnewtrain=[]
f = open('newtrain.csv', 'r',encoding="UTF-8")  
for row in csv.reader(f):  
    if len(row)!=0:
        loadnewtrain.append(row)
f.close()
#print(train[4970])
#print((loadnewtrain[4969]))
#print(loadfeatures[5][1].replace("}","").replace("'","").replace(" ","").replace("{","").split(",")[0])


#所有種類的真正各種features
finalfeatures=[]
for i in range(7):
    finalfeatures.append(loadfeatures[i][1].replace("}","").replace("'","").replace(" ","").replace("{","").split(",")[1:])
'''
    #print(len(finalfeatures[0]))
#loadnewtrain[0].append([0,0,1])
#print(loadnewtrain[0][len(loadnewtrain[0])-1])
count=0
for lnt in loadnewtrain:
    #print(lnt)
    if lnt[0]=="spouse":
        #ftemp=[0]*len(finalfeatures[0])
        ftemp=[]
        #print(ftemp)
        for ln in lnt:
            for i in range(len(finalfeatures[0])):
                if ln==finalfeatures[0][i]:
                    #ftemp[i]=1
                    ftemp.append(i)
        lnt.append(ftemp)
        
    elif lnt[0]=="parent":
        #ftemp=[0]*len(finalfeatures[1])
        ftemp=[]
        #print(ftemp)
        for ln in lnt:
            for i in range(len(finalfeatures[1])):
                if ln==finalfeatures[1][i]:
                    #ftemp[i]=1
                    ftemp.append(i)
        lnt.append(ftemp)
        
    elif lnt[0]=="child":
        #ftemp=[0]*len(finalfeatures[2])
        ftemp=[]
        #print(ftemp)
        for ln in lnt:
            for i in range(len(finalfeatures[2])):
                if ln==finalfeatures[2][i]:
                    #ftemp[i]=1
                    ftemp.append(i)
        lnt.append(ftemp)
        
    elif lnt[0]=="sibling":
        #ftemp=[0]*len(finalfeatures[3])
        ftemp=[]
        #print(ftemp)
        for ln in lnt:
            for i in range(len(finalfeatures[3])):
                if ln==finalfeatures[3][i]:
                    #ftemp[i]=1
                    ftemp.append(i)
        lnt.append(ftemp)
        
    elif lnt[0]=="birthPlace":
        #ftemp=[0]*len(finalfeatures[4])
        ftemp=[]
        #print(ftemp)
        for ln in lnt:
            for i in range(len(finalfeatures[4])):
                if ln==finalfeatures[4][i]:
                    #ftemp[i]=1
                    ftemp.append(i)
        #print(ln)
        lnt.append(ftemp)
        
    elif lnt[0]=="deathPlace":
        #ftemp=[0]*len(finalfeatures[5])
        ftemp=[]
        #print(ftemp)
        for ln in lnt:
            for i in range(len(finalfeatures[5])):
                if ln==finalfeatures[5][i]:
                    #ftemp[i]=1
                    ftemp.append(i)
        lnt.append(ftemp)
        
    elif lnt[0]=="workPlace":
        #ftemp=[0]*len(finalfeatures[6])
        ftemp=[]
        #print(ftemp)
        for ln in lnt:
            for i in range(len(finalfeatures[6])):
                if ln==finalfeatures[6][i]:
                    #ftemp[i]=1
                    ftemp.append(i)
        lnt.append(ftemp)
    count=count+1
    print(count)
    #if count==51:
        #break

#print(loadnewtrain[0])
f = open("bitnewtrain.csv","w",encoding="UTF-8")  
w = csv.writer(f)  
w.writerows(loadnewtrain)  
f.close()
'''
bitnewtrain=[]
f = open('bitnewtrain.csv', 'r',encoding="UTF-8")  
for row in csv.reader(f):  
    if len(row)!=0:
        bitnewtrain.append(row)
f.close()
#print(loadnewtrain[49])
#print((bitnewtrain[0][0]))
#print((bitnewtrain[2][len(bitnewtrain[2])-1]).replace("]","").replace("[","").replace("'","").replace(" ","").split(","))
feature_bit=[]
for i in range(len(bitnewtrain)):
    #print(i,bitnewtrain[i][len(bitnewtrain[i])-1])#bit
    #print(bitnewtrain[i][0])#features
    temp=[]
    temp.append(bitnewtrain[i][0])#features
    #bit=((bitnewtrain[i][len(bitnewtrain[i])-1]).replace("[","").replace("'","").replace(" ","").split(","))
    #print(bit)
    temp.append((bitnewtrain[i][len(bitnewtrain[i])-1]).replace("[","").replace("]","").replace("'","").replace(" ","").split(","))
    
    #print(i,l.replace("]","").replace("[","").replace("'","").replace(" ","").split(",")[0])
    #if i>49:
       #break
    #print(i,[i for i,v in enumerate(bitnewtrain[i][len(bitnewtrain[i])-1]) if v==1])

    feature_bit.append(temp)
#print(finalfeatures[4][5462])
#print(train[232])
#train id ,0 train features 1 bit position
#print(len(feature_bit[231][1]))
#print("feature_bit down!")
#for i in range(len(feature_bit)):
    #print(i,feature_bit[i])
#print((finalfeatures))
#-------------------------------------------------------------------------------
#分類feature_bit
spouse=[]
parent=[]
child=[]
sibling=[]
birthPlace=[]
deathPlace=[]
workPlace=[]
for i in range(len(feature_bit)):
    if not feature_bit[i][1]==['']:
        if feature_bit[i][0]=="spouse":
            spouse.append(feature_bit[i][1])
        elif feature_bit[i][0]=="parent":
            parent.append(feature_bit[i][1])
        elif feature_bit[i][0]=="child":
            child.append(feature_bit[i][1])
        elif feature_bit[i][0]=="sibling":
            sibling.append(feature_bit[i][1])
        elif feature_bit[i][0]=="birthPlace":
            birthPlace.append(feature_bit[i][1])
        elif feature_bit[i][0]=="deathPlace":
            deathPlace.append(feature_bit[i][1])
        elif feature_bit[i][0]=="workPlace":
            workPlace.append(feature_bit[i][1])
#print(len(spouse)+len(parent)+len(child)+len(sibling)+len(birthPlace)+len(deathPlace)+len(workPlace))
#for f in finalfeatures:
    #print(len(f))

#-------------------------------------------------------------------------------
'''
plot=[]
x=np.arange(0,len(finalfeatures[2]))
y=np.zeros(len(finalfeatures[2]))
for si in child[20]:
    for yi in range(len(y)):
        if yi==(int)(si):
            y[yi]=1
            break
    #print(si)
#print(y[1096])
plt.scatter(x,y)
'''

#圖形化權重
#spouse 每一個feature的權重
x=np.arange(0,len(finalfeatures[0]))
sx=np.zeros(len(finalfeatures[0]))
#print(len(sx))
for si in spouse:
    for sit in si:
        sx[int(sit)]=sx[int(sit)]+1/len(si)
#print(sx)
#print(np.where(sx==max(sx)))
#print(finalfeatures[0][10106])#10106 max in spouse
sx=sx/max(sx)
#plt.title("spouse")
#plt.scatter(x,sx)
#plt.show()

#parent 每一個feature的權重
x=np.arange(0,len(finalfeatures[1]))
px=np.zeros(len(finalfeatures[1]))
#print(len(sx))
for si in parent:
    for sit in si:
        px[int(sit)]=px[int(sit)]+1/len(si)
#print(px)
px=px/max(px)
maxpivot=(np.where(px==max(px))[0])
#print(maxpivot,finalfeatures[1][maxpivot],px[maxpivot])
#plt.title("parent")
#plt.scatter(x,px)
#plt.show()

#child 每一個feature的權重
x=np.arange(0,len(finalfeatures[2]))
cx=np.zeros(len(finalfeatures[2]))
#print(len(sx))
for si in child:
    for sit in si:
        cx[int(sit)]=cx[int(sit)]+1/len(si)
#print(cx)
#print(finalfeatures[2][(np.where(cx==max(cx))[0])])
cx=cx/max(cx)
#plt.title("child")
#plt.scatter(x,cx)
#plt.show()

#sibling 每一個feature的權重
x=np.arange(0,len(finalfeatures[3]))
sbx=np.zeros(len(finalfeatures[3]))
#print(len(sx))
for si in sibling:
    for sit in si:
        sbx[int(sit)]=sbx[int(sit)]+1/len(si)
#print(sbx)
#print(np.mean(sbx))
sbx[(np.where(sbx==max(sbx))[0])]=0#去掉"生"
sbx=sbx/max(sbx)

maxpivot=(np.where(sbx==max(sbx))[0])
bro=np.where(sbx==max(sbx))

sbx[(np.where(sbx==max(sbx))[0])]=0#去掉"子"
maxpivot=(np.where(sbx==max(sbx))[0])

sbx[(np.where(sbx==max(sbx))[0])]=0
maxpivot=(np.where(sbx==max(sbx))[0])

sbx[bro]=1
maxpivot=(np.where(sbx==max(sbx))[0])

#print(maxpivot,finalfeatures[3][maxpivot],sbx[maxpivot])
#plt.title("sibling")
#plt.scatter(x,sbx)
#plt.show()

#birthplace 每一個feature的權重
x=np.arange(0,len(finalfeatures[4]))
bpx=np.zeros(len(finalfeatures[4]))
#print(len(sx))
for si in birthPlace:
    for sit in si:
        bpx[int(sit)]=bpx[int(sit)]+1/len(si)
        break
#print(np.mean(bpx))
bpx[(np.where(bpx==max(bpx))[0])]=0#足球 誤差太大
bpx=bpx/max(bpx)
maxpivot=(np.where(bpx==max(bpx))[0])
print(maxpivot,finalfeatures[4][maxpivot],bpx[maxpivot])
#plt.title("birthplace")
#plt.scatter(x,bpx)
#plt.show()

#deathPlace每一個feature的權重
x=np.arange(0,len(finalfeatures[5]))
dpx=np.zeros(len(finalfeatures[5]))
#print(len(sx))
for si in deathPlace:
    for sit in si:
        dpx[int(sit)]=dpx[int(sit)]+1/len(si)
#print(dpx)
#print(np.mean(sbx))
dpx=dpx/max(dpx)
maxpivot=(np.where(dpx==max(dpx))[0])
#print(maxpivot,finalfeatures[5][maxpivot],dpx[maxpivot])
#plt.title("deathplace")
#plt.scatter(x,dpx)
#plt.show()

#workPlace每一個feature的權重
x=np.arange(0,len(finalfeatures[6]))
wpx=np.zeros(len(finalfeatures[6]))
#print(len(sx))
for si in workPlace:
    for sit in si:
        wpx[int(sit)]=wpx[int(sit)]+1/len(si)
#print(wpx/max(wpx))
wpx=wpx/max(wpx)
#print(np.mean(sbx))
maxpivot=(np.where(wpx==max(wpx))[0])
#print(maxpivot,finalfeatures[6][maxpivot],wpx[maxpivot])
#plt.title("workplace")
#plt.scatter(x,wpx)
#plt.show()

print("#--------------------------------------------------")
#-------------------------------------------------------------------------------


def inputarray(row):
    tin=row
    ts=[]
    #print(len(loadsentences[0]))
    t1=[]
    t2=[]
    t1.append(tin[0])
    t2.append(tin[0])
    seg1 = jieba.posseg.cut(tin[1])
    for i1 in seg1:
        t1.extend(i1)
    
    seg2 = jieba.posseg.cut(tin[2])
    for i2 in seg2:
        t2.extend(i2)
    
    #print("@",t1)
    #print("@",t2)
    
    tname=[]
    for i in range(len(t1)):
        if i%2==1 :
            #print(t1[i])
            tname.append(t1[i])
    
    
    for i in range(len(t2)):
        if i%2==1:
            #print(t2[i])
            tname.append(t2[i])
            
    tlocal=[]
    tlocal.append("N")
    if "ns" in t2:
        tlocal.remove("N")
        tlocal.append("L");
    else:
        tlocal.remove("N")
        tlocal.append("E");
    #例外
    if ("柏林" in t2)and("N" in tlocal) :
        tlocal.remove("N")
        tlocal.append("L");
    if  "南宫" in t2 and "公主" in t2:
        tlocal.remove("L")
        tlocal.append("N");
    #print(tname)
    #print(tlocal)
    ts.append(tin[0])
    ts.append(tlocal)
    ts.append(tname)
    #print(ts)
    
    ttemp=[]
    for sentence in loadsentences:
        for tterm in ts[2]:
            if tterm in sentence:
                ttemp.append(sentence)
    t=[]
    for tt in ttemp:
        t=t+tt
    t=list(set(t))
    
    print("#-----------")
    #加強原問句
    #print(len(t))
    
    for i in range(len(t)):
        t.extend(ts[2])
        if i >int(len(t))*0.01:
            break
    #print(t)            
    print("#-----------")
    #print(t)
    
    
    #--------t要收到所有相關的term---------------
    
    #birthPlace
    #print(finalfeatures[4])
    bpt=np.zeros(len(finalfeatures[4]))
    for j in range(len(t)):
        for i in range(len(finalfeatures[4])):
            if t[j]==finalfeatures[4][i]:
                bpt[i]=bpt[i]+1
                break
    print(bpt, np.count_nonzero(bpt),"birthplace")
    
    #spouse
    st=np.zeros(len(finalfeatures[0]))
    for j in range(len(t)):
        for i in range(len(finalfeatures[0])):
            if t[j]==finalfeatures[0][i]:
                st[i]=st[i]+1
                break
    print(st, np.count_nonzero(st),"spouse") 
    
    #parent
    pt=np.zeros(len(finalfeatures[1]))
    for j in range(len(t)):
        for i in range(len(finalfeatures[1])):
            if t[j]==finalfeatures[1][i]:
                pt[i]=pt[i]+1
                break
    print(pt, np.count_nonzero(pt),"parent") 
         
    #deathplace
    dpt=np.zeros(len(finalfeatures[5]))
    for j in range(len(t)):
        for i in range(len(finalfeatures[5])):
            if t[j]==finalfeatures[5][i]:
                dpt[i]=dpt[i]+1
                break
    print(dpt, np.count_nonzero(dpt),"deathplace") 
    
    #workplace
    wpt=np.zeros(len(finalfeatures[6]))
    for j in range(len(t)):
        for i in range(len(finalfeatures[6])):
            if t[j]==finalfeatures[6][i]:
                wpt[i]=wpt[i]+1
                break
    print(wpt, np.count_nonzero(wpt),"workplace") 
    
    #sibling
    sbt=np.zeros(len(finalfeatures[3]))
    for j in range(len(t)):
        for i in range(len(finalfeatures[3])):
            if t[j]==finalfeatures[3][i]:
                sbt[i]=sbt[i]+1
                break
    print(sbt, np.count_nonzero(sbt),"sibling") 
    
    #child
    ct=np.zeros(len(finalfeatures[2]))
    for j in range(len(t)):
        for i in range(len(finalfeatures[2])):
            if t[j]==finalfeatures[2][i]:
                ct[i]=ct[i]+1
                break
    print(ct, np.count_nonzero(ct),"child") 
    
    score=np.dot(bpt,bpx)
    score2=np.dot(st,sx)
    score3=np.dot(pt,px)
    score4=np.dot(wpt,wpx)
    score5=np.dot(dpt,dpx)
    score6=np.dot(sbt,sbx)
    score7=np.dot(ct,cx)
    
    human_location2=[]
    human_location2.append(score2/len(sx)**0.5)#spouse
    human_location2.append(score3/len(px)**0.5)#parent
    human_location2.append(score7/len(cx)**0.5)#child
    human_location2.append(score6/len(sbx)**0.5)#sibling
    human_location2.append(score/len(bpx)**0.5) #birthPlace
    human_location2.append(score5/len(dpx)**0.5)#deathPlace
    human_location2.append(score4/len(wpx)**0.5)#workPlace
      
    human_location=[]
    human_location.append(score2)#spouse
    human_location.append(score3)#parent
    human_location.append(score7)#child
    human_location.append(score6)#sibling
    human_location.append(score) #birthPlace
    human_location.append(score5)#deathPlace
    human_location.append(score4)#workPlace
    
    print(score2/len(sx)**0.5,score2,"spouse")
    print(score3/len(px)**0.5,score3,"parent")
    print(score7/len(cx)**0.5,score7,"child")
    print(score6/len(sbx)**0.5,score6,"sibling")
    print(score/len(bpx)**0.5,score,"birth")
    print(score5/len(dpx)**0.5,score5,"death")
    print(score4/len(wpx)**0.5,score4,"work")
    
    
    
    #x=np.arange(0,len(finalfeatures[4]))
    #plt.scatter(x,plot)
    
    maxpivot=(np.where(human_location==max(human_location))[0])
    if len(maxpivot)>1:
        if tlocal=="N":
            maxpivot=[1]
        elif tlocal=="L":
            maxpivot=[4]
        else:
            maxpivot=[0]
    #print(maxpivot)
    option=["spouse","parent","child","sibling","birthPlace","deathPlace","workPlace"]
    returntwo=[]
    returntwo.append(option[(maxpivot)[0]])
    
    maxpivot=(np.where(human_location2==max(human_location2))[0])
    if len(maxpivot)>1:
        if tlocal=="N":
            maxpivot=[1]
        elif tlocal=="L":
            maxpivot=[4]
        else:
            maxpivot=[0]
    
    returntwo.append(option[(maxpivot)[0]])
    print("#--------------------------------------------------")
    return returntwo
    
    
'''
allarray=[]
allarray2=[]
with open('test.csv', mode='r', encoding='utf-8') as f:
    reader = csv.reader(f)
    i=7573
    for row in reader:
        if i==8074:
            break
        #if i>7580:#7574~8073
        if i>7573:#['8072', '琳达·巴克', '哈佛大学']
            print(i," new#######")
            temp=[]
            temp2=[]
            temp.append(i)
            temp2.append(i)
            #print(inputarray(row))
            getarray=inputarray(row)
            temp.append(getarray[0])
            temp2.append(getarray[1])
            allarray.append(temp)
            allarray2.append(temp2)
        i=i+1
'''
print(birthPlace)
#print("score:",allarray)
#print("score2:",allarray2)
'''
inputsub=[]
f = open("test2_submission.csv","w+",newline='',encoding="UTF-8")#newline='' for no extra line 
w = csv.writer(f)
a=[]
a.append("Id")
a.append("Property")
inputsub.append(a)
for i in range(len(allarray)):
    inputsub.append(allarray[i])
w.writerows(inputsub)
f.close()

inputsub=[]
f2 = open("test3_submission.csv","w+",newline='',encoding="UTF-8")#newline='' for no extra line 
w2 = csv.writer(f2)
a=[]
a.append("Id")
a.append("Property")
inputsub.append(a)
for i in range(len(allarray2)):
    inputsub.append(allarray2[i])
w2.writerows(inputsub)
f2.close()
'''
#-------------------------------------------------------------------------------
#print(finalfeatures[1][int(parent[2][4])])
'''
#mapping 先暫停 不用NN
parent2spouse=[]
k=0
for p in parent:
    #print(len(p))
    temp=[]
    for i in range(len(p)):
        for fi in range(len(finalfeatures[0])):
            if finalfeatures[0][fi]==finalfeatures[1][(int)(p[i])]:
                #print(finalfeatures[0][fi])
                temp.append(fi);
                break
                #print(fi,p[i],finalfeatures[0][fi])
    #print(len(temp))
    parent2spouse.append(temp)
    k=k+1
    print(k)
    
k=0
child2spouse=[]
for p in child:
    #print(len(p))
    temp=[]
    for i in range(len(p)):
        for fi in range(len(finalfeatures[0])):
            if finalfeatures[0][fi]==finalfeatures[2][(int)(p[i])]:
                #print(finalfeatures[0][fi])
                temp.append(fi);
                break
                #print(fi,p[i],finalfeatures[0][fi])
    #print(len(temp))
    child2spouse.append(temp)
    k=k+1
    print(k)

print("ok")

print(len(child2spouse),len(spouse))
#print(finalfeatures[1][2860])
'''
#-------------------------------------------------------------------------------
'''
#print(len(train))
for i in range(len(train)):
    for s in range(len(loadsentences)):
        temp=[]*len(loadfeatures[0][1]
        if train[i][3]=="spouse":
            if (train[i][1] in loadsentences[s])and (train[i][2] in loadsentences[s]):
                for stemp in loadsentences[s]:
                    
                
        elif train[i][3]=="parent":
            parentlen=parentlen+1
        elif train[i][3]=="child":
            childlen=childlen+1
        elif train[i][3]=="sibling":
            siblinglen=siblinglen+1
        elif train[i][3]=="birthPlace":
            birthPlacelen=birthPlacelen+1
        elif train[i][3]=="deathPlace":
            deathPlacelen=deathPlacelen+1
        elif train[i][3]=="workPlace":
            workPlacelen=workPlacelen+1
        #else:
            #print(train[i][3])
'''
#len(loadfeatures[0][1])
#spouse=[]*spouselen
#print(len(spouse))