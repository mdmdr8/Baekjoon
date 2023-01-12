import sys

n = int(sys.stdin.readline())
meetings = []
for i in range(n):
    meetings.append(list(map(int, input().split())))

meetings = sorted(time, key=lambda x: (x[0], x[1]) )


cnt = 0 
meetings_end = 0 

for i in meetings:
    begin = i[0]
    end = i[1]
    if begin >= meetings_end: 
        conut += 1
        meetings_end = end

print(cnt)

