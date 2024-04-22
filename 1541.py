import sys
import re

input = sys.stdin.readline

s = input()[:-1]
num = list(map(int, re.split("[-+]", s)))
oper = [i for i in re.split("[0-9]", s) if i in ["+", "-"]]

i = 0
while i < len(oper):
    if oper[i] == "-":
        while i + 1 < len(oper) and oper[i + 1] == "+":
            oper[i + 1] = "-"
            i += 1
    i += 1

ans = num[0]
num = num[1:]

for i in range(len(num)):
    ans = ans + num[i] if oper[i] == "+" else ans - num[i]

print(ans)
