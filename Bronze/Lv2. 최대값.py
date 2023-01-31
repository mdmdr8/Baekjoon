arr = [list(map(int, input().split())) for _ in range(9)]

temp = 0
n, m = 0, 0
for i in range(9):
    for j in range(9):
        if arr[i][j] >  temp :
            temp = arr[i][j]
            n, m = i, j
        else:
            temp = temp

print(temp)
print(n+1, m+1)