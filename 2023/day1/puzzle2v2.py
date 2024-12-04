import datetime
start_time = datetime.datetime.now()
spellNumber = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] 
sum =0
with open("day1/input.txt") as file:
    for line in file:
        nums= []
        for i, chr in enumerate(line):
            for val, name in enumerate(spellNumber):
                if name in line[i:i+len(name)]:
                    nums.append(str(val))
            if chr.isdigit() :
                nums.append(chr)
        sum += int(nums[0] + nums[-1])
print(sum)
end_time = datetime.datetime.now()
print(end_time - start_time)


