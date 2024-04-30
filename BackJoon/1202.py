import sys
import heapq
input = sys.stdin.readline

n, k = map(int,input().rstrip().split())
gems = sorted([list(map(int,input().rstrip().split())) for _ in range(n)])
bags = sorted([int(input().rstrip()) for _ in range(k)])

h = []
ans = 0
for bag in bags :
    while gems and gems[0][0] <= bag :
        heapq.heappush(h, -gems[0][1])
        heapq.heappop(gems)
    if h :
        ans -= heapq.heappop(h)
print(ans)