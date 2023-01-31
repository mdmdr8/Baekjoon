bar_razor=list(input())
answer = 0
st = []

for i in range(len(bar_razor)):
    if bar_razor[i] == '(':
        st.append('(')

    else:
        if bar_razor[i-1] == '(':
            st.pop()
            answer += len(st)
        else:
            st.pop()
            answer += 1
print(answer)

#STUDY

    # 1. '(' st에 적재
    # 2. '('')'는 pop
    # 3. ')'는 +1
    # 인데(())에서 가운데 ()가 pop이 되면 ()가 남는데, 이것도 pop시키는 레이저였다.
    # 문제를 이해하는데 시간이 오래 걸렸다. 
