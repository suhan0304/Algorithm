import sys
input = sys.stdin.readline

n, a, b = map(int, input().split())

q = []
if a + b > n + 1 :
    print(-1)
elif a >= b :
    for i in range(1, a+1) :
        q.append(i)

        if i == 1 :
            for j in range(n-a-b+1) :
                q.append(1)
    for i in range(b-1, 0, -1) :
        q.append(i)
else :
    if a == 1 :
        for i in range(b, 0, -1) :
            q.append(i)
        
            if i == b :
                for j in range(n-a-b+1) :
                    q.append(1)
    else :
        for i in range(n-a-b+1) :
            q.append(1)
        for i in range(1, a) :
            q.append(i)
        for i in range(b, 0, -1) :
            q.append(i)
print(*q)