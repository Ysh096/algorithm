# 연결 리스트(Linked List)

참고자료: 자료구조와 함께 배우는 알고리즘 입문(파이썬 편), Bohyoh Shibata 지음, 강민 옮김

대부분의 코드는 위 책에서 그대로 가져왔습니다.



## 1. 리스트

리스트는 순서가 있는 데이터를 늘어놓은 자료구조이다. 단순한 리스트의 종류로 선형 리스트와 연결 리스트가 있다.

여기서 말하는 리스트는 파이썬에서 제공하는 list() 자료형과는 다른 좀 더 본질적인? 것이다.



## 2. 연결 리스트란?

연결 리스트는 A가 B에게, B가 C에게 차례대로 연락하는, 비상 연락망과 같은 구조로, 중간에 건너뛰어서는 안 된다. 이러한 A, B, C등의 리스트 원소를 노드(node)라고 하며, 노드는 데이터와 포인터를 가진다.

- 데이터: 노드가 가진 정보
- 포인터: 뒤쪽 노드를 가리키는(참조하는) 도구

맨 앞 노드를 머리 노드(head node), 맨 끝 노드를 꼬리 노드(tail node)라고 하며, 각 노드의 바로 앞 노드를 앞쪽 노드(predecessor node), 바로 뒤 노드를 뒤쪽 노드(successor node) 라고 한다.



### 2.1 배열로 연결 리스트 만들기(비효율적)

회원의 정보가 저장된 다음과 같은 데이터가 있다고 해 보자. (포인터는 없고, **인덱스로 앞, 뒤, 머리, 꼬리를 구분**함)

```python
data = [
    # 회원번호, 이름, 전화번호
    (12, 'john', '999-999-1234'),
    (12, 'Paul', '999-999-1235'),
    (12, 'Mike', '999-999-1236'),
    (12, 'Rita', '999-999-1237'),
    None,
    None,
]
```

위와 같이 데이터가 구성된 경우, 회원이 새로 가입하여 중간에 회원의 정보를 추가해야 할 때, 중간에 삽입한 이후의 데이터를 한 칸씩 뒤로 옮겨야 하는 문제가 발생한다. (**insert의 시간 복잡도 => O(n)**)

```python
data = [
    # 회원번호, 이름, 전화번호
    (12, 'john', '999-999-1234'),
    (12, 'Paul', '999-999-1235'),
    (57, 'Alan', '999-999-1238'), # 추가
    (12, 'Mike', '999-999-1236'), # 이후의 데이터는 한 칸씩 옮겨지게 됨
    (12, 'Rita', '999-999-1237'),
    None,
    None,
]
```

이렇게 한 칸씩 옮겨야 각 노드들이 각자의 앞쪽 노드와 뒤쪽 노드를 가지는 연결 리스트 상태를 유지할 수 있다.

이렇게 모든 데이터의 위치를 옮기는 것 보다는, **포인터를 이용하여 노드가 가리키는 주소만 바꿔주는 방법**을 이용하면 보다 효율적으로 삽입, 삭제를 할 수 있다.



### 2.2 포인터로 연결 리스트 만들기(class 이용)

포인터를 이용하기 위해서는 우선 노드에 포인터의 정보를 담아야 한다. 그림으로 표현하면 다음과 같다.

**next가 포인터의 역할을 하는 필드!**

![linked_list_node](연결 리스트(Linked List)_images/linked_list_node.jpg)

data는 데이터를 참조하고, next는 뒤쪽 노드를 참조한다. 그러나 일반적으로 데이터에 대한 참조는 따로 화살표로 표시하지 않는다.

노드를 구현하는 클래스를 작성해보면 다음과 같다.

```python
class Node:
    def __init__(self, data, next):
        # 초기화
        self.data = data # 데이터
        self.next = next # 뒤쪽 포인터
```

data는 데이터에 대한 참조이며, 임의의 형태를 가진다(Any형을 가리킴).

next는 뒤쪽 포인터이며, 뒤쪽 노드를 가리킨다. (Node형을 가리킴)



연결 리스트를 구현하는 클래스를 작성해보면 다음과 같다.

