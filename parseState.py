import csv

file = csv.reader(open("/home/okutech/Desktop/kartik.csv", "r"), delimiter=",")

for line in file:
  state = line[22]

  if state == 'state':
    print 'state'
    continue

  if state == '1400' or state == '1230' or state == '1200' or state == '1220' or state == '1210' or state == '1240' or state == '1205' or state == '1222' or state == '1280':
    print 1
  else:
    print 2
