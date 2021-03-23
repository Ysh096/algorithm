# DP(Dynamic Programming) 개요



### 1. Dynamic Programming이란?

큰 문제를 작은 문제로 나누어 푸는 것! 특히, 작은 부분문제에서 답의 중복이 일어나는 경우 이를 보완하는 방법을 고민한 결과 이름붙여진 개념이다.

피보나치 수열을 재귀적으로 구하는 경우를 생각하면 된다!

- 작은 문제들은 한 번만 풀어야 한다.
- 작은 문제에서 얻은 답을 큰 문제를 풀 때 이용한다.

이렇게 작은 문제의 답을 저장해놓고, 활용하여 중복 계산을 줄이는 것을 **Memoization**이라고 한다.



### 2. Top-down 과 Bottom-up

### 2.1 Top-down

Top-down은 위에서 아래로, 큰 문제부터 작은 문제로 나아가는 것을 말한다.

재귀함수로 구현하는 경우 Top-down 형식!

```python
def fibonacci_td(n):
    # memoization 배열에 이미 저장이 되어 있으면
    if memo[n] > 0:
        return memo[n]
    
    if n <= 1:
        memo[n] = n
        return memo[n]
    
    else:
        memo[n] = fibonacci_td(n-1) + fibonacci_td(n-2)
        return memo[n]
```



### 2.2 Bottom-up

Bottom-up은 아래에서 위로, 작은 문제부터 큰 문제로 나아가는 것을 말한다.

```python
def fibonacci_bu(n):
    if n <= 1:
        return n
    
    fir = 0
    sec = 1
    for i in range(0, n-1):
        next = fir+sec
        fir = sec
        sec = next
    return next
```



어떤 정해진 방식이 있다기 보다는 센스의 문제인 것 같다. 풀이를 생각해 낼 수 있느냐, 반복되는 부분을 찾았느냐, 그 부분이 다시 반복되지 않도록 규제를 잘 걸어놓았느냐..



많은 문제를 풀어보며 익혀보도록 하자!