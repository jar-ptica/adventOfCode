with open("day2/input.txt") as file:
  sumGame =[]

  for line in file:
    text = line.split(":")
    data = text[1].split(" ")
    blue =[]
    red=[]
    green=[]
    
    for i in range(0, len(data),2):
      if "red" in data[i]:
        red.append(int(data[i-1]))
      elif "blue" in data[i]:
        blue.append(int(data[i-1]))
      elif "green" in data[i]:
        green.append(int(data[i-1]))
    mult = max(blue) * max(red) *max(green)
    sumGame.append(mult)
  print(sum(sumGame))