```python
class LinkedList:
    def __init__(self):
        # 초기화
        self.no = 0 # 노드의 개수
        self.head = None # 머리 노드
        self.current = None # 주목 노드
        
    def __len__(self):
        # 연결 리스트의 노드 개수 반환
        return self.no
```

위 클래스의 init 함수는 노드가 아직 하나도 없는 빈 연결 리스트를 생성한다. 주의할 점은, 노드가 없는 빈 연결 리스트라고 할지라도 head라는 것이 없는 건 아니라는  점이다. head는 노드의 머리 부분을 참조하는 역할일 뿐이고, 현재는 머리 부분이 없어 참조할 것이 없는 것이다.

len 함수는 연결 리스트의 길이를  반환하는 함수로, 그냥 현재 노드의 개수를 반환해주면 된다. 마치 list의 len처럼 list를 구성하는 원소의 개수를 세는 것과 같다.



**노드가 1개인 경우**

이제 노드가 1개 있는 경우를 살펴보자. 이 경우 head는 그 한 개 있는 노드(노드를 클래스로 구현했음을 잊지 말자)를 가리키면 되고, 이 head가 참조하는 뒤쪽 노드 next는 아무것도 참조하지 않으므로 None이 된다. 따라서 노드가 단 1개인지 확인하기 위해서는 다음의 식을 사용할 수 있다.

```python
head.next is None
또는
no == 1
```



**노드가 2개인 경우**

이제 노드가 두 개이고, 각각을 A, B라고 해 보자.

머리 노드를 A, 꼬리 노드를 B라고 하면, head에는 A노드가, head 노드의 next에는 B 노드가, B의 next에는 None이 들어간다. 연결 리스트의 노드가 2개인지는 다음 식으로 알 수 있다.

```python
head.next.next is None
또는
no == 2
```



**리스트의 원소를 검색하는 방법**

```python
def search(self, data):
    # data와 값이 같은 노드를 검색
    cnt = 0
    ptr = self.head
    while ptr is not None:
        if ptr.data == data:
            self.current = ptr
            return cnt
        cnt += 1
        ptr = ptr.next
    return -1
```

1) head node에서 시작

2) head node가 비어있지 않다면 반복문 시작

	- 만약 현재 노드의 데이터가 data와 같은 값이라면 cnt를 반환
	- 그렇지 않다면 cnt를 하나 늘리고, 다음 노드를 확인

3) 노드가 비어있다면 반복문이 종료되고 -1 반환

연결 리스트에서의 검색은 순차적으로 이루어지는 것 같다. 마치 트리구조에서 원하는 값을 찾는 것과 비슷한 느낌?



**중요: 머리에 노드를 삽입하는 add_first() 함수**

```python
	def add_first(self, data):
        # 맨 앞에 노드를 삽입
        ptr = self.head # 삽입하기 전의 머리 노드
        self.head = self.current = Node(data, ptr)
        self.no += 1
```

1) 삽입하기 전 머리노드 A를 참조하는 포인터를 ptr에 저장해둔다.

2) 삽입할 노드를 생성(Node(data, ptr)) -> **삽입하기 전 맨 앞 노드를 가리키는 노드**가 생성되는 것

3) head는 새로운 노드를 참조하도록 업데이트된다.

정리하자면, 뒤쪽 포인터로 현재의 head 노드를 가리키는 새로운 노드를 만든 후에, 이 새로운 노드를 head 노드로 업데이트 해주면 된다.



**중요: 꼬리에 노드를 삽입하는 add_last() 함수**

```python
	def add_last(self, data):
        # 맨 끝에 노드를 삽입
        if self.head is None:
            self.add_first(data) # 헤드가 비어있으면 넣어줌
        else:
        	ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next # 꼬리가 나올때까지 이동
            ptr.next = self.current = Node(data, None) # 새로운 노드를 만들고, 꼬리 부분에 추가
            self.no += 1
```

1) 헤드 부분부터 시작해서 꼬리를 찾아나간다.

2) 꼬리를 찾았으면, while문을 나오게 된다.

