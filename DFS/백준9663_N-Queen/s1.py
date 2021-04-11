import sys
sys.stdin = open('input.txt')

n = int(input())

def dfs(col, i):
    global answer
    if i == n+1:
        # print(col)
        answer += 1
        return
    for k in range(1, n+1):
        col[i] = k
        if promising(col, i):
            dfs(col, i+1)
        else:
            col[i] = 0

def promising(col, i):
    k = 1
    flag = True
    while k < i and flag:
        if col[k] == col[i] or abs(col[i] - col[k]) == i - k:
            flag = False
        k += 1
    return flag

col = [0]*(n+1)
answer = 0
dfs(col, 1)
print(answer)
