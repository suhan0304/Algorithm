import sys

input = sys.stdin.readline

n, score, p = map(int, input().split())

if n == 0:
    print(1)
    exit()

rank = list(map(int, input().split()))

i = 0
while i < n and rank[i] > score:
    i += 1
my_rank = i + 1


if my_rank > p:
    print(-1)
else:
    same_score = list(filter(lambda x: rank[x] == score, range(len(rank))))
    if same_score and same_score[-1] + 1 >= p:
        print(-1)
    else:
        print(my_rank)
