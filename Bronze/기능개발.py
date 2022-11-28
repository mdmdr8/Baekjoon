def solution(p, s):
    answer = []
    while p:
        cnt=0
        while p and p[0] >= 100:
            cnt += 1;
            p.pop(0)
            s.pop(0)
        #작업 리스트의 진도 증가
        p = [p[i]+s[i] for i in range(len(p))]
        #만약 오늘 기능이 배포되었다면 결과리스트에 추가
        if cnt:
            answer.append(cnt)

    return answer
