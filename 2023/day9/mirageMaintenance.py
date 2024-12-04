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
    lastItems = [line[-1]]
    while notZero:
        for i in range(1, len(newLine)):
            difference.append(newLine[i] - newLine[i-1])
        lastItems.append(difference[-1])
        if difference == [0]* (len(newLine)-1):
            notZero == False
            print("stop")
            break
        else:
            newLine=difference
            difference=[]
        
      
        #print(newLine)
    sumOflines += sum(lastItems)
    print(sum(lastItems))
print(sumOflines)
    

      
