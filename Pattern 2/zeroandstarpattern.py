## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
start=1
end=2*n+1
mid=n+1
row=1
while(row<=n):
    column=1
    while column<=(2*n+1):
        if column==start or column==end or column==mid:
            print("*",end='')
        else:
            print("0",end="")
        column=column+1
    start=start+1
    end=end-1
    row=row+1
    print()
