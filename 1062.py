import sys

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

arr = list(input().rstrip() for _ in range(N))
print(arr)
def check(visited) :
    cnt = 0
    for s in arr :
        for c in s :
            if visited[char(c)] == 0 :
                break
        else :
            cnt += 1
    return cnt

max_cnt = 0
def bk_tr(depth, visited) :
    if depth == K :
        global max_cnt
        max_cnt = max(check(visited))
        return
    
    for s in arr :
        for c in s :
            print(c)
            if visited[char(c)] == 0 :
                visited[char(c)] = 1
                bk_tr(depth+1, visited)
                visited[char(c)] = 0
    return
                
def char(c) :
    return ord(c) - ord('a')

visited = [0] * 26
if K < 5 :
    print(0)
    exit(0)
else :
    visited[char('a')] = 1
    visited[char('n')] = 1
    visited[char('t')] = 1
    visited[char('i')] = 1
    visited[char('c')] = 1
    bk_tr(5, visited)
    print(max_cnt)