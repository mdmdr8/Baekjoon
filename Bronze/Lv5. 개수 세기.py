n = int(input())
arr = list(map(int, input().split()))
fix = int(input())
cnt = 0

for i in arr:
    if fix == i:
        cnt += 1
print(cnt)

