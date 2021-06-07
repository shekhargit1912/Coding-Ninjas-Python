
from sys import stdin


def removeAllOccurrencesOfChar(string, ch) :
    arr1=""
    arr2=""
    for i in range(len(string)):
        if string[i]==ch:
            arr1+=string[i]
            
        else:
            arr2+=string[i]
            
    return arr2
            
	# Your code goes here




























	

#main
string = stdin.readline().strip()
ch = stdin.readline().strip()[0]

ans = removeAllOccurrencesOfChar(string, ch)

print(ans)
