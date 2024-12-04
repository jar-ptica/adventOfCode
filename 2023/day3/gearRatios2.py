import datetime
start_time = datetime.datetime.now()

with open("day3/input.txt") as file:
    validNum = {}
    gears=[]
    lines = file.read().splitlines()
    for l, line in enumerate(lines):
        num = ""
        indx = ""
        # store all numbers and their indecies
        for c, chr in enumerate(line):
            if chr.isdigit():
                num += chr
                indx+= str(c)
                indx+= ","

            else:
                if c>0:
                    if line[c-1].isdigit():
                        num+= " "
                        indx+= " "
        # split string to list(crop last element if it is blank)
        num = num[0:-1] if num[-1] == " " else num
        num = num.split(" ")
        
        # get a list of indecies
        indx = indx[0:-1].split(" ")
        
        # if the whole line doesn't contain digits skip it
        if num == ['']:
            continue

        # for every number 
        for i,each in enumerate(num):
            # got min and max range of indicies
            numLen = indx[i].split(",")
            minR = int(numLen[0])
            maxR = int(numLen[-2] if numLen[-1]=="" else numLen[-1])
            
            # search for * in neiboring lines 
            for k in range(l-1 if l >0 else l, l+2 if (l+1)< len(lines) else l+1):
                for s in range(minR-1 if minR>0 else minR, maxR+2 if maxR < len(line)-1 else maxR+1):
                    if lines[k][s] == "*":
                        # if * appears twice in a dictionary that's a gear
                        if (k,s) in validNum.keys():
                            gears.append(validNum[k,s]*int(each))
                        else:
                            validNum[k,s] = int(each)
                                     
    #print(validNum)
    print(sum(gears))
    """with open("numbersValid.txt") as file:
        for i,line in enumerate(file):
            if int(line) not in gears:
                print(int(line), i,  "dont match")
            else:
                gears.remove(int(line))
        print(gears)"""
end_time = datetime.datetime.now()
print(end_time - start_time)