3) Node(data, None) 으로 뒤쪽 포인터가 None이고 data를 가지는 노드를 만든 후, 현재 노드의 next로 넣어준다.

정리해보면, 맨 앞부터 끝까지 이동한 후에 새로운 노드를 맨 끝의 next 부분에 넣어주면 된다.



**중요: 머리 노드 삭제 함수 remove_first()**

```python
	def remove_first(self):
        # 머리 노드를 삭제
        if self.head is not None:
            self.head = self.current = self.head.next
        self.no -= 1
```

1) head가 비어있지는 않은지 확인

2) 비어있지 않다면 head 노드에 head.next 노드를 넣어준다. (head의 참조 대상이 바뀌는 것)

노드 A의 정보를 지운다기 보다는 참조하지 않음으로써 삭제하는 방법이다.



**중요: 꼬리 노드를 삭제하는 remove_last() 함수**

```python
	def remove_last(self):
        if self.head is not None:
            if self.head.next is None: # 노드가 1개 뿐이라면
                self.remove_first() # 머리 노드를 삭제
            else: # 노드가 1개 초과라면
                ptr = self.head # 스캔 중인 노드
                pre = self.head # 스캔 중인 노드의 앞쪽 노드
                
                while ptr.next is not None: # 다음 노드가 있는 동안 순회
                    pre = ptr
                    ptr = ptr.next # 다음 노드로 넘어가는 동작
                # 순회가 끝나면 다음 노드가 없는 꼬리 노드에 도달하게 됨. (ptr이 꼬리노드)
                pre.next = None # 꼬리 노드인 ptr 바로 앞 노드 pre의 next를 None으로 바꿔줌.
                self.current = pre
                self.no -= 1
```

1) head가 비어있지 않은 동안(연결 리스트의 원소가 1개 이상인 경우에만) 검사를 진행

2) 노드가 1개라면 머리 노드를 삭제하는 것이 곧 꼬리 노드를 삭제하는 것과 같다.

3) 노드가 2개 이상이라면 **꼬리 노드 앞쪽의 노드가 가리키는 다음 노드를 None으로 바꿔준다.**

꼬리 노드를 직접 어떻게 하는 것이 아니라, 그 앞 노드가 가리키지 않도록 바꿔준다.



**가장 중요: 임의의 노드를 삭제하는 remove() 함수**

리스트가 비어있지 않고, 주어진 노드 p가 존재할 때 노드를 삭제한다.

다음의 두 가지 경우로 나뉜다.

- p가 머리 노드일 때: 머리 노드를 삭제하는 것이므로 remove_first()함수 호출
- p가 머리 노드가 아닐 때: 리스트에서 p가 참조하는 노드 D를 삭제한다.

```python
	def remove(self, p):
        # 노드 p를 삭제하는 함수
        
        if self.head is not None: # head가 비어있지 않을 때에만 아래 코드 실행
            if p is self.head: # p가 머리 노드이면
                self.remove_first()
            else: # p가 머리 노드가 아니면
                ptr = self.head # 포인터가 가리키는 노드를 head로 만든 후
                
                while ptr.next is not p: # ptr의 다음 노드가 p가 아니면
                    ptr = ptr.next # 다음 노드로 이동
                    if ptr is None: # 가리키는 노드가 없다면(꼬리에 도달하면)
                        return # remove 함수 종료
                # while문이 끝나고, 함수도 종료되지 않았다면 ptr은 곧 다음 노드가 p인 상태이다.
                ptr.next = p.next # p = p.next와 동일
                # 즉 p를 가리키는 부분을 없애고 바로 p 다음 노드를 가리키도록 만든 것.
                self.current = ptr
                self.no -= 1
```

1) 머리 노드가 비어있는지 확인

2) 머리 노드가 비어있지 않다면 p가 머리 노드인지 확인

3) p가 머리 노드이면 삭제해주고, 머리 노드가 아니면 p를 찾아 순회

4) p를 가리키는 노드가 없으면 함수 종료

5) p를 가리키는 노드에 도달했으면, p 대신 p 다음 노드를 가리키도록 변경



