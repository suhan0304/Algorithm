import math

T = int(input())
for i in range(T) :
    result = 0
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    for i in range(n) :
        cx, cy, cr = map(int, input().split())
        d1 = math.sqrt((x1-cx)**2 + (y1-cy)**2)
        d2 = math.sqrt((x2-cx)**2 + (y2-cy)**2)
        if min(d1, d2) < cr < max(d1,d2) : result += 1
    print(result)
