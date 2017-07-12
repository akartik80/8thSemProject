from random import random

row = []

for i in range(1, 1000):
  # city
  if random() < 0.96517:
    row.append(1)
  elif random() < 0.99022:
    row.append(2)
  else:
    row.append(3)

  # relocating from
  if random() < 0.55897:
    row.append(1)
  elif random() < 0.78995:
    row.append(2)
  else:
    row.append(3)

  # bhk
  if random() < 0.04169:
    row.append(1) # 1RK
  elif random() < 0.32574:
    row.append(2) # 1BHK
  elif random() < 0.84346:
    row.append(3) # 2BHK
  elif random() < 0.98518:
    row.append(4) # 3BHK
  elif random() < 0.99893:
    row.append(5) # 4BHK
  else:
    row.append(6) # 5BHK

  # customer type
  
