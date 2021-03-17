# Stack 응용

### 괄호 매칭

```python
"""
괄호 매칭
1. 괄호의 종류 - [], {}, ()
2. 괄호 매칭의 조건 
- 왼쪽 괄호의 개수와 오른쪽 괄호의 '개수'가 같아야 한다.
- 같은 괄호에서 왼쪽 괄호는 오른쪽 괄호보다 '먼저' 나와야 한다.
 - 괄호 사이에는 포함 관계만 존재한다.
3. 잘못된 사용의 예시
(a(b) -> 괄호 개수
a(b)c) -> 괄호 개수
a{b(c[d]e}) -> 괄호가 올바르게 매칭되지 않음
"""

# 소괄호만
stack = []
def push(item):
    stack.append(item)

def pop():
    if len(stack): #stack이 비어있지 않으면
        return stack.pop(-1) #스택의 마지막 원소 꺼내기
    else:
        return "꺼낼 원소가 없습니다."

def is_empty(): #스택이 비어있는지 확인하는 함수
    if len(stack) == 0:  #만약 스택이 비어있으면
        return False #False 반환
    return True

def check_matching(data):
    for cha in data: #데이터의 각 문자에서
        if cha == '(': # ( 모양은 푸시해주고
            push(cha)
        elif cha == ')': # ) 모양을 만나면?
            if is_empty() == False: #스택이 비어있으면
                return '괄호 개수가 맞지 않습니다.'
            else:
                pop() #'('를 꺼내줌 ()가 하나 맞춰짐
    if len(stack) != 0: #순회가 다 끝난 후에
        return '괄호 개수가 맞지 않습니다.' #스택이 비어 있지 않으면
    return True #비어있으면
```



### 파스칼의 삼각형

​				1

​			1		1

​		1		2		1

​	1		3		3		1

1		4		6		4		1

이러한 형태의 삼각형을 파스칼 삼각형이라고 한다. 이 형태를 구현하는 방법을 스택으로 할 수 있을까?

우선은 그냥 for문을 이용하여 구현한 경우이다.

```python
import sys
sys.stdin = open('input.txt', 'r')
# 1. for문으로 풀기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    p_list = [[1]*(i+1) for i in range(N)] #행, 열의 개수에 맞는 이차원 배열 준비하기

    for i in range(N):
        if i > 1:
            for j in range(len(p_list[i])): #각 열별로
                if j > 0 and j < len(p_list[i])-1: #위치가 적절한 경우!
                    p_list[i][j] = p_list[i-1][j-1] + p_list[i-1][j] #왼쪽 위와 오른쪽 위의 값을 합한 값을 대입
    print('#{}'.format(tc))
    for i in range(N):
        print(*p_list[i])
```



다음으로 이항정리, 조합을 이용한 풀이이다.

**파스칼의 삼각형에서 보이는 이항정리의 성질**

​							1C0        					     -> (x+y)^0 의 계수

​					1C0		1C1 					     -> (x+y)^1 의 계수

​			2C0		2C1		2C2				    ->(x+y)^2의 계수

​		3C0		3C1		3C2		3C3	     ->(x+y)^3의 계수

4C0		4C1		4C2		4C3		4C4   ->(x+y)^4의 계수

재귀함수에 사용할 수 있는 점화식, nCk = n-1_C_k-1 + n-1_C_k를 얻을 수 있다.

```python
# 2. 조합 재귀함수 이용하기
#파스칼의 삼각형에서 발견할 수 있는 이항정리의 각 항의 성질!
#nCk = n-1_C_k-1 + n-1_C_k
#이를 바탕으로 조합의 combination을 구성하면?
def combination(n, k):
    arr[n][k] += 1 #호출횟수 세어보기 위함
    if k == 0 or k == n: #양끝인 경우 return 1
        return 1
    return combination(n - 1, k - 1) + combination(n - 1, k) #그 외의 경우에는 점화식 사용

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * (i+1) for i in range(N)] #호출을 세어보기 위한 리스트
    print('#{}'.format(tc))
    for n in range(N):
        for k in range(n+1):
            print(combination(n, k), end = ' ') #제대로된 출력값을 얻을 수 있다.
        print()
#     print(arr)
# N = 6일 때, arr = [[1], [16, 16], [8, 15, 8], [4, 7, 7, 4], [2, 3, 3, 3, 2], [1, 1, 1, 1, 1, 1]]
```

다만 이 경우에 N이 커지면 커질수록 함수 호출 및 계산량이 기하급수적으로 늘어난다. 

한 번 한 계산을 계속해서 중복 계산하기 때문이다. 이를 막기 위한 획기적인 방법을 오늘 배웠다.



```python
# 3. 스택?인지는 모르겠고 여기서 두 번 검사할 필요 없게 만드는 방법
#N이 매우 커질 때 그냥 재귀와는 비교할 수 없을만큼 빠르다! for문이랑 속도가 비슷함.
def combination(n, k):
    # arr[n][k] += 1
    if k == 0 or k == n:
        comb[n][k] = 1
    elif comb[n][k] == -1: #만약 배열이 -1값을 가진다면(아직 값이 채워지지 않았다면)
        comb[n][k] = comb[n-1][k-1] + comb[n-1][k] #모든 결과를 배열에 저장! (일종의 스택이 아닐까?)
    return comb[n][k] #값이 채워져 있는 경우에는 그 값을 반환한다. (두 번 계산하지 않음!)
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # arr = [[0] * (i + 1) for i in range(N)] #몇 번 호출되는지 파악해보자.
    comb = [[-1]*(i+1) for i in range(N)] #combination값을 저장할 이차원 배열 만들기
    print('#{}'.format(tc))
    for n in range(N):
        for k in range(n+1):
            print(combination(n, k), end = ' ')
        print()
    # print(arr)
# N=6일 때, arr = [[1], [1, 1], [1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
```

