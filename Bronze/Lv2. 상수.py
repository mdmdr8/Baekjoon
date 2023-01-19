num1, num2 = input().split()

num1 = int(num1[::-1]) #역순
num2 = int(num2[::-1]) #역순

if num1 > num2 :
    print(num1)
else:
    print(num2)

# study
# str, list, tuble만 문자열을 분리할 수 있다.
# 정수형에서 '인덱싱' 및 '슬라이싱'을 시도하려고 할 때 TypeError가 발생한다.

# 삼항연산자
# print(num1) if num1 > num2 else print(num2)