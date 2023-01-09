import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
array.sort()
min=0
for i in range(n):
    min+= array[i]*(n-i)

print(min)