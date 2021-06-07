
from sys import stdin
import itertools
def removeConsecutiveDuplicates(string) :
    
    
   	return (''.join(i for i, _ in itertools.groupby(string)))
	# Your code goes here



























	


#main
string = stdin.readline().strip()

ans = removeConsecutiveDuplicates(string)

print(ans)
