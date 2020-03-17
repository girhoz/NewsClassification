# -*- coding: utf-8 -*-
"""
Created on Wed May 29 08:25:04 2019

@author: Gias
"""
import numpy as np
import math

def getTf(allFeature, newsContent):
    countFeature, tfTable = 0, np.array([[0 for x in range (len(newsContent)+1)] for y in range(len(allFeature))],dtype=object) #kolom x baris
    for feature in allFeature:                                                #access each feature are used from feature selection
        countDoc = 0                                                           #number of word 
        tfTable[countFeature][countDoc]= feature                             #every [number][0] fill with feature
        for doc in newsContent:
            countWord = 0
            for word in doc:                                           #access each word in sentence news
                if feature == word:
                    countWord += 1                                                #count the sum of feature active in that document
            countDoc += 1
            tfTable[countFeature][countDoc] = countWord                            #every [feature-x][doc-x] = count that feature  ==> [word, val doc 1, val2, ..,vallas feature]
        countFeature += 1
    return tfTable

def getIdf(allFeature, newsContent):
    countFeature, idfTable = 0, np.array([[0 for x in range (0,2)] for y in range(len(allFeature))],dtype=object)           
    for feature in allFeature:
        idfTable[countFeature][0] = feature
        countDf = float(0)
        for doc in newsContent:
            flag = 0
            for word in doc:
                if feature == word:                                     #if the feature found in 
                    flag += 1                                           #flag to give the sign that have that feature
                    break                                                       #out from loop, just need one word
            if flag > 0:                                              #1 mean document contain that feature, 0 mean not yet
                countDf += 1                                                      #the number of news that contain that feature
        idfTable[countFeature][1] = math.log10((len(newsContent) / 1+countDf))          #get idf value
        countFeature += 1
    return idfTable

def getTfidf(tfTable, idfTable, allFeature, newsContent):
    countFeature, tfidfTable = 0, np.array([[0 for x in range (len(newsContent))] for y in range(len(allFeature))],dtype=float)
    for x in tfTable:                                                           #access tf data
        for y in idfTable:                                                      #access idf data
            if x[0] == y[0]:                                                    #conditional if tf data equal to idf data
                for col in range(len(newsContent)):                            #this loop use for fill the tf-idf feature in all document
                    tfidfTable[countFeature][col] = float(x[col+1] * y[1])            #column is feature, left is document
                break
        countFeature+=1
    return tfidfTable.T                                                         #transpose, column is document row is feature

#TF-IDF For Input ONLY
    
def getTfInput(allFeature, newsContent):
    countFeature, tfTable = 0, np.array([[0 for x in range (0,2)] for y in range(len(allFeature))],dtype=object) #kolom x baris
    for feature in allFeature:                                                #access each feature are used from feature selection
        countDoc = 0                                                           #number of word 
        tfTable[countFeature][countDoc]= feature                             #every [number][0] fill with feature
        countWord = 0
        for word in newsContent:
            if feature == word:
                countWord += 1                                                #count the sum of feature active in that document
        countDoc += 1
        tfTable[countFeature][countDoc] = countWord                            #every [feature-x][doc-x] = count that feature  ==> [word, val doc 1, val2, ..,vallas feature]
        countFeature += 1
    return tfTable

def getTfidfInput(tfTable, idfTable, allFeature, newsContent):
    countFeature, tfidfTable = 0, np.array([[0 for x in range (0,1)] for y in range(len(allFeature))],dtype=float)
    for x in tfTable:                                                           #access tf data
        for y in idfTable:                                                      #access idf data
            if x[0] == y[0]:                                                    #conditional if tf data equal to idf data
                for col in range(0,1):                            #this loop use for fill the tf-idf feature in all document
                    tfidfTable[countFeature][col] = float(x[col+1] * y[1])            #column is feature, left is document
                break
        countFeature+=1
    return tfidfTable.T