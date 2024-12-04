import datetime
start_time = datetime.datetime.now()
import re
with open("day3/input.txt") as file:
    sumValid = []
    lines = file.read().splitlines()
    for k, line in enumerate(lines):
        newLine = line
        text = line.split(".")
        for each in text:
            if each=="":
                continue
            else: 
                if each.isdigit():
                    index = newLine.find(each)
                    newLine = newLine.replace(each, "."*len(each),1)
                    isValid = False

                    if k < (len(lines)-1):
                            for i in range(index -1 if index> 0 else index,
                                            index + len(each)+1 if (index+len(each)) <len(lines) else index + len(each)):
                                if (lines[k+1][i] =="." or lines[k+1][i].isdigit()):
                                    continue
                                else:
                                    isValid = True
                    if (isValid==False and k>0):
                            for i in range(index -1 if index> 0 else index, 
                                           index + len(each)+1 if (index+len(each)) <len(lines) else index + len(each)):
                                if (lines[k-1][i] =="." or lines[k-1][i].isdigit()):
                                    continue
                                else: 
                                    isValid = True
                                    
                                
                    if isValid==True:
                        sumValid.append(int(each))
                    
                else:
                    newLine = newLine.replace(each, "."*len(each),1)
                    if len(each)> 4:
                        splitter = 0
                        for chr in each:
                            if chr.isdigit() == False:
                                splitter = chr
                        numbers = each.split(splitter)
                        for n in numbers:
                                sumValid.append(int(n))
                    else:
                        intValid = re.sub('\D', '',each)
                        if intValid != "":
                            sumValid.append(int(intValid))
    print(sum(sumValid))
    """with open("numbersValid.txt") as file:
        for i,line in enumerate(file):
            if int(line) not in sumValid:
                print(int(line), i,  "dont match")
            else:
                sumValid.remove(int(line))
        print(sumValid)"""
            
end_time = datetime.datetime.now()
print(end_time - start_time)    
        


