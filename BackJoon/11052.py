import sys

n = int(sys.stdin.readline())

card = list(map(int,input().split()))

ans = card
ans[0] = 100

print(card)
print(ans)
    