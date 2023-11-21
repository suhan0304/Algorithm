import sys

input = sys.stdin.readline

def dfs(n, cnt) :
    if cnt == 6 :
        print(*n)
        return
    
    for i in range(len(s)) :
        if not visited[i] and n[-1] < s[i]:
            visited[i] = True
            dfs(n + [s[i]], cnt + 1)
            visited[i] = False

while True :
    a = list(map(int,input().split()))
    if len(a) == 1 :
        break
    
    s = a[1:]

    visited = [False] * len(s) 
    for i in range(len(s)-6 + 1) :
        visited[i] = True
        dfs([s[i]], 1)
        visited[i] = False
    print()
    
