# -*- coding: utf-8 -*-1
"""
Created on Fri May 24 22:16:58 2019

@author: Gias
"""
import time
import operator #shorting
import pickle
import numpy as np
import Preprocessing as pr
import KamusNews as kms
import Tfidf as tfidf
import MutualInformation as mi
import SvmClassification as cl
from xlrd import open_workbook #open file
from sklearn.model_selection import KFold

startTime = time.time()

wb = open_workbook('DataSet.xls')
items = pr.openFile(wb)     
print("Load Complete")
print("Preprosessing")
items = pr.preprocessing(items)        #preprocessing (clean, casefold, stopword, stem, token) 
print("finish preprosessing")
newsContent, arr = [], [[],[],[],[],[],[],[],[],[],[],[],[]]
for i in items:
    newsContent.append(i.news)
    arr[int(i.classValue)-1].append(np.int64(1))
    for x in range(0,12):
        if (x != (int(i.classValue-1))):
            arr[x].append(np.int64(0))
arr2 = []
for i in arr:
    arr2.append(np.array(i, dtype = np.int64))

# =============================================================================
# print("Save Array Class")
# pickle_out = open("ClassValue.pickle","wb")
# pickle.dump(arr2, pickle_out)
# pickle_out.close()
# =============================================================================

dictionary = kms.classWord(items)
print("Get Kamus Class Value")

kf, count = KFold(n_splits=5, random_state=None, shuffle=True),0
for train_index, test_index in kf.split(newsContent):
    dataTrain, dataTrainText, dataTest, dataTestText, yTrain, yTest = [],[],[],[],[],[]
    count +=1
    for i in range (len(train_index)):
        dataTrain.append(items[train_index[i]])
        dataTrainText.append(newsContent[train_index[i]])
        yTrain.append(items[train_index[i]].classValue)
    for i in range (len(test_index)):
        dataTest.append(items[test_index[i]]) 
        dataTestText.append(newsContent[test_index[i]])
        yTest.append(items[test_index[i]].classValue)
        
