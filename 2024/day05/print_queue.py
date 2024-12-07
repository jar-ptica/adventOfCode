import os

def readInput(input):
    absolute_path = os.path.dirname(__file__)
    full_path = os.path.join(absolute_path, input)

    pairs = []
    data = []
    with open(full_path) as file:
        for line in file:
            if "|" in line:
                a, b = line.strip().split("|")
                pairs.append([a,b])

            elif "," in line:
                nums = line.strip().split(",")
                data.append(nums)

    return pairs, data

def sortOrder(array, rules):
    arr = array.copy()
    n = len(arr)
    for i in range(n):
        correct = 0
        for j in range(i+1, n):
            if [arr[i], arr[j]] not in rules:
                if [arr[j], arr[i]] in rules:
                    arr[i], arr[j] = arr[j], arr[i]
                
            else:
                arr[i], arr[j] = arr[i], arr[j]

    return arr

def puzzle1(input):
    rules, data = readInput(input)
    sum =0
    incorrectSum = 0
    for line in data:
        newline = sortOrder(line, rules)
        index = len(line) // 2
        if line == newline:
            sum += int(newline[index])
        else: 
            incorrectSum += int(newline[index])
    return(sum, incorrectSum)


print(puzzle1("test.txt"))
print(puzzle1("input.txt"))

#sort(['61','13','29'], rules)


