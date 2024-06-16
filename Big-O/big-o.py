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


import math
def nlogn(n):
    lim= n
    while n > 1:
        n= math.floor(n/2)
        for i in range(1,lim):
            print(i)

nlogn(16)



def twotonfibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return twotonfibonacci(n-1) + twotonfibonacci(n-2)

twotonfibonacci(9)



def nfactorial(n):
    if n == 0:
        print("1")
        return
    else:
        for i in range(0,n):
            print(i)
            nfactorial(n-1)

nfactorial(3)


counter = 0
def actualFactorial(n):
    global counter
    counter += 1
    print(counter)
    if (n==1 or n==0):
        return 1
    else:
        return (n * actualFactorial(n - 1))
    
actualFactorial(8)