# =============================================================================
#     print("Save Data Train")
#     title = "DataTrain"+str(count)+".pickle"
#     pickle_out = open(title,"wb")
#     pickle.dump(dataTrainText, pickle_out)
#     pickle_out.close()
#     
#     print("Save Data Test")
#     title = "DataTest"+str(count)+".pickle"
#     pickle_out = open(title,"wb")
#     pickle.dump(dataTestText, pickle_out)
#     pickle_out.close()
#     
#     print("Save train index")
#     title = "TrainIndex"+str(count)+".pickle"
#     pickle_out = open(title,"wb")
#     pickle.dump(train_index, pickle_out)
#     pickle_out.close()
#     
#     print("Save test index")
#     title = "TestIndex"+str(count)+".pickle"
#     pickle_out = open(title,"wb")
#     pickle.dump(test_index, pickle_out)
#     pickle_out.close()
# =============================================================================

    f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,sumWord = kms.getFreqWord(dataTrain)
    
    print("Get Kamus Not Class Value")
    notf1 = kms.getNotClass(f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12)
    notf2 = kms.getNotClass(f2,f1,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12)
    notf3 = kms.getNotClass(f3,f2,f1,f4,f5,f6,f7,f8,f9,f10,f11,f12)
    notf4 = kms.getNotClass(f4,f2,f3,f1,f5,f6,f7,f8,f9,f10,f11,f12)
    notf5 = kms.getNotClass(f5,f2,f3,f4,f1,f6,f7,f8,f9,f10,f11,f12)
    notf6 = kms.getNotClass(f6,f2,f3,f4,f5,f1,f7,f8,f9,f10,f11,f12)
    notf7 = kms.getNotClass(f7,f2,f3,f4,f5,f6,f1,f8,f9,f10,f11,f12)
    notf8 = kms.getNotClass(f8,f2,f3,f4,f5,f6,f7,f1,f9,f10,f11,f12)
    notf9 = kms.getNotClass(f9,f2,f3,f4,f5,f6,f7,f8,f1,f10,f11,f12)
    notf10 = kms.getNotClass(f10,f2,f3,f4,f5,f6,f7,f8,f9,f1,f11,f12)
    notf11 = kms.getNotClass(f11,f2,f3,f4,f5,f6,f7,f8,f9,f10,f1,f12)
    notf12 = kms.getNotClass(f12,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f1)
    
    print("Get Kamus Total Word")
    sumf1, sumNotf1 = kms.getSumWord(f1), kms.getSumWord(notf1)
    sumf2, sumNotf2 = kms.getSumWord(f2), kms.getSumWord(notf2)
    sumf3, sumNotf3 = kms.getSumWord(f3), kms.getSumWord(notf3)
    sumf4, sumNotf4 = kms.getSumWord(f4), kms.getSumWord(notf4)
    sumf5, sumNotf5 = kms.getSumWord(f5), kms.getSumWord(notf5)
    sumf6, sumNotf6 = kms.getSumWord(f6), kms.getSumWord(notf6)
    sumf7, sumNotf7 = kms.getSumWord(f7), kms.getSumWord(notf7)
    sumf8, sumNotf8 = kms.getSumWord(f8), kms.getSumWord(notf8)
    sumf9, sumNotf9 = kms.getSumWord(f9), kms.getSumWord(notf9)
    sumf10, sumNotf10 = kms.getSumWord(f10), kms.getSumWord(notf10)
    sumf11, sumNotf11 = kms.getSumWord(f11), kms.getSumWord(notf11)
    sumf12, sumNotf12 = kms.getSumWord(f12), kms.getSumWord(notf12)
    
    print("Get feature with count")
    wordf1 = sorted(f1.items(), key=operator.itemgetter(0))
    wordNotf1 = sorted(notf1.items(), key=operator.itemgetter(0))
    wordf2 = sorted(f2.items(), key=operator.itemgetter(0))
    wordNotf2 = sorted(notf2.items(), key=operator.itemgetter(0))
    wordf3 = sorted(f3.items(), key=operator.itemgetter(0))
    wordNotf3 = sorted(notf3.items(), key=operator.itemgetter(0))
    wordf4 = sorted(f4.items(), key=operator.itemgetter(0))
    wordNotf4 = sorted(notf4.items(), key=operator.itemgetter(0))
    wordf5 = sorted(f5.items(), key=operator.itemgetter(0))
    wordNotf5 = sorted(notf5.items(), key=operator.itemgetter(0))
    wordf6 = sorted(f6.items(), key=operator.itemgetter(0))
    wordNotf6 = sorted(notf6.items(), key=operator.itemgetter(0))
    wordf7 = sorted(f7.items(), key=operator.itemgetter(0))
    wordNotf7 = sorted(notf7.items(), key=operator.itemgetter(0))
    wordf8 = sorted(f8.items(), key=operator.itemgetter(0))
    wordNotf8 = sorted(notf8.items(), key=operator.itemgetter(0))
    wordf9 = sorted(f9.items(), key=operator.itemgetter(0))
    wordNotf9 = sorted(notf9.items(), key=operator.itemgetter(0))
    wordf10 = sorted(f10.items(), key=operator.itemgetter(0))
    wordNotf10 = sorted(notf10.items(), key=operator.itemgetter(0))
    wordf11 = sorted(f11.items(), key=operator.itemgetter(0))
    wordNotf11 = sorted(notf11.items(), key=operator.itemgetter(0))
    wordf12 = sorted(f12.items(), key=operator.itemgetter(0))
    wordNotf12 = sorted(notf12.items(), key=operator.itemgetter(0))
    
    print("Get confusion matrix of each class")
    budaya = mi.confusionMatrixValue(wordf1, wordNotf1, sumf1,sumNotf1)
    ekonomi = mi.confusionMatrixValue(wordf2, wordNotf2, sumf2,sumNotf2)
    hiburan = mi.confusionMatrixValue(wordf3, wordNotf3, sumf3,sumNotf3)
    hukum = mi.confusionMatrixValue(wordf4, wordNotf4, sumf4,sumNotf4)
    kesehatan = mi.confusionMatrixValue(wordf5, wordNotf5, sumf5,sumNotf5)
    lifestyle = mi.confusionMatrixValue(wordf6, wordNotf6, sumf6,sumNotf6)
    otomotif = mi.confusionMatrixValue(wordf7, wordNotf7, sumf7,sumNotf7)
    pendidikan = mi.confusionMatrixValue(wordf8, wordNotf8, sumf8,sumNotf8)
    politik = mi.confusionMatrixValue(wordf9, wordNotf9, sumf9,sumNotf9)
    sport = mi.confusionMatrixValue(wordf10, wordNotf10, sumf10,sumNotf10)
    tekno = mi.confusionMatrixValue(wordf11, wordNotf11, sumf11,sumNotf11)
    wisata = mi.confusionMatrixValue(wordf12, wordNotf12, sumf12,sumNotf12)
    
    print("Get mi value of each word on each class")
    miBudaya = mi.miTable(budaya,(sumWord))
    miEkonomi = mi.miTable(ekonomi,(sumWord))
    miHiburan = mi.miTable(hiburan,(sumWord))
    miHukum = mi.miTable(hukum,(sumWord))
    miKesehatan = mi.miTable(kesehatan,(sumWord))
    miLifestyle = mi.miTable(lifestyle,(sumWord))
    miOtomotif = mi.miTable(otomotif,(sumWord))
    miPendidikan = mi.miTable(pendidikan,(sumWord))
    miPolitik = mi.miTable(politik,(sumWord))
    miSport = mi.miTable(sport,(sumWord))
    miTekno = mi.miTable(tekno,(sumWord))
    miWisata = mi.miTable(wisata,(sumWord))
    
    print("Merge all feature with mi value")
    allMiValue = miBudaya
    allMiValue = mi.mergeMiValue(miEkonomi, allMiValue)
    allMiValue = mi.mergeMiValue(miHiburan, allMiValue)
    allMiValue = mi.mergeMiValue(miHukum, allMiValue)
    allMiValue = mi.mergeMiValue(miKesehatan, allMiValue)
    allMiValue = mi.mergeMiValue(miLifestyle, allMiValue)
    allMiValue = mi.mergeMiValue(miOtomotif, allMiValue)
    allMiValue = mi.mergeMiValue(miPendidikan, allMiValue)
    allMiValue = mi.mergeMiValue(miPolitik, allMiValue)
    allMiValue = mi.mergeMiValue(miSport, allMiValue)
    allMiValue = mi.mergeMiValue(miTekno, allMiValue)
    allMiValue = mi.mergeMiValue(miWisata, allMiValue)
    
    def getKey(item):
        return item.value
    print("Sorted feature with the highest mi value")
    featureX = sorted(allMiValue, key=getKey, reverse=True)

