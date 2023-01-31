import sys
n = int(input())
arr = []
for _ in range(n):
    arr.append(sys.stdin.readline().strip())
arr_list = list(set(arr))
arr_list.sort()
# print(arr_list)
arr_list.sort(key=len)
# print(arr_list)


for i in arr_list:
    print(i)



#STUDY

    # 1.길이가 짦은 것 부터
    # 2.길이가 같으면 사전 순으로
    # 라는 조건이 존재한다.
    # arr_list.sort()를 print해보면 길이가 아닌 알파벳순으로 정렬된다.
    # 알파벳순 정렬 이후 arr_list.sort(key=len)길이순으로 정렬해주면 통과!