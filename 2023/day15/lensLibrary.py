data =[]
with open("day15/input.txt") as file:
    data = file.read().strip().split(",")

decode = []
for each in data:
    value = 0
    for c in each:
        value += ord(c)
        value*=17
        value%=256
    decode.append(value)

print(decode)
print(sum(decode))
