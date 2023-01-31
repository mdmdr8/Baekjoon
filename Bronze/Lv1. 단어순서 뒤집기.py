from collections import deque

n = int(input())
li=deque()

for i in range(n):
    li = input().split()
    li.reverse()
    print(f'Case #{i+1}:', ' '.join(li))
    li.clear()

#STUDY

    # 스택으로 풀어도 되지만 deque로 풀었음.
    # - input().split()은 list타입이고
    # - input()은 str타입
    # - f-string에서 ''이거 백틱 아님 주의! 홑따옴표
    # - reverse(), clear() 메소드 사용