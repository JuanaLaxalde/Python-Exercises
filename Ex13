# In this assignment you will read through and parse a file with text and numbers
# You will extract all the numbers in the file and compute the sum of the numbers.
# The basic outline of this problem is to read the file, look for integers using the re.findall(),
# looking for a regular expression of '[0-9]+' and then converting the extracted strings to
# integers and summing up the integers.

fhandle = open('actualdata.txt')
sum = 0
import re
for line in fhandle:
    lines = line.rstrip()
    numbers = re.findall(('[0-9]+'), lines)
    for value in numbers:
        inum = int(value)
        sum = sum + inum
print(sum)
