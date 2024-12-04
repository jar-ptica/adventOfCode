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
print(len(lines), len(lines[0]))
# add new columns
for p, each in enumerate(lines):
    newLine = each
    for i,c in enumerate(column):
        newLine = newLine[0:c+i] + "." + newLine[c+i:]
    lines[p] = newLine

# add new rows
for i, each in enumerate(emptyline[::-1]):
   print(i, each)
   lines.insert(each, "."*len(lines[1]))

# find galaxies
galaxies= []
for l, line in enumerate(lines):
   for s, symbol in enumerate(line):
       if symbol=="#":
           galaxies.append((l,s))
#print(galaxies)

print(len(lines), len(lines[0]))
print(len(galaxies))
shortestWay=[]
length = len(galaxies)
print(length)
count=0
for i in range(0, len(galaxies)):
    for k in range(i+1, len(galaxies)):
        count+=1
        down = abs(galaxies[k][0] - galaxies[i][0])
        side = abs(galaxies[k][1] - galaxies[i][1])
        shortestWay.append(down+side)
#print(shortestWay)
print(sum(shortestWay))
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

    
