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

print(navigation)
print(maps)

start = "AAA"
step=0
while start!="ZZZ":
   for i in range(0, len(navigation)):
      start = maps[start][navigation[i]]
      step+=1
      print(start)

print(step)
