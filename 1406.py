import sys
from collections import deque

input = sys.stdin.readline

s = input().strip()
front = deque(s)
back = deque()

m = int(input())
for _ in range(m):
    command = input().strip()
    if command[0] == "L":
        if front:
            back.append(front.pop())
    if command[0] == "D":
        if back:
            front.append(back.pop())
    if command[0] == "B":
        if front:
            front.pop()
    if command[0] == "P":
        front.append(command[2])

print("".join(front), end="")
while back:
    print(back.pop(), end="")
