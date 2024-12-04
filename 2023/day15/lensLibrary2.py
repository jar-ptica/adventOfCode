data =[]
with open("day15/input2.txt") as file:
    data = file.read().strip().split(",")

boxes=  { i : "[" + data[i] + "]" for i in range(0, len(data) ) }
print(boxes)
#print(data)
for i, each in enumerate(data):
    if "=" in each:
        boxes[i] = boxes[i].replace("=", " ")
        print(boxes)
    if "-" in each:
        boxes[i] = boxes[i].replace("-", " ")
