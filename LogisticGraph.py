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

used_cols = ['city', 'moving_from','bhk', 'min_budget','max_budget',
            'customer_type', 'workers','no_of_cars', 'house_type', 'travelling_time',
            'furnishing', 'lease_type','seen_other_options','show_old_construction',
            'status', 'is_urgent','state'];

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
      labels.append(np.int64(int(row[16])-1))
      for i in range(0, len(used_cols)-1):
        if row[i] == '':
          print index
        rowx.append(int(row[i]))
      data.append(np.array(rowx))
  return (data, labels)


train, labels = read_data("/home/okutech/training.csv")
test, test_label = read_data("/home/okutech/testing.csv")
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
print n_classes
test_label = label_binarize(test_label, classes=[0, 1])
test_label = np.mat(test_label)
label_score = logreg.fit(train_mat, labels).predict(test)
fpr = dict()
tpr = dict()
roc_auc = dict()
label_score = label_binarize(label_score, classes=[0, 1])
print label_score
print test_label
for k in range(0, n_classes):
    fpr[k], tpr[k], _ = roc_curve(test_label[:,k], label_score[:, k])
    roc_auc[k] = auc(fpr[k], tpr[k])

# Compute micro-average ROC curve and ROC area
fpr["micro"], tpr["micro"], _ = roc_curve(test_label, label_score)
roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])
#print labels
plt.figure()
lw = 1
plt.plot(fpr[0], tpr[0], color='darkorange', lw=lw, label='ROC curve (area = %0.2f)' % roc_auc[0])
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic example')
plt.legend(loc="lower right")
plt.show()
print "Number of correct labels = ",count
print "The Roc_auc_score is = " , roc_auc_score(test_label, predict_labels)
print "Mean value of Cross_validation score =", np.mean(cv_score)
print "Max value of Cross_validation score =", np.max(cv_score)
print "Standard deviation of Cross_validation score =", np.std(cv_score)