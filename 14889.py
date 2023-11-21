import sys

input = sys.stdin.readline

def sumS(t) :
    sum = 0
    for i in range(len(t)) :
        for j in range(i+1, len(t)) :
                sum += s[t[i]][t[j]] + s[t[j]][t[i]]
    return sum

team = []
ans = 10 ** 8
def dfs(m, cnt) :
    if cnt == n//2 :
        global ans
        team1 = [i for i, key in enumerate(visited) if key]
        team2 = [i for i, key in enumerate(visited) if not key]
        temp = abs(sumS(team1) - sumS(team2))
        if ans > temp :
            #print(team1, team2, sumS(team1), sumS(team2))
            ans = temp
            if ans == 0 :
                print(0)
                exit()
        return
    
    for i in range(n) :
        if not visited[i] and m[-1] < i:
            visited[i] = True
            dfs(m + [i], cnt + 1)
            visited[i] = False

n = int(input())

s = []
for _ in range(n) :
    s.append(list(map(int,input().split())))

visited = [False] * n
for i in range(n) :
    visited[i] = True
    dfs([i], 1)
    visited[i] = False
print(ans)