# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 21:42:54 2019

@author: Gias
"""

import Tfidf as tfidf
import time
import pickle
import SvmClassification as cl

startTime = time.time()
totalAcc = 0

print("Load Class Value")
pickle_in = open("ClassValue.pickle","rb")
arr = pickle.load(pickle_in)

print("Load Data Train")
title = "D:\TA\Stemming\Data_Train\DataTrain1.pickle"
pickle_in = open(title,"rb")
dataTrain = pickle.load(pickle_in)
    
print("Load Data Test")
title = "D:\TA\Stemming\Data_Test\DataTest1.pickle"
pickle_in = open(title,"rb")
dataTest = pickle.load(pickle_in)
    
print("Load Feature MI")
title = "D:\TA\Stemming\Data_feature_MI\FeatureMI1.pickle"
pickle_in = open(title,"rb")
featureX = pickle.load(pickle_in)

print("Load Train Index")
title = "D:\TA\Stemming\Index_Data\TrainIndex1.pickle"
pickle_in = open(title,"rb")
train_index = pickle.load(pickle_in)

print("Load Train Index")
title = "D:\TA\Stemming\Index_Data\TestIndex1.pickle"
pickle_in = open(title,"rb")
test_index = pickle.load(pickle_in)

length = 0
while(length<=len(featureX)):
    length+=100
    feature = []
    for i in range (0,length+1):
        feature.append(featureX[i].news)
    tfTrain = tfidf.getTf(feature,dataTrain)                     #get TF Value
    idfTrain = tfidf.getIdf(feature,dataTrain)                   #get IDF Value
    tfidfTrain = tfidf.getTfidf(tfTrain, idfTrain,feature,dataTrain)  #get TF-IDF
         
    tfTest = tfidf.getTf(feature,dataTest)                                      
    tfidfTest = tfidf.getTfidf(tfTest, idfTrain,feature,dataTest)
    
    print("Jumlah Feature = ",length+1)
    xTrain, xTest = tfidfTrain, tfidfTest
    p, r = [], []
    for c, y in enumerate(arr):                                         
        yTrain, yTest = y[train_index], y[test_index]
        predictValue = cl.classification(xTrain, yTrain, xTest)
        p.append(predictValue)
        r.append(yTest)
    tot, acc = 0, 0
    for x in range(len(p)):
        for y in range(len(p[x])):
            if (p[x][y] == r[x][y]):
                acc+=1
            tot+=1
    acc = (acc/tot) * 100
    print("Akurasi = ",acc,"%")