import csv

file = csv.reader(open("/home/okutech/Desktop/kartik.csv", "r"), delimiter=",")

for line in file:
  bhkString = line[2]
  largest = 0

  if bhkString == 'bhk':
    print 'bhk'
    continue
  
  for character in bhkString:
    if character.isdigit() and int(character) > largest:
      largest = int(character)

  if ("RK" in bhkString or "rk" in bhkString) and ("bhk" not in bhkString or "BHK" not in bhkString):
    print 1
  else:
    print largest + 1
