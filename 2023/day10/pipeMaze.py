
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

    up = [-1, 0] #[start[0] -1, start[1]] if start[0]!=0 else [start[0], start[1]]
    down = [1, 0]#[start[0] +1, start[1]] if start[0]!=len(pipes) else [start[0], start[1]]
    left = [0, -1] #[start[0], start[1]-1 ] if start[1]!=0 else [start[0], start[1]]
    right = [0, 1] #[start[0], start[1] +1] if start[1]!=len(pipes[0]) else [start[0], start[1]]

    directions = {"|" : [up, down],
                  "-" : [left, right],
                  "L" : [up, right],
                  "J" : [up, left],
                  "7" : [left, down],
                  "F" : [right, down]}
    
    startPos = []
    for x in [up, down, left, right]:
        startPos.append([findS[0] + x[0], findS[1]+x[1]]) 

    count=1
    start = findS
    posToCheck = startPos
    symbol = ""
    loop = 0
    while symbol!= "S":
        for pos in posToCheck:
            print(pos)
            if loop==0:
                symbol = pipes[pos[0]][pos[1]]
                if symbol in directions.keys():
                    count+=1
                    #print(symbol, pos, directions[symbol])
                    difference = [start[0] - pos[0], start[1] - pos[1]]
                    #print(difference, start)
                    for each in directions[symbol]:
                        if difference!= each:
                            #print(each, pos)
                            posToCheck = [[pos[0] + each[0], pos[1] + each[1]]]
                            loop+=1
                            start = pos
                            
            else:
                break
        loop = 0
        print(symbol, posToCheck)
        #print(start, count)
    print(count/2)
    
    
    """for line in range(upBound, lowBound):
        for pos in range(leftBound, rightBound):
            print(line, pos)
            if pipes[line][pos] in directions.keys():
                print(True, line, pos , pipes[line][pos])"""
                
