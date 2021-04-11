#재귀버전 dfs(depth first search)

import sys
sys.stdin = open('input.txt')

#V = 정점, E = 간선(edge)
V, E = map(int, input().split())
sequence = list(map(int, input().split()))

graph = [[0] * (V+1) for _ in range(V+1)]
#G = 인접 행렬
for i in range(E):
    graph[sequence[2*i]][sequence[2*i+1]] = 1
    graph[sequence[2 * i+1]][sequence[2 * i]] = 1

visit = [0]*(V+1)
stack = []
start = 1
print('경로: {}'.format(start), end = '->')
def dfs_recurssion(start, graph, visit):
    i = 1
    while i < len(graph[start]):
        visit[start] = start
        if graph[start][i] == 1 and i not in visit: #가보지 않은 길이 있으면
            stack.append(i) #스택에 쌓아주고
            start = i #다음 경로로 이동하자.
            print(start, end = '->')
            return dfs_recurssion(start, graph, visit)
        else:
            i += 1 #길이 없으면 다음 숫자 확인
    if i == len(graph[start]): #while문이 끝남 = 다 가본 길일 때
        if stack: #스택에 뭔가 들어있을 때
            start = stack.pop()
            return dfs_recurssion(start, graph, visit)
        else:
            return 'Done'
print(dfs_recurssion(start, graph, visit))
#결과# 경로: 1->2->4->6->5->7->3->Done