n = int(input())
cnt =1
for i in range(1, n+1):
    if n==0 :
        cnt = 0
    else :
        cnt*=i
print(cnt)