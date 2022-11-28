# is~() 메서드를 사용하여 최종 제출했다. 


import sys

#테스트 케이스가 몇 개인지 주어지지 않았기 때문에 EOFError 검사도하고 while로 돌린다.
while True:
    line = sys.stdin.readline().rstrip('\n')
    up, lo, sp, nu = 0, 0, 0, 0
    
    if not line:
        break
    for l in line:
        if l.isupper():
            up += 1
        elif l.islower():
            lo += 1
        elif l.isdigit():
            nu += 1
        elif l.isspace():
            sp += 1
    # import sys로 입력 받으면 sys.stdout.write으로 출력 
    sys.stdout.write(f"{lo} {up} {nu} {sp}\n")
    
    

    ///study
    isupper()는 아스키코드로 65~90에 해당하고 'A'~'Z'까지를 의미한다.    
    islower()는 아스키코드로 97~122에 해당하고 'a'~'z'까지를 의미한다.
    isdigit()는 아스키코드로 48~57에 해당하고 0~9까지를 의미한다.
    isspace()는 아스키코드로 32에 해당하고 공백을 의미한다.
    
    sys가 아닌 input()을 사용하면, try except문으로 EOFError를 처리해주면 된다.
    sys의 입력에 '\n'도 space로 포함시키기 때문에 strip을 해줘야한다. 공백과 \n을 구분해야한다.
    따라서, rstrip('\n') 또는 sys.stdin.readline()[:-1]를 사용할 수 있다.
