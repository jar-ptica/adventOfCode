with open("day4/input.txt") as file:
   sumGame =[]
   for line in file:
    text = line.strip().split(":")[1].split("|")
    winNum = [x for x in text[0].split(" ") if x!=""]
    cardNum = [x for x in text[1].split(" ") if x!=""]

    points = 0
    for n in cardNum:
      if n in winNum:
        if points== 0:
          points+=1
        else: 
          points*=2
    
    sumGame.append(points) 
print(sum(sumGame))
