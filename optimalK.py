import pandas as pd
import numpy as np
import re
import csv
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.metrics import roc_auc_score
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
regr = linear_model.LinearRegression()
used_cols = ['city','bhk','max_budget',
            'house_type','furnishing','state'];

def read_data (f, header = True, test = False):
  data = []
  labels = []

  csv_reader = csv.reader(open(f, "r"), delimiter=",")
  index = 0
  for row in csv_reader:
    index = index + 1
    if header and index == 1:
      continue
    
    if not test:
      rowx = []
      labels.append(np.int64(int(row[5])-1))
      for i in range(0, len(used_cols)-1):
        if row[i] == '':
          print index
        rowx.append(int(row[i]))
      data.append(np.array(rowx))
  return (data, labels)


train, labels = read_data("data/training.csv")
test, test_label = read_data("data/testing.csv")
x_index = []
y_index =  []

for j in range(1, 40):
  knn = KNeighborsClassifier(n_neighbors = j, algorithm="kd_tree")
  train_mat = np.mat(train)
  test_mat = np.mat(test)
  knn.fit(train_mat, labels)
  predict_labels = knn.predict_proba(test)[:, 1]
  predict = knn.predict(test_mat)
  count = 0.0
  total_count = 0.0
  for i in range(0, len(predict)):
    total_count = total_count + 1
    if predict[i] == test_label[i]:
      count = count+1
  cv_score = cross_val_score(knn, train_mat, labels, cv=5, scoring='roc_auc')
  #print "Number of correct labels = ",count
  #print "The Roc_auc_score is = " , roc_auc_score(test_label, predict_labels)
  x_index.append(j)
  y_index.append(1- roc_auc_score(test_label, predict))
  
for xx in range(0, len(x_index)):
  if np.min(y_index) == y_index[xx]:
    print x_index[xx], y_index[xx]
plt.title('OPtimal Value of k')
plt.plot(x_index, y_index, 'b')
plt.legend(loc = 'lower right')
plt.plot([0, 40], [0, 1],'r--')
plt.xlim([0, 40])
plt.ylim([0, 1])
plt.ylabel('error')
plt.xlabel('k')
plt.show()
# fit = np.polyfit(x_index,y_index,1)
# fit_fn = np.poly1d(fit) 
# # fit_fn is now a function which takes in x and returns an estimate for y

# plt.plot(x_index,y_index, 'yo', x_index, fit_fn(x_index), '--k')
# plt.xlim(0, 101)
# plt.ylim(0, 1)
# plt.show()