## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())

i=1
n1=(n+1)//2
n2=(n//2)
while i<=n1:
    sp=1
    while sp<=(n1-i):
        print(' ',end="")
        sp+=1
    
    j=1           
    while j<=(2*i)-1:
        print("*",end="")
        j+=1
        
    print()
    i+=1
   
i=n2
while i>=1:
    
    sp=1    
    while sp<=(n2-i+1):
        print(' ',end="")
        sp+=1
        
    j=1
    while j<=(2*i-1):
        print("*",end="")
        j+=1
        
    print()
    i-=1
