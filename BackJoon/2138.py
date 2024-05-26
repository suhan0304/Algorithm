import sys
input = sys.stdin.readline

n = int(input())
bulb = list(map(int, input()))
target = list(map(int, input()))

def proc(a, b) :
    a_c = a[:]
    p = 0