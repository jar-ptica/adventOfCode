import os

def readInput(input):
    absolute_path = os.path.dirname(__file__)
    full_path = os.path.join(absolute_path, input)

    with open(full_path) as file:
        data = file.read().splitlines()

    return data


def puzzle1(input):
    lines = readInput(input)
    count = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j]=="^":
                print(i, j)
                up = i-1
                while lines[up][j] != "#":
                    count +=1
                    up -=1
                right = j +1
                while lines[up+1][right]!= "#":
                    count +=1
                    right +=1
                print(up+1, right-1)

    print(count)

print(puzzle1("test.txt"))
