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

#STUDY

    # map은 map타입이고 map과 int는 TypeError를 발생시킨다.
    # 비교연산자는 같은 타입이여야 한다.