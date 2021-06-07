## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
for i in range(1,n+1):
    for j in range(1,i):
        print(" ",end="")
    for k in range(i,n+1):
        print(k,end="")
    print()
for i in range(1,n):
    for j in range(n-i-1,0,-1):
        print(" ",end="")
    for k in range(n-i,n+1):
        print(k,end="")
    print()
