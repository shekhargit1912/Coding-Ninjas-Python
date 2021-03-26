n=int(input())
i=1

while i<=n:
    j=1
    while j<=i:
        strt=chr(ord('A')+i-1)
        print(strt,end='')
        j+=1
    
    print()
    i+=1
