# import sys
# from pandas import DataFrame
#
# sys.stdin = open('input.txt')
#
# #V = 정점, E = 간선(edge)
# V, E = map(int, input().split())
# sequence = list(map(int, input().split()))
#
# G = [[0] * (V+1) for _ in range(V+1)]
#
# for i in range(E):
#     G[sequence[2*i]][sequence[2*i+1]] = 1
#     G[sequence[2 * i+1]][sequence[2 * i]] = 1
# #G = 인접 행렬
# # print(DataFrame(G))
#
# stack = []
# visit = [-1]*(V+1)
# i = 1
# while True:
#     j = 1
#     while j < V+1:
#         if visit[i] == -1: #방문표시가 안되어 있으면
#             visit[i] = True  # 방문 표시
#         if visit[j] == True: #만약 j에 이미 갔었으면
#             j += 1
#             continue #다음 j로
#         if G[i][j] == 1: #새로운 길이 있으면
#             stack.append(i) #정점을 스택에 쌓는다.
#             print(j)
#             i = j #다음 정점으로
#             break
#         else:
#             j += 1 #새로운 길이 아니면 또 다음 경로 확인
#     if j == V+1: #모든 열을 확인했는데 새로운 길이 없다?
#         if len(stack) > 0:
#             i = stack.pop()
#         else:
#             print(visit)
#             print('done!')
#             break

# 단방향
import sys
sys.stdin = open('input.txt')
def dfs():
    while stack:
        i = stack.pop()
        if visited[i] == -1:
            visited[i] = 1
        j = 1
        while j < E:
            if graph[i][j]: # i번 정점에서 볼 때 j번 정점으로의 길이 있으면

                # 방문여부 확인
                if visited[j] == 1: # j에 이미 방문했으면
                    j += 1
                else:
                    visited[j] = 1 # 길이 있는 j를 다 확인해 볼 필요는 없다.
                    stack.append(i)
                    print(j)
                    i = j
                    j = 1
            else:
                # i번 정점에서 j번 정점으로 가는 길이 없으면
                j += 1


V, E = map(int, input().split()) # 노드의 수, 간선의 수
# 인접 그래프 만들기
graph = [[0] * (V+1) for _ in range(V+1)]
visited = [-1] * (V+1)

edges = list(map(int, input().split()))
for i in range(E):
    graph[edges[2*i]][edges[2*i+1]] = 1


stack = [1]
dfs()