지금까지 **포인터를 이용하여** 노드 만들기, 연결 리스트 만들기, 연결 리스트 검색, 노드 삽입, 노드 삭제 등에 대해 알아보았다.

이러한 개념이 있기는 하지만, 실제 코딩테스트에서 이를 구현하여 사용하는 일은 없을 것이다. 다만 어떤 배열이 서로 연결되는 과정에 대해 알고 있으면 후에 혹시라도 비슷한 작업을 하게 된다면 이를 떠올리고 참고할 수 있지 않을까 생각한다.



### 2.3 커서로 연결 리스트 만들기

노드를 배열 안의 원소에 저장하고, 그 원소를 이용하여 연결 리스트로 구현하는 방법!

-  포인터를 이용한 연결 리스트는 노드를 삽입, 삭제할 때마다 내부에서 노드용으로 인스턴스를 생성한다. 이때 메모리를 확보하고 해제하는 비용을 무시할 수 없다고 한다. 프로그램을 실행하면서 데이터 개수가 크게 변하지 않거나, 데이터 최대 개수를 예측할 수 있는 경우, 배열 안의 원소를 사용하여 효율적으로 연결 리스트를 구성할 수 있다.

이게 지금까지 문제를 풀 때 사용한 **인접 리스트**같은 개념이 아닌가 생각한다. 코드가 너무 길어서 이번 시간을 통해 코드를 뜯어보지는 않을 것이지만, 개념만 살펴보면 다음과 같다.

1) 어떤 배열 데이터가 다음과 같이 주어진다.

```python
head = 2

index Data next
  0    D    2
  1    A    4
  2    E    5
  3    C    0
  4    B    3
  5    F   -1 # 꼬리
```

head가 가리키는 index에 해당하는 데이터가 머리 노드라고 할 수 있다.

next가 -1인 데이터가 꼬리 노드라고 할 수 있다.

그 외 모든 노드가 next에 어떤 index값을 가진다. 이는 곧 해당 인덱스와 연결되어 있음을 뜻한다.

인접 리스트와 매우 비슷한 것 같다. 데이터가 포함되어 있다는 점에 주목하여 인접 리스트로 이를 구현하면 다음과 같지 않을까?

```python
head = 1 # A가 머리 노드
linked_list = [('D', 2), ('A', 4), ('E', 5), ('C', 0), ('B', 3), ('F', -1)]
```

만약 어떤 원소를 추가해야 한다면, 미리 배열에 자리를 만들어 놓는 것이 좋을 것이다.

예를 들어, data = G, next = 1인 머리 노드를 하나 추가한다고 해 보자.

```python
# 삽입
head = 1
linked_list = [['D', 2], ['A', 4], ['E', 5], ['C', 0], ['B', 3], ['F', -1], 0]

# 삽입 후
head = 6
linked_list = [['D', 2], ['A', 4], ['E', 5], ['C', 0], ['B', 3], ['F', -1], ['G', 1]]
```

head는 6번 인덱스인 G를 가리키고, G는 1번 인덱스인 A를 가리키면서, A 앞에 G가 추가되는 것과 같아진다.

삭제는 포인터에서와 마찬가지로 할 수 있는데, 예를 들어 E를 삭제하려고 한다면, 다음과 같다.

1) E를 가리키는 노드를 찾는다.

2) D가 E를 가리킴을 알았다. 이제 E가 가리키는 노드도 확인한다.

3) E가 5번 노드를 가리키므로, D가 가리키는 노드를 5번 노드로 바꿔준다.

여기에 추가적으로 원한다면 E 데이터를 0으로 바꿔버려도 될 듯?



## 그 외의 리스트들

이런게 있더라 하는 정도로 알아두면 좋을 것 같아 소개한다. 

### 원형 리스트(circular list)

연결 리스트의 꼬리 노드가 다시 머리 노드를 가리키는 모양. 예를 들어 커서로 연결 리스트를 만드는 예에서, -1 부분에 머리 노드의 인덱스가 들어간 경우와 같다.

*코드는 본인이 임의로 작성한 것으로, 개념만 알기 위함

```python
head = 1
linked_list = [['D', 2], ['A', 4], ['E', 5], ['C', 0], ['B', 3], ['F', 1]]
```

