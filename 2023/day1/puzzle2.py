import datetime
start_time = datetime.datetime.now()
spellNumber = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] 

with open("day1/input.txt") as file:
  calValues = []
  for line in file:
    numbersinText = {}

    # find all spellNumbers in text with coressponded index
    for i, number in enumerate(spellNumber):
      if number in line:
        numbersinText[line.find(number)] = str(i+1)
        numbersinText[line.rfind(number)] = str(i+1)

    # find all digits in text with coressponded index
    for i, each in enumerate(line):
      if each.isdigit():
        numbersinText[i] = each

    a = min(numbersinText.keys())
    b = max(numbersinText.keys())
    calibrationValue = numbersinText[a] + numbersinText[b]
    #print(line, calibrationValue)
    calValues.append(int(calibrationValue))
  print(sum(calValues))
end_time = datetime.datetime.now()
print(end_time - start_time)




