import datetime
start_time = datetime.datetime.now()

import re
str2num = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}

def replace_words(text):
    for k, v in str2num.items():
        text = text.replace(k, v)
    return text

def calibration(text):
    return sum(int(l[0] + l[-1]) for l in re.sub(r"[A-z]", "", text).split("\n")[:-1])

text = open("day1/input.txt").read()
#print(replace_words(text))
print(calibration(replace_words(text)))
end_time = datetime.datetime.now()
print(end_time - start_time)
