import sys
sys.stdin = open('input.txt', 'r')
#A 도시에서 B 도시로 가는 길이 존재하는지 알아내는 프로그램
#A = 0, B = 99
def find_way(graph):
    stack = [0]
    visit = []
    while stack:
        pos = stack.pop()  # 현재 위치
        if 99 in graph[pos]:
            return 1
        else:
            for i in graph[pos]:
                if i not in visit: #봤던 길은 다시 보지 않도록
                    stack.append(i)
                    visit.append(i)
    #0에서 시작하여 99를 찾지 못하고 stack이 비어버린 경우(1과 관련된 모든 경로 확인완료)
    return 0

for _ in range(10):
    tc, E = map(int, input().split()) #테스트 케이스 번호, edge(경로)
    edges = list(map(int, input().split()))
    graph = [[] for _ in range(100)]
    i = 0
    while i < len(edges)//2:
        graph[edges[2*i]] += [edges[2*i+1]]
        i += 1

    #경로찾기
    print('#{} {}'.format(tc, find_way(graph)))