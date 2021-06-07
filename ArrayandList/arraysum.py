## Read input as specified in the question.
## Print output as specified in the question.
def sum(n):
    sum=0
    li=[int(x) for x in input().split()]
    for ele in li:
        sum+=ele
        
    print(sum)
  
n=int(input())
sum(n)
        
    
    
