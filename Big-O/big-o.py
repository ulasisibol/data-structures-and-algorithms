#BIG O NOTATION
#Time Complexity - Space Complexity
#https://www.bigocheatsheet.com/

#BRUTE FORCE => O(n)


def bigOn(n):
    for i in range(0,n):
        print(i)

bigOn(10)


def bigOn2(n):
    for i in range(0,n):
        for j in range(0,n):
            print(i,j)

bigOn2(10)

def bigOn3(n):
    for i in range(0,n):
        for j in range(0,n):
             for k in range(0,n):
                print(i,j,k)

bigOn3(5)


import math
def logn(n):
    while n > 1:
        n= math.floor(n/2)
        print(n)

logn(8)