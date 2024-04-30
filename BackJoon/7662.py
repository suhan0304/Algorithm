import sys
from collections import deque

input = sys.stdin.readline

t = int(input().rstrip())
for i in range(t) :
    q = deque()
    k = int(input().rstrip())
    for j in range(k) :
        oper = list(input().split())
        if oper[0] == 'I' :
            if len(q) > 0 :
                
            elif len(q) == 0 :
                q.append(int(oper[1]))
        elif oper[0] == 'D' :
            print('D')