#     #===================================Save======================================================
# =============================================================================
#     print("Save Feature Word with MI")
#     
#     title = "FeatureMI"+str(count)+".pickle"
#     pickle_out = open(title,"wb")
#     pickle.dump(featureX, pickle_out)
#     pickle_out.close()
#     
#     print("=======================================")
#     print("Feature Saved ",count)
#     print("=======================================")
# =============================================================================
      #==================LOAD FEATURE=======================
# =============================================================================
#     titleMI = "Data_feature_MI/FeatureMI"+str(count)+".xls"
#     wb = open_workbook(titleMI)
#     featureLoad = mi.loadMI(wb)
# =============================================================================


#         #==================== TF IDF
# =============================================================================
# 
# =============================================================================
    feature = []
    for i in range (0,5000):
        feature.append(featureX[i].news)
    tfTrain = tfidf.getTf(feature,dataTrainText)                     #get TF Value
    idfTrain = tfidf.getIdf(feature,dataTrainText)                   #get IDF Value
    tfidfTrain = tfidf.getTfidf(tfTrain, idfTrain,feature,dataTrainText)  #get TF-IDF
         
    tfTest = tfidf.getTf(feature,dataTestText)                                      
    tfidfTest = tfidf.getTfidf(tfTest, idfTrain,feature,dataTestText)
    
# =============================================================================
#     print("Save TF-IDF value")
#     title = "IDFTrain"+str(count)+".pickle"
#     pickle_out = open(title,"wb")
#     pickle.dump(idfTrain, pickle_out)
#     pickle_out.close()
#     
#     title = "TFIDFTrain"+str(count)+".pickle"
#     pickle_out = open(title,"wb")
#     pickle.dump(tfidfTrain, pickle_out)
#     pickle_out.close()
#     
#     title = "TFIDFTest"+str(count)+".pickle"
#     pickle_out = open(title,"wb")
#     pickle.dump(tfidfTest, pickle_out)
#     pickle_out.close()
#     
#     print("=======================================")
#     print("TF-IDF Saved ",count)
#     print("=======================================")
# =============================================================================
     
    
      
#         #========================= Classification

    print("Klasifikasi ke-", count)
    xTrain, xTest = tfidfTrain, tfidfTest
    p, r = [], []
    for c, y in enumerate(arr2):                                         
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
    print(acc)
    print('Time: ',time.time()-startTime,'second')

print('Time: ',time.time()-startTime,'second')
                
            
