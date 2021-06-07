
import sys

def intersections(arr1, n, arr2, m) :
    #Your code goes here
    arr=[]
    for i in range(n):
        for j in range(m):
            if arr1[i]==arr2[j]:
                arr.append(arr1[i])
                arr2[j] -= arr2[j]
                break
    for k in range (len(arr)):
        print(arr[k],end=' ')
            

        
        
        
        
        # for j in range(m):
        #     arr2[j]=-1
        #     if arr1[i] in arr2[j]:
        #         li.append(arr1[i])
        #         return li
                























#Taking Input Using Fast I/O
def takeInput() :
    n = int(sys.stdin.readline().strip())
    if n == 0:
        return list(), 0

    arr = list(map(int, sys.stdin.readline().strip().split(" ")))
    return arr, n


#main
t = int(sys.stdin.readline().strip())

while t > 0 :
    arr1, n = takeInput()
    arr2, m = takeInput()

    intersections(arr1, n, arr2, m)
    print()

    t -= 1
