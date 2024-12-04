import operator
rocks = []
with open("day14/input2.txt") as file:
    lines = file.read().strip().splitlines()
    for line in lines:
        txt = []
        for chr in line:
            txt.append(chr)
        rocks.append(txt)
 
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

answer = 0
for i, line in enumerate(rocks):
   answer += operator.countOf(line,'O')* (len(rocks) - i)
print(answer)
