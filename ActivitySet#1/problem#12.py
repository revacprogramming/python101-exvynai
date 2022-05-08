# Regular Expressions
# https://www.py4e.com/lessons/regex

#Note
#the code is working - tested with a different sample. the website is buggy

import re

fhandle = open("dataset/regex_sum_1543883.txt", "r")
total = 0
for line in fhandle:
    line = line.rstrip()
    number = re.findall('[0-9]+', line)
    if len(number) != 0:
        for num in number:
            total = total + int(num)
     
print(total)    
    


