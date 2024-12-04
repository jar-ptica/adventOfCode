with open("day2/input.txt") as file:
  gameList =[]

  for line in file:
    text = line.split(":")
  
    indexGame = int(text[0].replace("Game ", ""))
    data = text[1].split(" ")
    gameList.append(indexGame)
    for i, item in enumerate(data):
      if (item.isdigit() and indexGame in gameList):
        if int(item)>14:
          gameList.remove(indexGame)
          continue 
        elif (int(item) >13 and "green" in data[i+1]):
          gameList.remove(indexGame)
          continue
        elif (int(item) > 12 and "red" in data[i+1]):
          gameList.remove(indexGame)
          continue 
      
  print(sum(gameList))

          
          
   
        
        

    
        
    
    
    