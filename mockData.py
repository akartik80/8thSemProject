from random import random

row = []

row = ["city", "moving_from", "bhk", "min_budget", "max_budget", "cutomer_type", "workers", "no_of_cars",
  "house_type", "travelling_time", "furnishing", "lease_type", "seen_other_options", "show_old_construction",
  "status", "is_urgent", "state"]

print (", ".join(row))

for i in range(1, 100000):
  row = []
  rand = random()
  
  # city  
  if rand < 0.96517:
    row.append(1)
  elif rand < 0.99022:
    row.append(2)
  else:
    row.append(3)

  # moving from
  if rand < 0.55897:
    row.append(1)
  elif rand < 0.78995:
    row.append(2)
  else:
    row.append(3)

  # bhk
  if rand < 0.53399:
    row.append(3) # 2BHK
  elif rand < 0.75348:
    row.append(4) # 3BHK
  elif rand < 0.92974:
    row.append(2) # 1BHK
  elif rand < 0.96899:
    row.append(1) # 1RK
  elif rand < 0.99786:
    row.append(5) # 4BHK
  else:
    row.append(6) # 5BHK
    

  # min budget --------------- ensure < max budget
  
  if rand < 0.34479:
    row.append(15000)
    minBudget = 15000
  elif rand < 0.59242:
    row.append(20000)
    minBudget = 20000
  elif rand < 0.69272:
    row.append(25000)
    minBudget = 25000
  elif rand < 0.75833:
    row.append(30000)
    minBudget = 30000
  elif rand < 0.8008:
    row.append(10000)
    minBudget = 10000
  elif rand < 0.8367:
    row.append(18000)
    minBudget = 18000
  elif rand < 0.8836:
    row.append(35000)
    minBudget = 35000
  elif rand < 0.89995:
    row.append(16000)
    minBudget = 16000
  elif rand < 0.91614:
    row.append(40000)
    minBudget = 40000
  elif rand < 0.93111:
    row.append(22000)
    minBudget = 22000
  elif rand < 0.93798:
    row.append(17000)
    minBudget = 17000
  else:
    row.append(20000)
    minBudget = 20000

  # max budget

  if rand < 0.2348:
    if minBudget > 15000:
      row.append(minBudget + 5000)
    else: 
      row.append(15000)
  elif rand < 0.42056:
    if minBudget > 20000:
      row.append(minBudget + 5000)
    else: 
      row.append(20000)
  elif rand < 0.56141:
    if minBudget > 25000:
      row.append(minBudget + 5000)
    else: 
      row.append(25000)
  elif rand < 0.65842:
    if minBudget > 30000:
      row.append(minBudget + 5000)
    else: 
      row.append(30000)
  elif rand < 0.71204:
    if minBudget > 18000:
      row.append(minBudget + 5000)
    else: 
      row.append(18000)
  elif rand < 0.75329:
    if minBudget > 35000:
      row.append(minBudget + 5000)
    else: 
      row.append(35000)
  elif rand < 0.78598:
    if minBudget > 16000:
      row.append(minBudget + 5000)
    else: 
      row.append(16000)
  elif rand < 0.81714:
    if minBudget > 22000:
      row.append(minBudget + 5000)
    else: 
      row.append(22000)
  elif rand < 0.84342:
    if minBudget > 40000:
      row.append(minBudget + 5000)
    else: 
      row.append(40000)
  elif rand < 0.86695:
    if minBudget > 17000:
      row.append(minBudget + 5000)
    else: 
      row.append(17000)
  elif rand < 0.88559:
    if minBudget > 50000:
      row.append(minBudget + 5000)
    else: 
      row.append(50000)
  elif rand < 0.89903:
    if minBudget > 23000:
      row.append(minBudget + 5000)
    else: 
      row.append(23000)
  elif rand < 0.91171:
    if minBudget > 45000:
      row.append(minBudget + 5000)
    else: 
      row.append(45000)
  elif rand < 0.9221:
    if minBudget > 28000:
      row.append(minBudget + 5000)
    else: 
      row.append(28000)
  elif rand < 0.93142:
    if minBudget > 24000:
      row.append(minBudget + 5000)
    else: 
      row.append(24000)
  else:
    if minBudget > 23000:
      row.append(minBudget + 5000)
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

  # workers

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
