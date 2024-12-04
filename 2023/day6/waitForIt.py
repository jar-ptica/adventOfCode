with open("day6/input.txt") as file:
  multGame = 1
  data = {}

  for line in file:
    key, values = line.split(":")
    value = [int(x) for x in values.strip().split()]
    data[key] = value
    
  print(data)
  for i in range(len(data['Time'])):
    variants = 0
    print(True)
    for t in range(1,data['Time'][i]):
      distance = (data['Time'][i] - t)*t
      #print(t, distance)
      if distance > data['Distance'][i]:
        variants +=1
        #print(data['Time'][i], True)
    multGame*=variants
  print(multGame)
