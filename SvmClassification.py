# -*- coding: utf-8 -*-
"""
Created on Wed May 30 09:20:33 2019

@author: Gias
"""
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier

def classification(X_train, y_train, X_test): 
    clf = svm.SVC(kernel='linear')
#    clf= MLPClassifier(solver='adam', alpha=1e-5, hidden_layer_sizes=(75, 10), random_state=1)#Multi layer perceptron 
#    clf = KNeighborsClassifier(n_neighbors=5)   
#    clf= GaussianNB()
    
    clf.fit(X_train, y_train)
    clf_predictions = clf.predict(X_test)
    return clf_predictions