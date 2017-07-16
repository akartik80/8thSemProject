from random import random

for i in range(1, 10):
  row = []
  rand = random()
  
  # city  
  if rand < 0.96517:
    row.append(1)
  elif rand < 0.99022:
    row.append(2)
  else:
    row.append(3)

  # relocating from
  if rand < 0.55897:
    row.append(1)
  elif rand < 0.78995:
    row.append(2)
  else:
    row.append(3)

  # bhk
  if rand < 0.04169:
    row.append(1) # 1RK
  elif rand < 0.32574:
    row.append(2) # 1BHK
  elif rand < 0.84346:
    row.append(3) # 2BHK
  elif rand < 0.98518:
    row.append(4) # 3BHK
  elif rand < 0.99893:
    row.append(5) # 4BHK
  else:
    row.append(6) # 5BHK

  # customer type
  if rand < 0.30247:
    row.append(1)
  elif rand < 0.44393:
    row.append(2)
  elif rand < 0.47952:
    row.append(3)

  # min budget --------------- ensure < max budget
  
  if rand < 0.34479:
    row.append(15000)
  elif rand < 0.59242:
    row.append(20000)
  elif rand < 0.69272:
    row.append(25000)
  elif rand < 0.75833:
    row.append(30000)
  elif rand < 0.8008:
    row.append(10000)
  elif rand < 0.8367:
    row.append(18000)
  elif rand < 0.8836:
    row.append(35000)
  elif rand < 0.89995:
    row.append(16000)
  elif rand < 0.91614:
    row.append(40000)
  elif rand < 0.93111:
    row.append(22000)
  elif rand < 0.93798:
    row.append(17000)
  else:
    row.append(20000)

  # max budget

  if rand < 0.2348:
    row.append(15000)
  elif rand < 0.42056:
    row.append(20000)
  elif rand < 0.56141:
    row.append(25000)
  elif rand < 0.65842:
    row.append(30000)
  elif rand < 0.71204:
    row.append(18000)
  elif rand < 0.75329:
    row.append(35000)
  elif rand < 0.78598:
    row.append(16000)
  elif rand < 0.81714:
    row.append(22000)
  elif rand < 0.84342:
    row.append(40000)
  elif rand < 0.86695:
    row.append(17000)
  elif rand < 0.88559:
    row.append(50000)
  elif rand < 0.89903:
    row.append(23000)
  elif rand < 0.91171:
    row.append(45000)
  elif rand < 0.9221:
    row.append(28000)
  elif rand < 0.93142:
    row.append(24000)
  else:
    row.append(23000)

  # customer type

  if rand < 0.30263:
    row.append(1)
  elif rand < 0.54598:
    row.append(5)
  elif rand < 0.71356:
    row.append(6)
  elif rand < 0.85517:
    row.append(2)
  elif rand < 0.9175:
    row.append(7)
  elif rand < 0.9644:
    row.append(4)
  else:
    row.append(3)

  # no of members

  if rand < 0.37504:
    row.append(2)
  elif rand < 0.64879:
    row.append(3)
  elif rand < 0.81026:
    row.append(4)
  elif rand < 0.9395:
    row.append(1)
  elif rand < 0.98029:
    row.append(5)
  elif rand < 0.99559:
    row.append(6)
  elif rand < 0.99742:
    row.append(7)
  elif rand < 0.99864:
    row.append(8)
  elif rand < 0.9994:
    row.append(10)
  else:
    row.append(9)

  # no of cars

  if rand < 0.56493:
    row.append(1)
  elif rand < 0.89979:
    row.append(0)
  elif rand < 0.99328:
    row.append(2)
  elif rand < 0.99832:
    row.append(3)
  else:
    row.append(4)

  # house type

  if rand < 0.48457:
    row.append(3)
  elif rand < 0.7982:
    row.append(1)
  elif rand < 0.90239:
    row.append(4)
  elif rand < 0.98274:
    row.append(2)
  else:
    row.append(5)

  # travelling time

  if rand < 0.36603:
    row.append(15)
  elif rand < 0.60022:
    row.append(30)
  elif rand < 0.76857:
    row.append(20)
  elif rand < 0.82586:
    row.append(10)
  elif rand < 0.8642:
    row.append(25)
  elif rand < 0.8891:
    row.append(0)
  elif rand < 0.91033:
    row.append(45)
  elif rand < 0.92973:
    row.append(40)
  elif rand < 0.93951:
    row.append(60)
  elif rand < 0.94501:
    row.append(5)
  elif rand < 0.95051:
    row.append(35)
  else:
    row.append(20)

  # furnishing

  if rand < 0.58692:
    row.append(1)
  else:
    row.append(2)

  # lease type

  if rand < 0.97006:
    row.append(1)
  else:
    row.append(2)

  # seen other options

  if rand < 0.73938:
    row.append(2)
  else:
    row.append(1)

  # show old construction

  if rand < 0.7212:
    row.append(1)
  else:
    row.append(2)

  # status

  if rand < 0.44332:
    row.append(2)
  elif rand < 0.72716:
    row.append(3)
  elif rand < 0.97556:
    row.append(0)
  else:
    row.append(4)
  
  # is urgent

  if rand < 0.83379:
    row.append(2)
  else:
    row.append(1)

  #result

  if rand < 0.03161:
    row.append(1)
  else:
    row.append(2)

  print(str(row).strip('[]'))
