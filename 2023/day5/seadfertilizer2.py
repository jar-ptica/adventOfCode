import datetime
start_time = datetime.datetime.now()
import multiprocessing
almanac = {}
#f = open("numbersValid.txt", "w")
mergedPairs = []
#seads = []

def merge_intervals(intervals):
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    interval_index = 0
    #print(sorted_intervals)
    for  i in sorted_intervals:

        if i[0] > sorted_intervals[interval_index][1]:
            interval_index += 1
            sorted_intervals[interval_index] = i
        else:
            sorted_intervals[interval_index] = [sorted_intervals[interval_index][0], i[1]]
    #print(sorted_intervals)
    return sorted_intervals[:interval_index+1]

with open("day5/input.txt") as file:
    #seads = lines[0].split(":")[1][1:].split(" ")

    for i, group in enumerate(file.read().split('\n\n')):
      if i == 0:
        seadNum = group.split(":")[1][1:].split(" ")
        pairs=[]
        for m in range(0, len(seadNum), 2):
            pairs.append([int(seadNum[m]), int(seadNum[m]) + int(seadNum[m+1])])
        
        mergedPairs = merge_intervals(pairs)
        #print(k)
        """f.write(str([x for x in range(k[0], k[1])]))
        f.write('\n')"""
        
      else:
            key, *val = group.split('\n')
            almanac[key] = []
            for v in  val:
                if v=="":
                    continue
                param = v.split(" ")
                array = [int(param[1]), int(param[2]) + int(param[1]), int(param[0])]
                almanac[key].append(array)


def getMin(seads=[], almanac=almanac):
    num = []
    for i,each in enumerate(seads):
        sead = int(each)
        #print(sead)
        for key, map in almanac.items():
            #print(key)
            for t in map:
                inRange = False
                if (sead in range(t[0], t[1]) and inRange==False):
                    #print(sead, sead - t[0] + t[2])
                    sead = sead - t[0] + t[2]
                    #print(True, sead)
                    break
                else:
                    #print(False, sead)
                    sead= sead
        #print("")
      
        num.append(sead)
    return (min(num))

def printVal(k):
    seads = [x for x in range(k[0], k[1])]
    return (getMin(seads))

#pool_obj = multiprocessing.Pool()
print(mergedPairs)
answers = []
for k in mergedPairs[1:2]:
    print(k)
    ans = printVal(k)
    #ans = pool_obj.map(printVal, k)
    print(ans)
    #answers.append(ans)

#pool_obj.close()

#print(answers)
#print(min(answers))

"""with open("numbersValid.txt") as file:
    minLines = []
    for line in file.read()[0:-1].split('\n'):
        seads = line[0:-1].split(" ") 
        minLines.append(getMin(seads, almanac))
    print(min(minLines))    
"""
end_time = datetime.datetime.now()
print(end_time - start_time)
    


