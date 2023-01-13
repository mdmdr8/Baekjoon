# '-'를 기준으로 괄호를 쳐준다

import sys

calculate = sys.stdin.readline().split("-")
num = 0

for i in calculate[0].split('+'):
    num += int(i)

for i in calculate[1:]:
    for j in i.split('+'):
        num -= int(j)

print(num)

