import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
pos = list(map(int, input().split()))
dq = deque(range(1, n + 1))

cnt = 0
for i in pos:
    while True:
        # 맨앞에 원하는 위치의 수가 있으면 popleft
        if dq[0] == i:
            dq.popleft()
            break
        else:
            # 앞쪽에 더 가깝다면 2번 방법 사용
            if dq.index(i) < len(dq) / 2:
                while dq[0] != i:
                    # 첫번째 자리에 올 때까지 2번 방법 사용
                    dq.append(dq.popleft())
                    cnt += 1
            # 뒤쪽에 더 가깝다면 3번 방법 사용
            else:
                while dq[0] != i:
                    # 첫번째 자리에 올 때까지 3번 방법 사용
                    dq.appendleft(dq.pop())
                    cnt += 1
print(cnt)
