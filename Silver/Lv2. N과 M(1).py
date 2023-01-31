n, m = map(int, input().split())
s=[]

def dfs() :
    if len(s) == m:
        print(' '.join(map(str,s)))
        return

    for i in range(1, n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
dfs()

#STUDY

    # 백트래킹 : 일반적인 DFS와의 차이점은 가지치기를 한다는 점이다.
    # 모든 경우의 수를 탐색하는 대신 조건을 걸어서 유망하지 않은 경우에는 탐색을 중지하고 이전 노드로 돌아가서 다른 경우를 탐색한다.
    # m이 커질수록 반복문을 계속 중첩시킬 수는 없기 때문에 백트래킹을 사용해야한다.
