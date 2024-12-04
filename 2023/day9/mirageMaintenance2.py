data = []
with open('day9/input.txt') as file:
    for i, group in enumerate(file.read().strip().split('\n')):
      line = [int(x)  for x in group.split(" ")]
      data.append(line)


sumOflines = 0
for line in data:
    notZero = True
    newLine = line
    difference=[]
    firstItems = [line[0]]
    while notZero:
        for i in range(1, len(newLine)):
            difference.append(newLine[i] - newLine[i-1])
        firstItems.append(difference[0])
        #print(newLine)
        if difference == [0]* (len(newLine)-1):
            notZero == False
            #print("stop")
            break
        else:
            newLine=difference
            difference=[]
    
    reverseItems = firstItems[::-1]
    sumItems = 0
    for i in range(1, len(firstItems)):
        sum = reverseItems[i] -sumItems
        sumItems=sum
    #print(sumItems)  
    sumOflines += sumItems
    #print(sum(firstItems))
print(sumOflines)
    

      
