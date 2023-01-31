t = int(input())

for _ in range(t):
    r, s = input().split()
    p = []
    for i in s:

        for _ in range(int(r)):
            p.append(i)
    print(''.join(p))

#STUDY

    # t = int(input())

    # for _ in range(t):
    #     r, s = input().split()
    #     for x in s:
    #         print(x*int(r), end='')
    #     print() #줄넘김