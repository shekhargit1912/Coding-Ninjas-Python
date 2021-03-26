N=int(input())
a = 0
b = 1
while N>1:
    c = a+b
    a = b
    b = c
    N-=1
    
print(b)
