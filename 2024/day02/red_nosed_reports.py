import os

def readInput(input):
    absolute_path = os.path.dirname(__file__)
    full_path = os.path.join(absolute_path, input)

    data = []
    with open(full_path) as file:
        for line in file:
            digits = line.strip().split(" ")
            data.append([int(x) for x in digits])

    return data

def puzzle1(input):
    reports = readInput(input)
    safe_reports = 0
    for n, line in enumerate(reports):
        increasing = False
        decreasing = False
        validLine = True
        for i in range(1, len(line)):
            if validLine == True:
                difference = line[i] - line[i-1]
                if (3 >= difference > 0):
                    if i == 1:
                        increasing = True
                    else:
                        if increasing != True:
                            validLine = False
                            break
                elif (-3 <= difference < 0):
                    if i == 1:
                        decreasing = True
                    else:
                        if decreasing != True:
                            validLine = False
                            break
                else:
                    validLine = False
                    break
            else:
                validLine = False
                break

        if validLine:
            safe_reports+=1
        else: 
            print(n, line)

    return safe_reports

def puzzle2(input):
    reports = readInput(input)
    safe_reports = 0
    for n, line in enumerate(reports):
        if n>50 :
            break
        valid = True
        index = 0
        count = {"+" : 0,
                 "-" : 0,
                 "0" : 0}
        validLine = []
        occurance = 0
        for i in range(1, len(line)):

                difference = line[i] - line[i-1]

                if (3 >= difference > 0):
                    validLine.append("+")
                    count["+"] +=1         
                elif (-3 <= difference < 0):
                    validLine.append("-")
                    count["-"] +=1 
                else:
                    validLine.append("0")
                    count["0"] +=1 
        print(line)
        print(validLine)
        chance = {k: v for k, v in sorted(count.items(), key=lambda item: item[1])}
        #print(chance)
        occurance = list(chance.values())[0] + list(chance.values())[1]
        #print(occurance)
        if count["0"] > 2 :
            #print("a lot irregular")
            valid = False
        elif occurance == 1:
            print("check")
            symbol = [k for k, v in chance.items() if v == 1][0]
            index = validLine.index(symbol)
            print(symbol, index)
            if (index +2 == len(line)) or (index==0):
                valid = True
            else:
                difference = line[index+2] - line[index]
                if (3 >= difference > 0):
                    symbol = "+"   
                elif (-3 <= difference < 0):
                    symbol = "-"
                else:
                    symbol = "0"
                if symbol == [k for k, v in chance.items() if v == max(chance.values())][0]:
                    #print("match", max(chance.values()))
                    valid = True

                else:
                    valid = False
        elif occurance >1 :
            valid=False
        else:
            valid = True



        """if validLine.count("0") > 1 :
            print("a lot irregular")
            valid = False
        elif occurance > 2:
            valid = False
        elif (2>=occurance > 0) and (index == (len(line)-1)):
            print("last char")
            valid = True
            
        elif (2>=occurance > 0):
            difference = line[index] - line[index-2] 
            symbol = ""
            if (3 >= difference > 0):
                symbol = "+"        
            elif (-3 <= difference < 0):
                symbol = "-"  
            else:
                symbol = "0"
            print(line[index], line[index-2]  , symbol, index)
            if symbol == sorted(validLine)[0]:
                print()
                valid = True
               
            else:
                valid=False
           
        else:
            valid = True   """

        if valid==True:
            print(valid)
            safe_reports+=1
           
    
    return safe_reports


         
    

#print(puzzle1("test.txt"))
#print(puzzle1("input.txt"))
#print(puzzle2("test.txt"))
print(puzzle2("input.txt"))


