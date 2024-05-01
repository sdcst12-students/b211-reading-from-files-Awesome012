#!python
# Sum of Values

"""
The file task03.txt contains a lot of data.  Each cluster of data is the number of points for that particular group.  Each blank line indicates a separator before the next group.
Read the contents of task03.txt into your program and determine the points value of the cluster with largest sum.

For sample data task03.txt, the largest sum should be 68787
"""

filename = 'task02a.txt'
file = open(filename,'r')
data = file.read()
myList = data.split('\n',)
finalList = []

def test():
    checklist = []
    while True:
        myList.pop(0)
        if myList[0] == "":
            cool = sum(checklist)
            finalList.append(cool)
            break
        else:
            checklist.append(int(myList[0]))
            
            

while True:
    try:
        test()
    except:
        finalList.sort()
        print(finalList[-1])
        break
    else:
        test()
