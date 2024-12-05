import os

def readInput(input):
    absolute_path = os.path.dirname(__file__)
    full_path = os.path.join(absolute_path, input)

    with open(full_path) as file:
        data = file.read().split("mul(")

    return data

def readInput2(input):
    absolute_path = os.path.dirname(__file__)
    full_path = os.path.join(absolute_path, input)
    data = []
    with open(full_path) as file:
        disable = file.read().split("don't()")
        data.append(disable[0])
        for i in range(1, len(disable)):
            if "do()" in disable[i]:
                dis, enable = disable[i].split("do()", maxsplit=1)
                data.append(enable)
                
    multiplication = []
    for each in data:
        mult = each.split("mul(")      
        [multiplication.append(x) for x in mult]

    return multiplication

def puzzle1(input, doIt=False):
    data = readInput2(input) if doIt==True else readInput(input)
    sum = 0
    for each in data:
        closed = each.split(")")
        if len(closed) >1:
            digits = closed[0].split(",", maxsplit=1)
            if len(digits) ==2:
                if digits[0].isdigit() and digits[1].isdigit():
                    mult =  int(digits[0])* int(digits[1])
                    sum+=mult
                    #print(digits[0], "mult" , digits[1], "is ", mult)
    return sum
                    

#print(puzzle1("test.txt"))
#print(puzzle1("test.txt", doIt=True))
#print(puzzle1("input.txt"))
print(puzzle1("input.txt", doIt=True))
