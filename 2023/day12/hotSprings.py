records = {}
with open("day12/input2.txt") as file:
    for  group in file.read().strip().split('\n'):
        key, values = group.split(' ')
        value = [int(x) for x in values.split(",")]
        records[key] = value

for spring, condition in records.items():
    txt = [x for x in spring.split(".") if  x!=""]
    for i, each in enumerate(txt):
        if "?" not in each:
            condition.remove(len(each))
            txt.remove(each)
    count = 0
    for i, each in enumerate(txt):
        if len(txt)==len(condition):
            if len(each)==condition[i]:
                continue
            count+=len(each)/condition[i]
        else:
            hashes=[]
            countHash = 0
            for c in each:
                if c=="#":
                    countHash+=1
                else:
                    hashes.append(countHash)
                    countHash=0
            hashes = hashes.remove(0)
        #print(hashes)
    if count==0:
        count+=1


    print(count)
