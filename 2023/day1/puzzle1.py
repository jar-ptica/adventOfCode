with open("day1/input.txt") as file:
  calValues = []
  for line in file:
    digitList = []
    for each in line:
      if each.isdigit():
        digitList.append(each)
    calibrationValue = digitList[0] + digitList[-1]
    print(calibrationValue)
    calValues.append(int(calibrationValue))
print (calValues, sum(calValues))




