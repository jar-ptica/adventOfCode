with open("day4/input.txt") as file:
    lines = file.read().splitlines()
    value_list = [1]*len(lines)
    instances = {index: element for index, element in enumerate(value_list)}

    for i, line in enumerate(lines):
        text = line.split(":")[1].split("|")
        winNum = [x for x in text[0].split(" ") if x != ""]
        cardNum = [x for x in text[1].split(" ") if x != ""]
        
        matchN = 0
        for n in cardNum:
            if n in winNum:
                matchN += 1

        for c in range(0,instances[i]):
            for k in range(i+1, i+ matchN +1):
                instances[k] = instances[k] + 1
                
    print(sum(instances.values()))


