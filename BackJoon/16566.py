import sys
input = sys.stdin.readline

n, m, k = map(int, input().rstrip().split())

card = list(map(int,input().rstrip().split()))
card.sort()

parent = [0 for _ in range(n+1)]
