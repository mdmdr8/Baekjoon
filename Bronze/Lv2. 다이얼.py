dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
time = 0
alpha = input()

for i in alpha:
    for j in dial:
        if i in j:
            time += dial.index(j) + 3
print(time)