이렇게 되면 머리 노드는 A이고, 꼬리 노드는 F 이지만 F가 다시 머리를 가리키게 된다.



### 이중 연결 리스트(doubly linked list)

연결 리스트는 뒤쪽 노드에 대한 정보를 가지고 있지만 앞쪽 노드에 대한 정보는 없기 때문에 앞쪽 노드를 찾기 어렵다는 단점이 있다. 이를 개선하여 만든 리스트 구조가 이중 연결 리스트이다.

각 노드에 뒤쪽 노드에 대한 포인터뿐 아니라 앞쪽 노드에 대한 포인터도 주어진다.

*코드는 본인이 임의로 작성한 것으로, 개념만 알기 위함

```python
head = 1
linked_list = [[3, 'D', 2], [None, 'A', 4], [0, 'E', 5], [4, 'C', 0], [1, 'B', 3], [2, 'F', -1]]
```

이렇게 작성해보면 각 노드 정보가 앞쪽 노드와 뒤쪽 노드의 인덱스에 대한 정보도 포함하게 된다.



### 원형 이중 연결 리스트

위 두 개념을 합친 것으로, 꼬리 노드가 머리 노드를 가리키고, 머리 노드가 꼬리 노드를 가리키도록 만들어주면 된다.

```python
head = 1
linked_list = [[3, 'D', 2], [5, 'A', 4], [0, 'E', 5], [4, 'C', 0], [1, 'B', 3], [2, 'F', 1]]
```





**참고: 커서로 연결 리스트 만들기 코드**

