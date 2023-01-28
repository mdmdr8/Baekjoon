n = int(input())

for _ in range(n):
    s = input()
    score = 0
    sum = 0  #새로운 리스트를 입력 받으면 리셋
    for i in s:
        if i == "O" :
            score += 1
        else:
            score = 0
        sum += score
    print(sum)

# #study
# https://my-archiver.tistory.com/62 
# 블로그에 설명