import sys
input = sys.stdin.readline

def find(n) : 
    if parent[n] == n :
        return n
    parent[n] = find(parent[n])
    return parent[n]

def union(a, b) :
    a, b = find(a), find(b)

    if a == b : 
        return
    parent[b] = a
    
g, p = int(input()),int(input())

parent = list(range(g+1))

ans = 0
for i in range(p) :
    g = int(input())
    tmp = find(g)
    if tmp == 0 :
        break
    union(tmp-1, tmp)
    ans += 1

print(ans)