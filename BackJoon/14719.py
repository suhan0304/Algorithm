import sys
input = sys.stdin.readline

h, w = map(int, input().split())
blocks = list(map(int, input().spplit()))
arr = [[0 for _ in range(w)] for _ in range(h)]
 