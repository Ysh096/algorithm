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