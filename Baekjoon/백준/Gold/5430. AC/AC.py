import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for i in range(T) :
    p = input().rstrip()
    n = int(input())
    x = deque(eval(input()))

    dir = 1

    for c in p :
        if c == "R" :
            dir = dir * -1
        elif c == "D" :
            if len(x) == 0 :
                print("error")
                break
            else :
                if dir == 1 :
                    x.popleft()
                elif dir == -1 :
                    x.pop()
    else :
        if dir == 1 :
            print("[" + ",".join(map(str, x)) + "]")
        elif dir == -1:
            x.reverse()
            print("[" + ",".join(map(str, x)) + "]")

