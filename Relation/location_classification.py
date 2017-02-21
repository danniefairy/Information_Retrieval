import csv
import numpy as np
from random import shuffle
import random
import matplotlib.pyplot as plt

'''
array=[]
with open('train.csv', mode='r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        temp=[]
        temp.append(row[2])
        temp.append(row[3])
        array.append(temp)
        
l=[]
lt=[]
n=[]
nt=[]
#我是把詞拆成字做成bag of word
for a in array:
    if a[1][-5:]=="Place":
        l.append(a[0])
        lt=lt+(list(a[0]))
        #print((a))
    else:
        n.append(a[0])
        nt=nt+(list(a[0]))
location=[]
location=location+list(set(l)) 

name=[]
name=name+list(set(n))





blt=list(set(lt))
bnt=list(set(nt))
allset=list(set(blt+bnt))
#print(len(blt),len(bnt),len(allset))

location_data=[]
for lc in location:
    newlocation=np.zeros(len(allset))
    for lcc in lc:
        for i in range(len(allset)):
            if allset[i]==lcc:
                newlocation[i]=1
    location_data.append(newlocation)

name_data=[]
for ln in name:
    newname=np.zeros(len(allset))
    for lnn in ln:
        for i in range(len(allset)):
            if allset[i]==lnn:
                newname[i]=1
    name_data.append(newname)


location_target=np.ones(len(location_data))
name_target=np.zeros(len(name_data))

shuffle(location_data)
shuffle(name_data)

#location_data 1234 name_data 2792
D=[]
data=[]
target=[]
D.append(data)
D.append(target)
l=0
n=0
for i in range(len(location_data)+len(name_data)):
    rand=random.randint(1,10)
    if i==0:
        D[0].append(location_data[0])
        D[1].append(location_target[0])
        l=l+1

    elif rand>5 :
        if l<1234:
            D[0].append(location_data[l])
            D[1].append(location_target[l])
            l=l+1

        else:
            D[0].append(name_data[n])
            D[1].append(name_target[n])
            n=n+1

    elif rand<=5:
        if n <2792:
            D[0].append(name_data[n])
            D[1].append(name_target[n])
            n=n+1

        else:
            D[0].append(location_data[l])
            D[1].append(location_target[l])
            l=l+1

            
#x=np.arange(0,len(D[0]))
#plt.scatter(x,D[1])


import theano.tensor as T
import theano

def compute_accuracy(y_target,y_predict):
    correct_prediction=np.equal(y_predict,y_target)
    accuracy=float(np.sum(correct_prediction))/float(len(correct_prediction))
    return accuracy
    
#定義input
x=T.dmatrix('x')
y=T.dvector("y")

rng=np.random
#初始化weight、bias
w=theano.shared(rng.randn(len(D[0][0])),name='w')
b=theano.shared(0.01,name='b')
#classification 前置作業
#機率
p_1=T.nnet.sigmoid(T.dot(x,w)+b)
prediction=p_1>0.5

#或是用 crossentropy=T.nnet.binary_crossentropy(p_1, y)
crossentropy=-y*T.log(p_1)-(1-y)*T.log(1-p_1)
#0.01*(w**2).sum() 防止overfitting
cost=crossentropy.mean()+0.01*(w**2).sum()
gW,gb=T.grad(cost,[w,b])

#train
learning_rate=0.05
train=theano.function(
    inputs=[x,y],
    outputs=[prediction,crossentropy.mean()],
    updates=((w,w-learning_rate*gW),
            (b,b-learning_rate*gb))
)
    
    #預測
predict=theano.function(inputs=[x],outputs=prediction)


#training
for i in range(5000):
    #input_value,target_class
    pred,err=train(D[0],D[1])
    if i%50==0:
        #print('costs:',err)
        print('accuracy:',compute_accuracy(D[1],predict(D[0])))

  
'''    

I=[]
myword=[["大","韩","民","国"],["剑","桥","大","学"],["理","学","院"],["修","道","院","国","学","加"],["大","国"]]
for wd in myword:
    myoutput=np.zeros(len(allset))
    for w in wd:
        for i in range(len(allset)):
            if allset[i]==w:
                myoutput[i]=1
    I.append(myoutput)

    

print(myword,"predict: ",predict(I))

print('accuracy:',compute_accuracy(D[1],predict(D[0])))