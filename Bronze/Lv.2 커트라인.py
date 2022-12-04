import sys

n, k = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

li.sort(reverse=True)

answer = li[k-1]
print(answer)

# #study
# sys.stdin.readline()은 끝에 /n이 붙고 str타입이다. 
# map()은 맵 객체 타입이다.

# sort()와 sorted()는 모두 리스트의 메소드이다.
# sort()는 기준에 따라 오름차순 내림차순 정렬을 한다.
# reverse()는 단순히 리스트의 순서를 뒤집는 것이다.

# arr.sort()는 원본 자체 정렬이다.
# arr.sort(reverse=True)는 역정렬이다.
# sorted(arr)는 새 정렬을 만든다.
