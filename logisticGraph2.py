import pandas as pd
import numpy as np
import re
import csv
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import label_binarize
from sklearn.metrics import roc_curve, auc

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
fpr, tpr, threshold = roc_curve(test_label, predict_labels)
roc_auc = auc(fpr, tpr)
count = 0
for i in range(0, len(test_label)):
  if test_label[i] == predict[i]:
    count = count + 1

cv_score = cross_val_score(logreg, train_mat, labels, cv=5, scoring='roc_auc')

labels = label_binarize(labels, classes=[0, 1])
n_classes = labels.shape[1]
print labels
print "Number of correct labels = ",count
print "The Roc_auc_score is = " , roc_auc_score(test_label, predict_labels)
print "Mean value of Cross_validation score =", np.mean(cv_score)
print "Max value of Cross_validation score =", np.max(cv_score)
print "Standard deviation of Cross_validation score =", np.std(cv_score)
plt.title('Receiver Operating Characteristic')
plt.plot(fpr, tpr, 'b', label = 'AUC = %0.2f' % roc_auc)
plt.legend(loc = 'lower right')
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()