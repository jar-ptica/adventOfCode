from math import gcd
chars_to_remove = ["(", ")", " "]

navigation = []
maps = {}
with open('day8/input.txt') as file:
    for i, group in enumerate(file.read().strip().split('\n')):
      if i == 0:
        navigation = [ 0 if x=="L" else 1 for x in group]
      elif i> 1:
            key, values = group.split('=')
            for i in chars_to_remove:
               values = values.replace(i, "")
            values = values.split(",")
            maps[key.strip()] = values

cycles = []
start = [key for key in maps if key.endswith("A")]

for each in start:
   cycle=[]

   curent_steps = navigation
   step_count = 0 
   firstZ = None

   while True:
      while step_count==0 or not each.endswith("Z"):
         step_count+=1
         each = maps[each][curent_steps[0]]
         curent_steps = curent_steps[1:] + [curent_steps[0]]

      cycle.append(step_count)
      if firstZ is None:
         firstZ = each
         step_count = 0
      elif each == firstZ:
         break
         
   cycles.append(cycle)

nums = [cycle[0] for cycle in cycles]
print(nums)

lcm = nums.pop()

for num in nums:
   lcm= lcm*num//gcd(lcm, num)

print(lcm)

    
