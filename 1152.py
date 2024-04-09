import sys
input = sys.stdin.readline

a = input().rstrip()
print(a.count(' ') + 1 - a.startswith(' ') if len(a) > 0 else 0)
