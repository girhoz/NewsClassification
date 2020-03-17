# -*- coding: utf-8 -*-1
"""
Created on Fri May 24 22:16:58 2019

@author: Gias
"""

import Preprocessing as pr
import SvmClassification as cl
import Tfidf as tfidf
import pickle

inputNews = input("Type the news: ")
inputNews = pr.preprocessingInput(inputNews)

print("Load Class Value")
pickle_in = open("ClassValue.pickle","rb")
arr = pickle.load(pickle_in)

print("Load Feature MI")
title = "D:\TA\Stopword\Data_feature_MI\FeatureMI1.pickle"
pickle_in = open(title,"rb")
featureX = pickle.load(pickle_in)

print("Load Data Train")
title = "D:\TA\Stopword\Data_Train\DataTrain1.pickle"
pickle_in = open(title,"rb")
dataTrain = pickle.load(pickle_in)

print("Load Train Index")
title = "D:\TA\Stopword\Index_Data\TrainIndex1.pickle"
pickle_in = open(title,"rb")
train_index = pickle.load(pickle_in)

print("Load Feature")
feature = []
for i in range(0,5000):
    feature.append(featureX[i].news)

print("Count TF-IDF")
title = "D:\TA\Stopword\Data_TFIDF\TFIDFTrain1.pickle"
pickle_in = open(title,"rb")
tfidfTrain = pickle.load(pickle_in)

title = "D:\TA\Stopword\Data_TFIDF\IDFTrain1.pickle"
pickle_in = open(title,"rb")
idfTrain = pickle.load(pickle_in)

tfTest = tfidf.getTfInput(feature,inputNews)                                      
tfidfTest = tfidf.getTfidfInput(tfTest, idfTrain, feature,inputNews)

print("Start Classification")
xTrain, xTest = tfidfTrain, tfidfTest

p = []
for c, y in enumerate(arr):                                         
    yTrain = y[train_index]
    predictValue = cl.classification(xTrain, yTrain, xTest)
    p.append(predictValue)

print ("=========Hasil Klasifikasi=========")
for i in range (len(p)):
    if p[i] == 1:
        if i == 0:
            print("Kelasnya adalah Budaya")
        elif i == 1:
            print("Kelasnya adalah Ekonomi")
        elif i == 2:
            print("Kelasnya adalah Entertainment")  
        elif i == 3:
            print("Kelasnya adalah Hukum dan Kriminal")
        elif i == 4:
            print("Kelasnya adalah Kesehatan")
        elif i == 5:
            print("Kelasnya adalah Lifestyle")
        elif i == 6:
            print("Kelasnya adalah Otomotif")
        elif i == 7:
            print("Kelasnya adalah Pendidikan")  
        elif i == 8:
            print("Kelasnya adalah Politik")
        elif i == 9:
            print("Kelasnya adalah Sport")            
        elif i == 10:
            print("Kelasnya adalah Teknologi")
        else:
            print("Kelasnya adalah Wisata")           