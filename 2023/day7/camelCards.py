cardBid = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
cardHighest = cardBid[::-1]

with open("day7/input.txt") as file:
  cards = {}

  for line in file:
    key, value = line.strip().split(" ")
    cards[key] = int(value)
    
  occurance= {}
  for card in cards.keys():
    newCard = card
    doubles=[]
    remapCard = []
    for s in newCard:
      remapCard.append(cardHighest.index(s))
      count = newCard.count(s)
      #print(count, s)
      if count>1:
         doubles.append(count)
      newCard = newCard.replace(s,"")
    doubles= sorted(doubles, reverse=True)
    if len(doubles) ==0:
      doubles.append(1)
    
    if len(doubles) ==1:
      doubles.append(1)
    
    [doubles.append(x) for x in remapCard]
    occurance[card] = doubles
  
  #print(occurance)
  sortList = dict(sorted(occurance.items(), key=lambda x: x[1]))
  sum = 0
  rank = 1
  print(sortList)
  
  
  for i,card in enumerate(sortList.keys()):
    sum += cards[card]*rank
    rank+=1
    
  print(sum)