```python
# 커서로 연결 리스트 구현하기

from __future__ import annotations
from typing import Any, Type

Null = -1

class Node:
    """선형 리스트용 노드 클래스(배열 커서 버전)"""

    def __init__(self, data = Null, next = Null, dnext = Null):
        """초기화"""
        self.data  = data   # 데이터
        self.next  = next   # 리스트의 뒤쪽 포인터
        self.dnext = dnext  # 프리 리스트의 뒤쪽 포인터

class ArrayLinkedList:
    """선형 리스트 클래스(배열 커서 버전)"""

    def __init__(self, capacity: int):
        """초기화"""
        self.head = Null                   # 머리 노드
        self.current = Null                # 주목 노드
        self.max = Null                    # 사용 중인 맨끝 레코드
        self.deleted = Null                # 프리 리스트의 머리 노드
        self.capacity = capacity           # 리스트의 크기
        self.n = [Node()] * self.capacity  # 리스트 본체
        self.no = 0


    def __len__(self) -> int:
        """선형 리스트의 노드 수를 반환"""
        return self.no

    def get_insert_index(self):
        """다음에 삽입할 레코드의 첨자를 구합니다"""
        if self.deleted == Null:  # 삭제 레코드는 존재하지 않습니다
            if self.max+1 < self.capacity:
                self.max += 1
                return self.max   # 새 레코드를 사용
            else:
                return Null       # 크기 초과
        else:
            rec = self.deleted                # 프리 리스트에서
            self.deleted = self.n[rec].dnext  # 맨 앞 rec를 꺼내기
            return rec

    def delete_index(self, idx: int) -> None:
        """레코드 idx를 프리 리스트에 등록"""
        if self.deleted == Null:      # 삭제 레코드는 존재하지 않습니다
            self.deleted = idx        # idx를 프리 리스트의
            self.n[idx].dnext = Null  # 맨 앞에 등록
        else:
            rec = self.deleted        # idx를 프리 리스트의
            self.deleted = idx        # 맨 앞에 삽입
            self.n[idx].dnext = rec

    def search(self, data: Any) -> int:
        """data와 값이 같은 노드를 검색"""
        cnt = 0
        ptr = self.head             # 현재 스캔 중인 노드
        while ptr != Null:
            if self.n[ptr].data == data:
                self.current = ptr
                return cnt          # 검색 성공
            cnt += 1
            ptr = self.n[ptr].next  # 뒤쪽 노드에 주목
        return Null                 # 검색 실패

    def __contains__(self, data: Any) -> bool:
        """선형 리스트에 data가 포함되어 있는지 확인"""
        return self.search(data) >= 0

    def add_first(self, data: Any):
        """머리 노드에 삽입"""
        ptr = self.head                     # 삽입하기 전의 머리 노드
        rec = self.get_insert_index()
        if rec != Null:
            self.head = self.current = rec  # rec번째 레코드에 삽입
            self.n[self.head] = Node(data, ptr)
            self.no += 1

    def add_last(self, data: Any) -> None:
        """꼬리 노드에 삽입"""
        if self.head == Null:     # 리스트가 비어 있으면
            self.add_first(data)  # 맨 앞에 노드 삽입
        else:
            ptr = self.head
            while self.n[ptr].next != Null:
                ptr = self.n[ptr].next
            rec = self.get_insert_index()

            if rec != Null:       # rec번째 레코드에 삽입
                self.n[ptr].next = self.current = rec
                self.n[rec] = Node(data)
                self.no += 1

    def remove_first(self) -> None:
        """머리 노드를 삭제"""
        if self.head != Null:  # 리스트가 비어 있으면
            ptr = self.n[self.head].next
            self.delete_index(self.head)
            self.head = self.current = ptr
            self.no -= 1

    def remove_last(self) -> None:
        """꼬리 노드를 삭제"""
        if self.head != Null:
            if self.n[self.head].next == Null:  # 노드가 1개 뿐이면
                self.remove_first()             # 머리 노드를 삭제
            else:
                ptr = self.head                 # 스캔 중인 노드
                pre = self.head                 # 스캔 중인 노드의 앞쪽 노드

                while self.n[ptr].next != Null:
                    pre = ptr
                    ptr = self.n[ptr].next
                self.n[pre].next = Null  # pre는 삭제한 뒤의 꼬리 노드
                self.delete_index(ptr)
                self.current = pre
                self.no -= 1

    def remove(self, p: int) -> None:
        """레코드 p를 삭제"""
        if self.head != Null:
            if p == self.head:       # p가 머리 노드면
                self.remove_first()  # 머리 노드를 삭제
            else:
                ptr = self.head

                while self.n[ptr].next != p:
                    ptr = self.n[ptr].next
                    if ptr == Null:
                        return  # p는 리스트에 존재하지 않음
                #self.n[ptr].next = Null
                self.delete_index(p)
                self.n[ptr].next = self.n[p].next
                self.current = ptr
                self.no -= 1

    def remove_current_node(self) -> None:
        """주목 노드를 삭제"""
        self.remove(self.current)

    def clear(self) -> None:
        """모든 노드를 삭제"""
        while self.head != Null:  # 리스트 전체가 빌 때까지
            self.remove_first()   # 머리 노드를 삭제
        self.current = Null

    def next(self) -> bool:
        """주목 노드를 한 칸 뒤로 진행"""
        if self.current == Null or self.n[self.current].next == Null:
            return False  # 진행할 수 없음
        self.current = self.n[self.current].next
        return True


    def print_current_node(self) -> None:
        """주목 노드를 출력"""
        if self.current == Null:
            print('주목 노드가 없습니다.')
        else:
            print(self.n[self.current].data)

    def print(self) -> None:
        """모든 노드를 출력"""
        ptr = self.head

        while ptr != Null:
            print(self.n[ptr].data)
            ptr = self.n[ptr].next

    def dump(self) -> None:
        """배열을 덤프"""
        for i in self.n:
            print(f'[{i}]  {i.data} {i.next} {i.dnext}')

    def __iter__(self) -> ArrayLinkedListIterator:
        """이터레이터를 반환"""
        return ArrayLinkedListIterator(self.n, self.head)

class ArrayLinkedListIterator:
    """클래스 ArrayLinkedList의 이터레이터용 클래스"""

    def __init__(self, n: int, head: int):
        self.n = n
        self.current = head

    def __iter__(self) -> ArrayLinkedListIterator:
        return self

    def __next__(self) -> Any:
        if self.current == Null:
            raise StopIteration
        else:
            data = self.n[self.current].data
            self.current = self.n[self.current].next
            return data
```



