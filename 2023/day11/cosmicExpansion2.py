with open("day11/input.txt") as file:
    lines = file.read().splitlines()

# find empty lines and columns
emptyline = []
emptyColumn = {}
for i, line in enumerate(lines):
    valid = True
    for k, chr in enumerate(line):
        if chr=="#":
            valid=False
        else:
            if k in emptyColumn.keys():
               emptyColumn[k] += 1   
            else:
               emptyColumn[k] =1         
    if valid==True:
        emptyline.append(i)

column = [x for x in emptyColumn.keys() if emptyColumn[x]==len(lines[1])]
print(column)
print(emptyline)
#print(len(lines), len(lines[0]))
# add new columns
"""for p, each in enumerate(lines):
    newLine = each
    for i,c in enumerate(column):
        newLine = newLine[0:c+i*1] + "."*1 + newLine[c+i*1:]
    lines[p] = newLine"""

# add new rows
"""for i, each in enumerate(emptyline[::-1]):
   for k in range(1):
       lines.insert(each, "."*len(lines[1]))"""

# find galaxies
galaxies= []
for l, line in enumerate(lines):
   for s, symbol in enumerate(line):
       if symbol=="#":
           galaxies.append((l,s))
#print(galaxies)

print(len(lines), len(lines[0]))
print(len(galaxies))
summary = 0
#appender = []
for i in range(0, len(galaxies)):
    for k in range(i+1, len(galaxies)):
        countLine = 0
        countColumn = 0
        for line in emptyline:
            if line in range(galaxies[i][0], galaxies[k][0]):
                countLine+=999999
        for c in column:
            if c in range(min(galaxies[k][1], galaxies[i][1]), max(galaxies[k][1], galaxies[i][1])):
                countColumn+=999999
        #print(galaxies[i], galaxies[k], galaxies[k][0] , galaxies[i][0])
        #print(countLine, countColumn)
        down = abs(galaxies[k][0] - galaxies[i][0]) #+ countColumn
        side = abs(galaxies[k][1] - galaxies[i][1]) #+ countLine
        #appender.append(countColumn+countLine)
        summary += (down+side+countColumn+countLine)
#print(shortestWay)
print(summary)
#print(appender)
#f = open("numbersValid2.txt", "w")

"""ans = 0
# and for now, let's just iterate over all pairs of galaxies
for i, (x1, y1) in enumerate(galaxies):
    for (x2, y2) in galaxies[i + 1:]:
        # sum the difference between Xs coordinates and Ys coordinates
        #print(abs(x1 - x2) + abs(y1 - y2))
        #f.write(str(abs(x1 - x2) + abs(y1 - y2)))
        #f.write('\n')
        ans += (abs(x1 - x2) + abs(y1 - y2))
print(ans)  
"""

    
