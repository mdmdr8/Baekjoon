n = int(input())
cnt = 0
num = n


while True :
    fir = num // 10
    sec = num % 10
    number = (fir + sec)%10
    num = (sec*10)+number
    cnt += 1
    if(num == n):
        break

print(cnt)

#STUDY

    # 1. n과 num 이 같아질 때까지 while문을 돌린다.
    # 2. 10의 자리 수를 구하는 것은 10으로 나눈 몫, 1의 자리 수를 구하는 것은 10으로 나눈 나머지를 활용하여 필요한 숫자를 만든다.
    # 3. 사이클이 돌때마다 cnt를 1씩 증가시킨다.