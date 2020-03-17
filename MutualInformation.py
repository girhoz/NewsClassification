# -*- coding: utf-8 -*-
"""
Created on Fri May 24 22:20:16 2019

@author: Gias
"""

import math

class truthTable(object):
    def __init__(self,news,tt,tf,ft,ff):
        self.news = news             #Content
        self.tt = tt     #Truth Truth
        self.tf = tf     #Truth False
        self.ft = ft     #False Truth
        self.ff = ff     #False False
        
class miClass(object):
    def __init__(self,news,value):
        self.news = news
        self.value = value

def confusionMatrixValue(wordTrue, wordFalse,sumWordTrue, sumWordFalse):
    tt, tf, ft, ff = 0, 0, 0, 0
    confusionMatrix = []
    for item in wordTrue:
        values = []
        word, tt = item[0], item[1]
        for item2 in wordFalse:
            if word == item2[0]:
                tf = item2[1]
                break
            else:
                tf = 0
        ft = sumWordTrue - tt
        ff = sumWordFalse - tf
        values.append(word)
        values.append(float(tt))
        values.append(float(tf))
        values.append(float(ft))
        values.append(float(ff))
        tTable = truthTable (*values)
        confusionMatrix.append(tTable)
    return confusionMatrix

def miTable(tabelNews, N):
    miTable = []
    N = float(N)
    for item in tabelNews:
        valMi = []
        tt = (item.tt/N) * math.log(((item.tt*N) / ((item.tt+item.tf) * (item.tt+item.ft))),2)
        ft = (item.ft/N) * math.log(((item.ft*N) / ((item.ft+item.ff) * (item.ft+item.tt))),2)
        if item.tf == 0:
            tf = 0
        else:
            tf = (item.tf/N) * math.log(((item.tf*N) / ((item.tf+item.tt) * (item.tf+item.ff))),2)
        ff = (item.ff/N) * math.log(((item.ff*N) / ((item.ff+item.tf) * (item.ff+item.ft))),2)
        miValues = (tt+ft+tf+ff)
        valMi.append(item.news)
        valMi.append(miValues)
        mi = miClass(*valMi)
        miTable.append(mi)
    return miTable

def mergeMiValue(miTable, mergeTable):
    for item1 in miTable:
        count, tag = 0,0
        for item2 in mergeTable:
            if (item1.news == item2.news):
                if (item1.value >= item2.value):
                    mergeTable[count] = item1
                tag += 1
                break
            count += 1
        if(tag == 0):
            mergeTable.append(item1)
    return mergeTable

