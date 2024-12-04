import operator
rocksOrig = []
with open("day14/input.txt") as file:
    lines = file.read().strip().splitlines()
    for line in lines:
        txt = []
        for chr in line:
            txt.append(chr)
        rocksOrig.append(txt)

def north(data):
    rocks=data.copy()
    for r in range(1, len(rocks)):
        for c, column in enumerate(rocks[r]):
            if column == "O":
                findLast = r
                for i in range(r-1,-1,-1):
                    if rocks[i][c] == ".":
                       findLast=i
                    else:
                       findLast=i+1
                       break
                rocks[r][c]="."
                rocks[findLast][c]="O"
    return rocks
def west(data):
    rocks=data.copy()
    for r in range(0, len(rocks)):
        for c, column in enumerate(rocks[r]):
            if column == "O":
                if c>0:
                    findLast = c
                    for i in range(c-1,-1,-1):
                        if rocks[r][i] == ".":
                           findLast=i
                       
                        else:
                           break
                    rocks[r][c]="."
                    rocks[r][findLast]="O"
    return rocks
def south(data):
    rocks=data.copy()
    for r in range(len(rocks)-2, -1, -1):
        for c, column in enumerate(rocks[r]):
            if column == "O":
                findLast = r
                for i in range(r+1,len(rocks)):
                    if rocks[i][c] == ".":
                       findLast=i
                    else:
                       findLast=i-1
                       break
                rocks[r][c]="."
                rocks[findLast][c]="O"
    return rocks

def east(data):
    rocks=data.copy()
    for r in range(0, len(rocks)):
        for c in range(len(rocks[r])-1, -1, -1):
            #print(c)
            column = rocks[r][c]
            if column == "O":
                findLast = c
                for i in range(c+1, len(rocks[r])):
                    #print(i)
                    if rocks[r][i] == ".":
                        findLast=i
                       
                    else:
                        break
                rocks[r][c]="."
                rocks[r][findLast]="O"
    return rocks
for i in range(1000):
    north(rocksOrig)
    west(rocksOrig)
    south(rocksOrig)
    east(rocksOrig)

for line in rocksOrig:
    print(line)



answer = 0
for i, line in enumerate(rocksOrig):
   #print(operator.countOf(line,'O'), " * ",len(rocksOrig) - i )
   answer += operator.countOf(line,'O')* (len(rocksOrig) - i)
print(answer)
