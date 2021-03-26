n=int(input())
i=1
while i<=n:
    j=1
    sta=chr(ord('A')+i-1)
    while j<=i:
        charp=chr(ord(sta)+j-1)
        print(charp,end="")
        j+=1
	
    print()
    i=i+1
