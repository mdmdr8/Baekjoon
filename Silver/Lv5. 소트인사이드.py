n = input()
li = []
for i in range(len(n)) :
    li.append(int(n[i]))

n = sorted(n, reverse=True)
n = ''.join(n)
n = int(n)
print(int(n))

#STUDY

    # 다른 사람 풀이
    # n = list(map(int, input()))
    # n.sort(reverse=True)
    # for i in n:
    #     print(i, end='')
