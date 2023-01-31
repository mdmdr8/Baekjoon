n = int(input())

cnt = 0

while n >= 0:
    if n % 5 == 0:
        cnt = n // 5
        print(cnt)
        break

    n -= 3
    cnt += 1
else:
    print(-1)

#STUDY

    # 파이썬에서는 for-else 혹은 while-else 구문을 쓸 수 있다는 걸 알았다.
    # for-else와 while-else는 중간에 break와 continue를 사용하지 않고 끝까지 수행되었을 때, else문이 작동된다.
    # else의 들여쓰기는 for, while문과 일치해야 한다.