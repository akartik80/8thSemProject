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
count = 0
rf = RandomForestClassifier(n_estimators=150, max_features=13, min_samples_leaf=3, random_state=5000)
rf.fit(train_mat, labels)
rf_predict_labels = rf.predict_proba(test_mat)[:, 1]
predict = rf.predict(test)
count = 0
for i in range(0, len(predict)):
  if predict[i] == test_label[i]:
    count = count+1
cv_score = cross_val_score(rf, train_mat, labels, cv=5, scoring='roc_auc')
print "Number of correct labels = ",count
print "The Roc_auc_score is = " , roc_auc_score(test_label, rf_predict_labels)
print "Mean value of Cross_validation score =", np.mean(cv_score)
print "Max value of Cross_validation score =", np.max(cv_score)
print "Standard deviation of Cross_validation score =", np.std(cv_score)