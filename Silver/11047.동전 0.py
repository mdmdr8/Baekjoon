#입력
n, k = map(int, input().split())
coins = []
answer = 0
for _ in range(n):
    coins.append(int(input()))
coins.sort(reverse=True)

# 갖고 있는 돈이 나눠주는 동전보다 크거나 같아야 몫을 answer에 넣을 수 있다.
for coin in coins:
    if k >= coin:
        answer += k // coin
        k %= coin
        # 갖고 있는 돈이 0이하가 되면 for문을 멈춘다
        if k <= 0:
            break
print(answer)