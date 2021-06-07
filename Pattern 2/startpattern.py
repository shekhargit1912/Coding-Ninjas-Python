# ## Read input as specified in the question.
# ## Print output as specified in the question.

# n=int(input())
# i=1

# while i<=n:
#     space=1
#     while space<=n-i:
#         print(' ',end="")
#         space+=1
#     j=1
#     while j<=i:
#         print("*",end="")
#         j+=1
        
#     while i-1>=j:
#         print("*",end="")
        
#     print()
#     i+=1
    
        
    

n=int(input())
i=1
while i<=n:
    s=1
    while s<=n-i:
        print(" ",end='')
        s=s+1
    p=1
    j=1
    while j<=i:
        print("*",end='')
        p=p+1
        j=j+1
    ####decreasing sequence
    p=i-1
    while p>=1:
        print("*",end='')
        p=p-1
    print()
    i=i+1
    
    
