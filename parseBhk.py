with open("/home/okutech/repos/8thSemProject/data/testing.csv") as file:
  count = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
  total = 0

  for line in file:
    largest = 0
    bhkString = line.split(",")[2]
    for character in bhkString:
      if character.isdigit() and int(character) > largest:
        largest = int(character)

    if "RK" in bhkString or "rk" in bhkString:
      count[0] += 1
    else:
      count[largest] += 1

    total += 1

  for i in range(0, len(count)):
    count[i] = count[i] / total

  cumulative = [count[0]]

  for i in range(1, len(count)):
    cumulative.append(count[i] + cumulative[i - 1])

  print(cumulative)
