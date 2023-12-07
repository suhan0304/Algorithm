import sys

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

arr = [int(input().rstrip()) for _ in range(N)]

print(arr)