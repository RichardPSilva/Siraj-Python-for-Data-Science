# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 15:28:03 2019

@author: 749445
"""

from sklearn import tree

#[height, weight, shoe size]
x = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37],
     [166, 65, 40], [190, 90, 47], [175, 64, 39], [177, 70, 40], [159, 55, 37],
     [171, 75, 42], [181, 85, 43]]

y = ['male', 'female', 'female', 'female', 'male', 'male', 'male', 'female', 'male', 'female', 'male']


clf = tree.DecisionTreeClassifier()

clf = clf.fit(x, y)

prediction = clf.predict([[190,70,43]])

print(prediction)