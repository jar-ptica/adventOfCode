almanac = {}
seads = []
with open("day5/input.txt") as file:
    #seads = lines[0].split(":")[1][1:].split(" ")

    for i, group in enumerate(file.read().split('\n\n')):
      if i == 0:
        seads = group.split(":")[1][1:].split(" ")
      else:
            key, *val = group.split('\n')
            almanac[key] = []
            for v in  val:
                if v=="":
                    continue
                param = v.split(" ")
                array = [int(param[1]), int(param[2]) + int(param[1]), int(param[0])]
                almanac[key].append(array)
#print(seads)                
num = []
for i, each in enumerate(seads):
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
                
                
print(min(num))


    


