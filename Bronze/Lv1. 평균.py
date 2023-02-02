n = int(input())
scores = list(map(int,input().split()))
max_score = max(scores)

fake_scores = []
for score in scores:
    fake_scores.append((score/max_score)*100)
avg_=sum(fake_scores)/n
print(avg_)