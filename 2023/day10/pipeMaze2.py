
with open("day10/input.txt") as file:
    pipes = file.read().splitlines()
    
    findS = []
    for line, pipe in enumerate(pipes):
        for pos, symbol in enumerate(pipe):
            if symbol=="S":
                print("start", line, pos)
                findS.append(line)
                findS.append(pos)
                break

    up = [-1, 0] 
    down = [1, 0]
    left = [0, -1] 
    right = [0, 1] 

    directions = {"|" : [up, down],
                  "-" : [left, right],
                  "L" : [up, right],
                  "J" : [up, left],
                  "7" : [left, down],
                  "F" : [right, down]}
    
    startPos = []
    for x in [up, down, left, right]:
        if (findS[0] + x[0]) >= findS[0]:
           startPos.append([findS[0] + x[0], findS[1]+x[1]]) 
    print(findS)
    print(startPos)
    start = findS
    count=[start]
    posToCheck = startPos
    symbol = ""
    loop = 0
    while symbol!= "S":
        for pos in posToCheck:
            #print(pos)
            if loop==0:
                symbol = pipes[pos[0]][pos[1]]
                if symbol in directions.keys():
                    #count+=1
                    #print(symbol, pos, directions[symbol])
                    difference = [start[0] - pos[0], start[1] - pos[1]]
                    #print(difference, start)
                    for each in directions[symbol]:
                        if difference!= each:
                            #print(each, pos)
                            posToCheck = [[pos[0] + each[0], pos[1] + each[1]]]
                            loop+=1
                            start = pos
                            count.append(start)
                            
            else:
                break
        loop = 0
        #print(symbol, posToCheck)
        #count.append(start)
        #print(start, count)
    pipeList = sorted(count)
    #print(count)
    print("")
    #print(pipeList)
    loopParts = []
    for i in range(1, len(count)):
        if pipeList[i][0] == pipeList[i-1][0]:
            difference=pipeList[i][1] - pipeList[i-1][1]
            if difference > 1:
                loopParts.append([pipeList[i][0], pipeList[i-1][1] +1, pipeList[i][1], pipeList[i][1]-pipeList[i-1][1]-1])
    print(loopParts)
    clusters = []
    num = 0
    for i in range(1, len(loopParts)):
        if loopParts[i][0] -1 == loopParts[i-1][0]:
            #print(loopParts[i], loopParts[i][0], loopParts[i-1][0])
            connected = False
            for k in range(loopParts[i][1], loopParts[i][2]):
                #print(loopParts[i], k, loopParts[i][1], loopParts[i][2]+1, loopParts[i-1][1], loopParts[i-1][2]+1)
                if k in range(loopParts[i-1][1], loopParts[i-1][2]):
                    #print("connectred")
                    connected = True
                    break
            print(loopParts[i], connected)
            if connected == True:
               #clusters.remove(loopParts[i-1])
               num+=loopParts[i-1][3]
               print("add to future num", loopParts[i-1][3])
            if (connected==True and i==len(loopParts)-1):
               clusters.append([loopParts[i][0], loopParts[i][1], loopParts[i][2], loopParts[i][3] +num])
               num=0
               print("add last element if everything is connected")
            if (connected==False and num>0):
               clusters.append(loopParts[i])
               clusters.append([loopParts[i-1][0], loopParts[i-1][1], loopParts[i-1][2], loopParts[i-1][3] +num])
               print("add not connected element ", loopParts[i], "+ previous elemenet ", [loopParts[i-1][0], loopParts[i-1][1], loopParts[i-1][2], num], " with num ", num)
               num=0
            elif (connected==False and num==0):
               clusters.append(loopParts[i])
               print("aded not connected")
               if loopParts[i-1] not in clusters:
                   clusters.append(loopParts[i-1])
                   print("forgotten element")
            print(num)
    if loopParts[-1] not in clusters:
       print("add last element")
       clusters.append(loopParts[-1])
            
    print(sorted(clusters))
    trueRange = []
    for each in clusters:
        valid = True
        for i in range(each[1], each[2]+1):
            if [each[0]+1, i] not in pipeList:
                print("not isnisde", each)
                valid = False
                break
        if valid:
            trueRange.append(each[3])
    print(trueRange)
    print(sum(trueRange))
        

                

    
        
    
                
