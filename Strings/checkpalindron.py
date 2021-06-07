
from sys import stdin


def isPalindrome(string) :
    pal=string
    string=string[::-1]
    if pal==string:
        return string
    else:
        return False
	# Your code goes here























	


#main
string = stdin.readline().strip();
ans = isPalindrome(string)

if ans :
    print('true')
else :
    print('false')

