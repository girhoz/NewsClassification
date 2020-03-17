# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 08:31:56 2019

@author: Gias
"""

from xlrd import open_workbook #open file
import Preprocessing as pr
import Tfidf as tfidf
import time
import pickle
import SvmClassification as cl

startTime = time.time()
wb = open_workbook('DataSet.xls')
items = pr.openFile(wb)     
print("Load Complete")
print("Preprosessing")
items = pr.preprocessing(items)        #preprocessing (clean, casefold, stopword, stem, token) 
print("finish preprosessing")
newsContent = []
for i in items:
    newsContent.append(i.news)
    
dataTrainText, dataTestText, yTrain, yTest = [],[],[],[]
print("Load Train Index")
title = "D:\TA\Stemming\Index_Data\TrainIndex1.pickle"
pickle_in = open(title,"rb")
train_index = pickle.load(pickle_in)

print("Load Class Value")
pickle_in = open("ClassValue.pickle","rb")
arr = pickle.load(pickle_in)
    
print("Load Test Index")
title = "D:\TA\Stemming\Index_Data\TestIndex1.pickle"
pickle_in = open(title,"rb")
test_index = pickle.load(pickle_in)

for i in range (len(train_index)):
    dataTrainText.append(newsContent[train_index[i]])
    
for i in range (len(test_index)):
    dataTestText.append(newsContent[test_index[i]])

print("Getting Feature")
feature = []
for item in dataTrainText:
    for x in item:
        if x not in feature:
            feature.append(x)
 
print("Count TF-IDF")    
tfTrain = tfidf.getTf(feature,dataTrainText)                     #get TF Value
idfTrain = tfidf.getIdf(feature,dataTrainText)                   #get IDF Value
tfidfTrain = tfidf.getTfidf(tfTrain, idfTrain,feature,dataTrainText)  #get TF-IDF
          
tfTest = tfidf.getTf(feature,dataTestText)                                      
tfidfTest = tfidf.getTfidf(tfTest, idfTrain,feature,dataTestText)

print("Load TFIDF Train")
title = "D:\TA\Stemming\Data_TFIDF\TFIDFTrain1.pickle"
pickle_in = open(title,"rb")
tfidfTrain = pickle.load(pickle_in)
    
print("Load TFIDF Test")
title = "D:\TA\Stemming\Data_TFIDF\TFIDFTest1.pickle"
pickle_in = open(title,"rb")
tfidfTest = pickle.load(pickle_in)

print("Start Classification")
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
acc = acc/tot
print("Accuracy : ",acc)
print('Time: ',time.time()-startTime,'second')