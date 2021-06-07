## Read input as specified in the question
## Print the required output in given format
n=int(input())
i=1
while i<=n:
    spac=1
    while spac<=n-i:
        print(' ',end='')
        spac+=1
    one=1
    while one<=i:
        print(one,end="")
        one+=1
    print()
    i+=1
