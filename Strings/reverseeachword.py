
from sys import stdin


def reverseEachWord(string) :
    string=string.split()
    res=[]
    
    for i in string:
        res.append(i[::-1])
        
        
    sem=' '.join(res)
    return sem
    
    # Your code goes here


























	



#main
string = stdin.readline().strip()

ans = reverseEachWord(string)

print(ans)
