# DFS

Depth First Search

- 비선형구조인 그래프 구조로 표현된 자료를 탐색하는 방법
- 방문할 수 있는 가장 깊은 곳 까지 방문한 후 되돌아와 다른 경로를 탐색하는 방식

가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 깊이 우선 탐색을 반복해야 하므로 후입선출 구조의 **스택** 사용



##### 그래프에 대한 DFS 예시

```
			A
		  /   \
		 B     C
	    /  \  /
	   D     E
	     \   |
	         F - G
	         
 A  B  C  D  E  F  G
[F, F, F, F, F, F, F]  <-- visited 배열
```

위와 같은 그래프가 있다고 할 때, DFS 과정은 다음과 같다.

1) A 방문

```python
visited[A] = True
```

2) A에 연결된 정점 중에 방문하지 않은 정점 B, C가 있으므로 A를 스택에 넣고(되돌아오기 위해), 인접정점 B와 C중에서 오름차순에 따라 B를 선택하여 탐색을 계속한다.

```python
push(A)
visited[B] = True
```

3) B에 연결된 정점 중에 방문하지 않은 정점 D, E가 있으므로 B를 스택에 넣고, 인접정점 D와 E 중에서 오름차순에 따라 D를 선택하여 탐색을 계속한다.

```python
push(B)
visited[D] = True
```

4) D에 연결된 정점 중 방문하지 않은 정점 F가 있으므로, D를 스택에 넣고 F를 방문한다.

```python
push(D)
visited[F] = True
```

5) F에 연결된 정점 중 방문하지 않은 정점 G, E가 있으므로 F를 스택에 넣고 E를 방문한다.

```python
push(F)
visited[E] = True
```

6) E에 연결된 정점 중 방문하지 않은 정점 C가 있으므로 E를 스택에 넣고 C를 방문한다.

```python
push(E)
visited[C] = True
```

이제 남은 미방문 정점은 G 하나인데, 되돌아가는 과정에서 방문하게 될 것이다.

7) C에서 방문하지 않은 인접정점이 없으므로 마지막 정점으로 돌아가기 위해 스택을 pop하여 받은 정점 E(직전의 정점)에 대해서 방문하지 않은 인접정점이 있는지 확인한다.

```python
pop(stack) -> E를 돌려줌
```

8) E는 방문하지 않은 인접정점이 없으므로 한 번 더 pop!

```python
pop(stack) -> F를 돌려줌
```

9) F는 G를 방문하지 않았으므로 F를 스택에 넣고 G를 방문한다.

```python
push(F)
visited[G] = True
```

10) G에서 방문하지 않은 인접정점이 없으므로, 마지막 정점으로 돌아가기 위해 스택을 pop

```python
pop(stack)
```

...

계속 pop하여 A에 도달!

14) A에서 방문하지 않은 인접정점이 없으므로 마지막 정점으로 돌아가기 위해 스택을 pop 하는데, 스택이 공백이므로 깊이 우선 탐색을 종료한다.



## 백트래킹

어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더 이상 그 경로를 따라가지 않음으로써 시도의 횟수를 줄임

- 가지치기(Prunning)
- 불필요한 경로의 조기 차단

- N! 가지의 경우의 수를 가진 문제에 대해 백트래킹을 하면 일반적으로 경우의 수가 줄어든다. 하지만 최악의 경우에는 지수함수 시간만큼 요하므로 처리 불가능 할 수 있다.
- 어떤 노드의 유망성을 검토한 후 유망하지 않으면 부모 노드로 되돌아가기!



## 예제1. 깊이우선탐색 경로 출력해보기

다음은 연결되어 있는 두 개의 정점 사이의 간선을 순서대로 나열 해 놓은 것이다. 모든 정점을 깊이 우선 탐색하여 화면에 깊이우선탐색 경로를 출력하시오.

시작 정점: 1

```python
1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7
=> 출력 결과: 1-2-4-6-5-7-3
```



```python
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
```



## 예제2. swea 1219_길찾기

```python
# 재귀를 이용한 풀이

# dfs랑 약간 결이 다른듯? 그냥 stack 활용?
def dfs(v):
    global flag
    for i in roads[v]:
        if 99 in roads[i]:
            flag = 1
            return
        else:
            dfs(i)
    return

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
    flag = 0
    dfs(0)
    print('#{} {}'.format(tc, flag))
    
실행시간: 262ms
```

```python
# stack을 이용한 풀이

def dfs():
    while stack:
        start = stack.pop()
        if 99 in roads[start]:
            return 1
        else:
            # 재방문이 있으므로 방문 처리도 할 필요 없고, 그냥 다 방문해봐야 하므로!
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
```

방문처리를 할 필요가 없는 문제였다.



## 예제3. Power set

```python
def backtrack(a, k, input):
    global MAXCANDIDATES
    c = [0]*MAXCANDIDATES
    
    if k == input:
        process_solution(a, k) # 답이면 원하는 작업을 한다.
    else:
        # 답이 아니면 재귀 백트래킹
        k+=1
        ncandidates = construct_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)
            
# 후보군 생성
def construct_candidates(a, k, input, c):
    c[0] = True
    c[1] = False
    return 2

MAXCANDIDATES = 100
NMAX = 100
a = [0]*NMAX
backtrack(a, 0, 3) # 세 개의 원소로 이루어진 부분집합 구하기
```

```python
"""
1 ~ 10까지의 부분집합 중에서 합이 10이되는 부분집합 구하기
"""
N = 10
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # 구하고자 하는 부분 집합
sel = [0] * N # a 리스트 (내가 해당 원소를 뽑았는지 체크하는 리스트)

def power_set(idx):
    # idx가 N과 같아 질 때
    if idx == N:
        result = []
        for i in range(N):
            if sel[i]:
                result.append(arr[i])
        if sum(result) == 10:
            print(result)
        return # 혹은 조건 분기

    # sel의 idx번째 자리를 1로 바꾸고
    # idx 자리의 원소를 뽑고 진행
    sel[idx] = 1
    power_set(idx+1)

    # idx 자리의 원소를 뽑지 않고 진행
    sel[idx] = 0
    # 더 수행 할 코드가 없으면 -> 이 함수를 호출한 곳으로 돌아가자!
    power_set(idx+1)

# 함수 호출의 시작
power_set(0)
```



## 예제4. 백준9663_N-Queen

```python
n = int(input())

def dfs(queen, row, n):
    count = 0
    if n == row:
        return 1
    for col in range(n):
        queen[row] = col
        for i in range(row):
            if queen[i] == queen[row]: # 열 체크
                break
            if abs(queen[i]-queen[row]) == row - i: # 대각선 체크
                break
        else:
            count += dfs(queen, row + 1, n)
    return count

def solution(n):
    return dfs([0]*n, 0, n)

print(solution(n))
```

```python
# 유튜브 강의보고 내가 짠거

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
```



## 예제5. swea 4881_배열최소합

```python
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
        # 0행부터 확인
        k = 0
        while k < i:
            # 현재 행의 열과 k행의 열이 겹치는지 확인
            if cols[k] == cols[i]:
                flag = False
                # 겹치면 아무것도 하지 않고 j값을 다음 값으로!
                break
            # 안겹치면 다음 행 확인
            k += 1
        # flag = False가 되면 cols[i]에 저장된 값을 쓸 수 없음
        # 끝까지 안 겹쳤으면 다음 행 확인!
        if flag:
            # 핵심!
            min_sum(i+1, cols, result+num_list[i][j])
```

