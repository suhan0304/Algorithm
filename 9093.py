import sys

input = sys.stdin.readline

n = int(input())
for _ in range(n):
    words = input().strip().split()
    for word in words:
        print(word[::-1], end=" ")
    print()
