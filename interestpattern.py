n=int(input())
i=1
while i<=n:
    j=1
    star=chr(ord('A')-i-1)
    while j<=i:
        charp=chr(n+j+ord(star))
        print(charp,end="")
        
        j+=1
    print()
    i+=1
