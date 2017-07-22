import pandas as pd
import numpy as np
import re
import csv
from sklearn import ensemble
from sklearn import datasets
from sklearn.utils import shuffle
from sklearn.metrics import mean_squared_error
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


train, labels = read_data("/home/okutech/training100000.csv")
test, test_label = read_data("/home/okutech/testing.csv")
train_mat = np.mat(train)
test_mat = np.mat(test)
params = {'n_estimators': 500, 'max_depth': 4, 'min_samples_split': 2,
          'learning_rate': 0.01, 'loss': 'ls'}
clf = ensemble.GradientBoostingClassifier(learning_rate=0.06, n_estimators=1000,max_depth=4, min_samples_split=1200,min_samples_leaf=60, subsample=0.85, random_state=10000, max_features=13)
clf.fit(train_mat, labels)
predict = clf.predict(test_mat)
predict_proba = clf.predict_proba(test_mat)[:,1]
count = 0
for i in range(0, len(predict)):
  if predict[i] == test_label[i]:
    count = count+1
cv_score = cross_val_score(clf, train_mat, labels, cv=5, scoring='roc_auc')

print "Number of correct labels = ",count
print "The Roc_auc_score is = " , roc_auc_score(test_label, predict_proba)
print "Mean value of Cross_validation score =", np.mean(cv_score)
print "Max value of Cross_validation score =", np.max(cv_score)
print "Standard deviation of Cross_validation score =", np.std(cv_score)