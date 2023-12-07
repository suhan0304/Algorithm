import sys

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

arr = [list(input().rstrip().split() for _ in range(N))]

def solution(cnt) :
    if cnt == K :
        return
    
    for s in arr :
        for c in s :
            if visited[char(c)] == 0 :
                visited[char(c)] = 1
                solution(cnt+1)
                visited[char(c)] = 1
                
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
    solution(5, visited)
    