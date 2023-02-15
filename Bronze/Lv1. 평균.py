n = int(input())
scores = list(map(int,input().split()))
max_score = max(scores)

fake_scores = []
for score in scores:
    fake_scores.append((score/max_score)*100)
avg_=sum(fake_scores)/n
print(avg_)

#STUDY

    # 다른 풀이
    # import sys

    # n = int(input())
    # score = list(map(int, input().split()))

    # high = max(score)

    # new_score = 0

    # total = 0
    # for sc in score:
    #     total += sc/high*100
    # new_score = total/len(score)
    # print(new_score)
