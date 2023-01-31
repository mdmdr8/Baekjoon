import sys

n = int(sys.stdin.readline())
meetings = []
for i in range(n):
    meetings.append(list((map(int, sys.stdin.readline().split()))))


# 먼저, 종료 시간을 기준으로 오름차순 정렬
# 다음, 시작 시각을 기준으로 오름차순 정렬
meetings = sorted(meetings, key=lambda x: (x[1], x[0]) )


cnt = 0 # 회의 개수를 저장할 변수
meetings_end = 0 #최종 회의 종료 시각 초기값 설정

for i in meetings:
    begin = i[0]
    end = i[1]

    #회의 시작 시각이 최종 회의 종료 시각보다 같거나 크면
    if begin >= meetings_end:
        cnt += 1
        meetings_end = end

print(cnt)

#STUDY

    # begin, end = (map(int, sys.stdin.readline().split()))
    # meetings.append([begin, end])
    # 위와 같이 따로 변수를 받는 것보다 list()로 한 줄로 묶어서 수행하니 4ms정도 빨라짐