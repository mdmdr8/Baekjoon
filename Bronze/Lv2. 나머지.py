array = []
value = []
cnt = 0
for _ in range(10):
    array.append(int(input()))

for i in range(10):
    va = array[i] % 42
    value.append(va)

value = set(value)
print(len(value))

#STUDY

    #숏코딩
    # value = {int(input())%42 for _ in range(10)}
    # print(len(value))

    # 튜플로 풀어보기
    # value = (int(input())%42 for _ in range(10))
    # print(len(value))
    # TypeError: object of type 'generator' has no len()

    #리스트로 다시 변경해주면 통과
    # value = (int(input())%42 for _ in range(10))
    # print(len(list(value)))
