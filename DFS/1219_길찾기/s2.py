import sys
sys.stdin = open('input.txt')

# dfs랑 약간 결이 다른듯? 그냥 stack 활용?
def dfs():
    while stack:
        start = stack.pop()
        if 99 in roads[start]:
            return 1
        else:
            stack.extend(roads[start])
    return 0


for _ in range(10):
    tc, N = map(int, input().split())
    roads = [[]*100 for _ in range(100)]
    data = list(map(int, input().split()))
    for i in range(N):
        if roads[data[2*i]]:
            roads[data[2*i]].append(data[2*i+1])
        else:
            roads[data[2*i]] = [data[2*i+1]]
    visited = [0]*100
    stack = [0]
    result = dfs()
    print('#{} {}'.format(tc, result))
# A(0번 노드)에서 B(99번 노드)로 갈 수 있는가?
