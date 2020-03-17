# -*- coding: utf-8 -*-
"""
Created on Wed May 29 08:23:56 2019

@author: Gias
"""

def classWord(items):
    dictionary = {}
    for i in range(len(items)):
        for word in items[i].news:
            if word in dictionary:
                if not items[i].classValue in dictionary[word]:
                    dictionary[word].append(items[i].classValue)
            else:
                dictionary[word] = []
                dictionary[word].append(items[i].classValue)        
    return dictionary

def getFreqWord(items):
    f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12 = {},{},{},{},{},{},{},{},{},{},{},{}
    sumWord = 0
    for i in range(len(items)):
        for word in items[i].news:
            if items[i].classValue == 1:
                if word in f1:
                    f1[word] += 1
                else:
                    f1[word] = 1
            elif items[i].classValue == 2:
                if word in f2:
                    f2[word] += 1
                else:
                    f2[word] = 1
            elif items[i].classValue == 3:
                if word in f3:
                    f3[word] += 1
                else:
                    f3[word] = 1
            elif items[i].classValue == 4:
                if word in f4:
                    f4[word] += 1
                else:
                    f4[word] = 1
            elif items[i].classValue == 5:
                if word in f5:
                    f5[word] += 1
                else:
                    f5[word] = 1
            elif items[i].classValue == 6:
                if word in f6:
                    f6[word] += 1
                else:
                    f6[word] = 1                    
            elif items[i].classValue == 7:
                if word in f7:
                    f7[word] += 1
                else:
                    f7[word] = 1        
            elif items[i].classValue == 8:
                if word in f8:
                    f8[word] += 1
                else:
                    f8[word] = 1
            elif items[i].classValue == 9:
                if word in f9:
                    f9[word] += 1
                else:
                    f9[word] = 1          
            elif items[i].classValue == 10:
                if word in f10:
                    f10[word] += 1
                else:
                    f10[word] = 1      
            elif items[i].classValue == 11:
                if word in f11:
                    f11[word] += 1
                else:
                    f11[word] = 1
            elif items[i].classValue == 12:
                if word in f12:
                    f12[word] += 1
                else:
                    f12[word] = 1
            sumWord += 1
    return f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,sumWord

def getNotClass(f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12):
    notf1 = {}
    jumlah, total = 0,0
    for item in f1:
        if item in f2:
            jumlah = f2[item]
            total = total + jumlah
        if item in f3:
            jumlah = f3[item]
            total = total + jumlah
        if item in f4:
            jumlah = f4[item]
            total = total + jumlah  
        if item in f5:
            jumlah = f5[item]
            total = total + jumlah
        if item in f6:
            jumlah = f6[item]
            total = total + jumlah
        if item in f7:
            jumlah = f7[item]
            total = total + jumlah
        if item in f8:
            jumlah = f8[item]
            total = total + jumlah
        if item in f9:
            jumlah = f9[item]
            total = total + jumlah
        if item in f10:
            jumlah = f10[item]
            total = total + jumlah
        if item in f11:
            jumlah = f11[item]
            total = total + jumlah
        if item in f12:
            jumlah = f12[item]
            total = total + jumlah
        if total != 0:
            notf1[item] = total
        total = 0
    return notf1

def getSumWord(newsDictionary):
    jumlah, total =0,0
    for i in newsDictionary:
        jumlah = newsDictionary[i]
        total = total + jumlah
    return total