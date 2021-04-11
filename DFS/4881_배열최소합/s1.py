# NxN 배열의 한 줄에서 하나씩 숫자를 골라 합이 최소가 되도록 만들기
import sys
sys.stdin = open("input.txt")

# def dfs(picked, total, visited):
#     '''
#     picked: 현재까지 선택한 숫자의 개수 -> 행의 인덱스로 사용
#     total: 현재까지 선택한 숫자들의 합
#     visited: 열 체크
#     '''
#     global min_val
#     # 현재까지 더한 값이 현재 최솟값보다 크면 더 이상 볼 필요 없음
#     if total > min_val:
#         return
#     # N개를 모두 선택했을 때 최솟값 비교
#     if picked == N:
#         min_val = min(min_val, total)
#         return
#
#
#     for x in range(N):
#         '''
#         2 1 2
#         5 8 5
#         7 2 2
#         '''
#         # 이전에 x열을 선택했다면 넘어간다.
#         if visited[x]:
#             continue
#         else:
#             # 이전에 x열을 선택하지 않았다면 선택
#             # total에 값을 더한다.
#             visited[x] = 1
#             total += matrix[picked][x]
#             dfs(picked+1, total, visited)
#             # 돌아왔을 때 원상복구
#             visited[x] = 0
#             total -= matrix[picked][x]
#
# test_case = int(input())
# for tc in range(test_case):
#     N = int(input())
#     matrix = [list(map(int, input().split())) for _ in range(N)]
#     # 열에 있는 숫자를 선택했는지 판단하는 리스트
#     # 1이면 해당 열을 방문한 상태
#     visited = [0 for _ in range(N)]
#
#     min_val = 100 # 최대 90이 나올 수 있기 때문에 설정한 값
#     dfs(0, 0, visited)
#     print("#{} {}".format(tc+1, min_val))
def min_sum(visit, picked, part_sum):
    global min_val
    if picked == N:
        if part_sum < min_val:
            min_val = part_sum
        return

    for x in range(N):
        if visit[x] == 1:
            continue
        else:
            visit[x] = 1
            part_sum += board[picked][x]
            min_sum(visit, picked+1, part_sum)
            visit[x] = 0
            part_sum -= board[picked][x]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visit = [0 for i in range(N)]
    picked = 0
    min_val = 100
    min_sum(visit, 0, 0)
    print(min_val)