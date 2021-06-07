def checkPalindrome(num):
    n1=str(num)
    temp=n1
    if n1[::-1]==temp:
        return 1
    else:
        return 0
 
#Implement Your Code Here

	
		
num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')
