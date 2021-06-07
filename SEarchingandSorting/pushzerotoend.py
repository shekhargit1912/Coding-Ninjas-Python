def pushZerosAtEnd(arr, n) :
    arr2 = []
    arr3 = []
    for i in range(len(arr)):
        if arr[i]==0:
            arr2.append(arr[i])
        else:
            arr3.append(arr[i])
    arr3.extend(arr2)
    for j in range(len(arr3)):
        print(arr3[j],end=" ")
    print()
    
    
t = int(input())
for s in range(1, t+1, 1):
    n = int(input())
    arr = [int(x) for x in input().split()]
    if n==1:
        print(arr[0])
    else:
    	pushZerosAtEnd(arr,n)
