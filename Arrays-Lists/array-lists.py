# Array, List, Stack, Queue, Deque
#list
myList = [1,2,3,4,5]
type(myList)


myList = []
myList.append(1)
import array as arr
myArray = arr.array("i", [3, 6, 9, 12])
myArray.append(15)
myArray



myList = [1,2,3,4,5]
otherList = [6,7,8]
myList.extend(otherList)
myList


result = [0] * 8
result


type(result)



result[3] = 2
result


import sys
n = 30
myDynamicArray = []

for i in range(0,n):
    
    myLength = len(myDynamicArray)
    myByte = sys.getsizeof(myDynamicArray)
    print(f"Length: {myLength} Byte: {myByte}")
    myDynamicArray.append(n)