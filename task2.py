"""
Read the data from one of the task02 text files.
The data from this file contains 3 numbers on each line.  Determine how many lines of this file contains Pythagorean triples.
Pythagorean triples are numbers where all of the sides are integers, and the 3 sides form a right triangle.
The triples contained are : { 2a : 6, 2b: 4, 2c: 11}
"""
import math

filename = 'task02c.txt'
file = open(filename,'r')
data = file.read()
myList = data.split('\n',)
total = 0

def pythagorean():
    global total
    numberA = myList[0]
    numberB = myList[1]
    numberC = myList[2]
    testlist = []
    testlist.append(numberA)
    testlist.append(numberB)
    testlist.append(numberC)
    testlist.sort()
    numberA = int(testlist[0])
    numberB = int(testlist[1])
    numberC = float(testlist[2])
    check = math.sqrt((numberA ** 2) + (numberB ** 2))
    if check == numberC:
        total = total + 1
    for i in range(4):
        myList.pop(0)

while True:
    try:
        pythagorean()
    except:
        print(f"there are {total} right triangles")
        break
    else:
        pythagorean()