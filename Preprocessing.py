# -*- coding: utf-8 -*-
"""
Created on Fri May 24 22:16:52 2019

@author: Gias
"""
#Library
import re #Regular Expression
from nltk.tokenize import word_tokenize #Tokenization
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory #Stopword Removal
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory #Stemming
from xlrd import open_workbook #open file


#Create stemmer and stopword function
stemLib = StemmerFactory()
stopLib = StopWordRemoverFactory()
stemmer = stemLib.create_stemmer()
stopword = stopLib.create_stop_word_remover()

class newsClass(object):
    def __init__(self, news, classValue):
        self.news = news
        self.classValue = classValue

#Open file function
def openFile(data):
    items= []
    for sheet in data.sheets():
        for row in range(sheet.nrows):
            values = []
            for col in range(sheet.ncols):
                values.append((sheet.cell(row,col).value))
            items.append(newsClass(*values))
    return items

#Preprocessing function
def preprocessing(news):
    for i in range (len(news)):
#        Cleanning
        cleanning = re.sub("[^a-zA-Z\s]","", news[i].news)       
#        Casefolding
        caseFold = cleanning.lower()
#        StopwordRemoval
#        stopWord = stopword.remove(caseFold)    
#        Stemming                                   
        stemming = stemmer.stem(caseFold) 
#        stemming = stemmer.stem(stopWord)                                       
#        Tokenisasi
#        tokens = word_tokenize(stopWord)
        tokens = word_tokenize(stemming)                                  
#        tokens = word_tokenize(caseFold)
        classes = news[i].classValue
        
        news[i].news = tokens
        news[i].classValue = classes
    return news

def preprocessingInput(news):
#        Cleanning
    cleanning = re.sub("[^a-zA-Z\s]","", news)       
#        Casefolding
    caseFold = cleanning.lower()
#        StopwordRemoval
#    stopWord = stopword.remove(caseFold)    
#        Stemming                                   
#    stemming = stemmer.stem(caseFold)                                       
#        Tokenisasi
#    tokens = word_tokenize(stopWord)
    tokens = word_tokenize(stemming)                                  
#    tokens = word_tokenize(caseFold)
    return tokens

wb = open_workbook('DataSet.xls')
items = openFile(wb)     
print("Load Complete")
print("Preprosessing")
items = preprocessing(items)