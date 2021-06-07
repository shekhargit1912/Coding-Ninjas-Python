from sys import stdin


def rotate(arr, n, d):
    if d==0 or n==0:
        return arr

    d=d%n
    first=arr[d:]+arr[:d]
    return(first)
    








#Taking Input Using Fats I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#to print the array/list 
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    arr, n = takeInput()
    d = int(stdin.readline().rstrip())
    print(*rotate(arr, n, d))
    
    
    t -= 1
