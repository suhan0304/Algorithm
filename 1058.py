import sys

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n)]

for i in range(n):
    s = input()[:-1]
    for j in range(len(s)):
        if s[j] == "Y":
            graph[i].append(j)
            graph[j].append(i)


print(graph)
