
from sys import stdin

def findTriplet(arr, n, x) :
    count=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
        	for k in range(j+1,len(arr)):
                   if arr[i]+arr[j]+arr[k]==x:
                   		count+=1
                   
    return count
                   
    #Your code goes her
    #return your answer





















#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().strip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n



#main
t = int(stdin.readline().strip())

while t > 0 :

    arr, n = takeInput()
    x = int(stdin.readline().strip())
    print(findTriplet(arr, n, x))
    t -= 1
