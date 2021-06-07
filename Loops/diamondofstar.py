## Read input as specified in the question.
## Print output as specified in the question.

n = int(input())
row = 1
while (row <= n // 2 + 1):
    col = 1
    while (col <= n // 2 + 1 - row):
        print(" ", end = "")
        col = col + 1
    col = 1
    while (col <= row):
        print("*", end = "")
        col = col + 1
    col = 1
    while (col <= row - 1):
        print("*", end = "")
        col = col + 1
    print()
    row = row + 1

row = 1
while (row <= n // 2+1):
    col = 1
    while (col <= row):
        print(" ", end = "")
        col = col + 1
    col = 1
    while (col <= n // 2+1  - row):
        print("*", end = "")
        col = col + 1
    col = 1
    while (col <= n // 2 - row):
        print("*", end = "")
        col = col + 1
    print()
    row=row+1
