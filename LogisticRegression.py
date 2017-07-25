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
from sklearn.preprocessing import label_binarize

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
train_mat = np.mat(train)
test_mat = np.mat(test)
logreg = LogisticRegression(C=2.0)
logreg.fit(train_mat, labels)
predict = logreg.predict(test)
predict_labels = logreg.predict_proba(test)[:, 1]

count = 0
for i in range(0, len(test_label)):
  if test_label[i] == predict[i]:
    count = count + 1

cv_score = cross_val_score(logreg, train_mat, labels, cv=5, scoring='roc_auc')

labels = label_binarize(labels, classes=[0, 1])
n_classes = labels.shape[1]

print "Number of correct labels = ",count
print "The Roc_auc_score is = " , roc_auc_score(test_label, predict_labels)
print "Mean value of Cross_validation score =", np.mean(cv_score)
print "Max value of Cross_validation score =", np.max(cv_score)
print "Standard deviation of Cross_validation score =", np.std(cv_score)
print "Accuracy as per testing data = " ,accuracy_score(test_label, predict)