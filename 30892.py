import sys
from collections import deque
input = sys.stdin.readline

N, K, T = map(int,input().rstrip().split())

arr = sorted(list(map(int,input().rstrip().split())))
