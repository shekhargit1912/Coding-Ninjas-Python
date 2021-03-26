N=int(input())
sume=0
sumo=0
while N>0:
    k=N%10
    if k%2==0:
        sume=sume+k
    else:
        sumo=sumo+k
    N=N//10
        
               
print(sume," ",sumo)
