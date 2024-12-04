import os

def readInput(input):
    absolute_path = os.path.dirname(__file__)
    full_path = os.path.join(absolute_path, input)

    listA = []
    listB = []
    with open(full_path) as file:
        for line in file:
            a, b = line.strip().split("   ")
            listA.append(int(a))
            listB.append(int(b))
    return listA, listB

def puzzle1(input):
    listA, listB = readInput(input)
    a = sorted(listA)
    b = sorted(listB)
    sum = 0
    for i in range(len(listA)):
        sum += abs(a[i] - b[i])

    return sum

def puzzle2(input):
    listA, listB = readInput(input)
    sum = 0
    uniqueElements = []
    for each in listA:
        if each not in uniqueElements:
            uniqueElements.append(each)

            occurrenceB = listB.count(each)
            occurrenceA = listA.count(each) 
            if occurrenceB == 0:
                continue

            for i in range(occurrenceA):
                sum += each*occurrenceB
            
    return sum

print(puzzle1("test.txt"), puzzle1("input.txt"))
print(puzzle2("test.txt"), puzzle2("input.txt"))

