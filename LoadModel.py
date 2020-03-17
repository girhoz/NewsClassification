# -*- coding: utf-8 -*-1
"""
Created on Fri May 24 22:16:58 2019

@author: Gias
"""
import time
import pickle
import SvmClassification as cl


startTime = time.time()
totalAcc = 0

print("Load Class Value")
pickle_in = open("ClassValue.pickle","rb")
arr = pickle.load(pickle_in)

for i in range (1,6):
# =============================================================================
#     print("Load Data Train")
#     title = "D:\TA\Stopword\Data_Train\DataTrain"+str(i)+".pickle"
#     pickle_in = open(title,"rb")
#     dataTrain = pickle.load(pickle_in)
# =============================================================================
# =============================================================================
#     
#     print("Load Data Test")
#     title = "D:\TA\Stopword\Data_Test\DataTest"+str(i)+".pickle"
#     pickle_in = open(title,"rb")
#     dataTest = pickle.load(pickle_in)
# =============================================================================
    
    print("Load Feature MI")
    title = "D:\TA\Stemming\Data_feature_MI\FeatureMI"+str(i)+".pickle"
    pickle_in = open(title,"rb")
    feature = pickle.load(pickle_in)
    
    print("Load TFIDF Train")
    title = "D:\TA\Stemming\Data_TFIDF\TFIDFTrain"+str(i)+".pickle"
    pickle_in = open(title,"rb")
    tfidfTrain = pickle.load(pickle_in)
    
    print("Load TFIDF Test")
    title = "D:\TA\Stemming\Data_TFIDF\TFIDFTest"+str(i)+".pickle"
    pickle_in = open(title,"rb")
    tfidfTest = pickle.load(pickle_in)
    
    print("Load Train Index")
    title = "D:\TA\Stemming\Index_Data\TrainIndex"+str(i)+".pickle"
    pickle_in = open(title,"rb")
    train_index = pickle.load(pickle_in)
    
    print("Load Test Index")
    title = "D:\TA\Stemming\Index_Data\TestIndex"+str(i)+".pickle"
    pickle_in = open(title,"rb")
    test_index = pickle.load(pickle_in)
    
    print("Klasifikasi ke-", i)
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
    totalAcc+=acc
    print("Akurasi = ",acc,"%")

avg = totalAcc/5
print("Rata-Rata Akurasi Model = ",avg,"%")
print('Time: ',time.time()-startTime,'second')
    