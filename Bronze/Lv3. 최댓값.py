import sys
li = []
temp = 0

for i in range(9):
    li.append(int(sys.stdin.readline()))
    if(li[i] > temp):
        temp = li[i]
        n = i
    else:
        temp = temp
print(temp)
print(n+1)