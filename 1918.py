import sys
from collections import deque
from collections import Counter

input = sys.stdin.readline

s = input().strip()

q = deque()
oper = deque()

cnt = 0
"""
for c in s:
    if c in ['+','-','*','/','(',')'] :
        if c == '(' : 
            cnt += 1
        elif c== ')' :
            cnt -= 1
            
        if c in ['*','/'] and oper and oper[-1] in ['+','-'] :
            temp = q.pop()
            q.append('(')
            q.append(temp)
            oper.append('(')
            cnt += 1
        if c in ['+','-'] and oper and oper[-1] in ['*','/'] :
            q.append(')')
            oper.append(')')
            cnt -= 1
            
        oper.append(c)
    q.append(c)

for i in range(cnt) :
    oper.append(')')
    q.append(')')
    
if oper[0] != '(' :
    oper.appendleft('(')
    oper.append(')')
    q.appendleft('(')
    q.append(')')
        
print(q)
"""

