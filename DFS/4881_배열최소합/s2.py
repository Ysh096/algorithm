import sys
sys.stdin = open('input.txt')

def min_sum(i, cols, result):
    global min_val

    # 백트래킹
    if result > min_val:
        return

    # 끝까지 확인했을 때
    if i == N:
        # 최솟값이면 저장
        if min_val > result:
            min_val = result
        return

    for j in range(N):
        cols[i] = j
        flag = True
        k = 0
        while k < i:
            if cols[k] == cols[i]:
                flag = False
                break
            k += 1
            # flag = False가 되면 cols[i]에 저장된 값을 쓸 수 없음
        if flag:
            min_sum(i+1, cols, result+num_list[i][j])



T = int(input())

for tc in range(1, T+1):
    N = int(input())

    num_list = [list(map(int, input().split())) for _ in range(N)]

    # 행별로 선택한 열을 저장
    result = 0
    min_val = 9999999999
    cols = [-1]*N
    min_sum(0, cols, result)
    print('#{} {}'.format(tc, min_val))