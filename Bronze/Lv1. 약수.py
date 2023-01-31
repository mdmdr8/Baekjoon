import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
array.sort()
print(array[0]*array[-1])

#STUDY

    # input()때문인지 for문 떄문인지 실행하니까, 런타임에러가 뜨고
    # sort()함수 안써줬더니 에러났다. 입출력 내용을 잘 봐야겠다.
    # 오랜만에 sort()함수 쓰니까. 다시 sort()와 sorted()함수의 차이점을 다시 정리하자면

    # sort()함수는 리스트명.sort() 형식으로 "리스트형의 메소드"이며 원본값을 직접 수정한다.
    # sorted()함수는 sorted(리스트명)형식으로 "내장 함수"이며 리스트 원본 값은 그대로이고 정렬 값을 반환한다.