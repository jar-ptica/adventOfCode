with open("day11/input.txt") as file:
    lines = file.read().splitlines()
lines = [list(l) for l in lines]
print(lines)
# First of all, find the empty lines
empty_lines = []
len_line = len(lines[0])
for idx, line in enumerate(lines):
    if set(line) == {'.'}:
        empty_lines.append(idx)
print(empty_lines)
# The let's insert one more line after each empty line
# To avoid any mistake with the lines array length
# I do it in a "reverted" way, insert last lines first
for i in empty_lines[::-1]:
    lines.insert(i, (['.'] * len_line))

# The same proccess to the columns
# Just a little bit more code to find the empty coluns
empty_columns = []
for idx in range(len_line):
    flag = True
    for j in range(len(lines)):
        if lines[j][idx] == '#':
            flag = False
            break
    if flag:
        empty_columns.append(idx)
print(empty_columns)
# Once again, add the new empty column to every line
for column in empty_columns[::-1]:
    for line in lines:
        line.insert(column, '.')

# Our map is ready, let's find the coordinates of all the galaxies
f = open("numbersValid.txt", "w")
galaxies = []
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == '#':
            galaxies.append((i, j))
            k = (i, j)
            f.write(str(k))
            f.write('\n')
print(len(lines), len(lines[0]))           
print(len(galaxies))
#print(galaxies)
ans = 0
# and for now, let's just iterate over all pairs of galaxies
for i, (x1, y1) in enumerate(galaxies):
    for (x2, y2) in galaxies[i + 1:]:
        # sum the difference between Xs coordinates and Ys coordinates
        #print(abs(x1 - x2) + abs(y1 - y2))
        #f.write(str(abs(x1 - x2) + abs(y1 - y2)))
        #f.write('\n')
        ans += (abs(x1 - x2) + abs(y1 - y2))
f.close
print(ans)

