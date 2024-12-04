with open("day6/input.txt") as file:
  data = {}

  for line in file:
    key, values = line.split(":")
    value = values.strip().replace(" ", "")
    data[key] = int(value)
    
  print(data)
  variants= 0
  for t in range(1,data['Time']):
      distance = (data['Time'] - t)*t
      if distance > data['Distance']:
        variants +=1
    
  print(variants)
