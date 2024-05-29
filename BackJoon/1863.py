import sys
input = sys.stdin.readline

n = int(input())
building = [list(map(int, input().split())) for _ in range(n)]
building.sort()

ans = 0
q = []
for i in range(n) :
    while q and q[-1] >= building[i][1] :
        if q[-1] != building[i][1] :
            ans += 1
        q.pop()

    if building[i][1] != 0 :
        q.append(building[i][1])
while q :
    q.pop()
    ans += 1
print(ans)