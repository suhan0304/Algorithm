import sys

input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()

def make_string(s) :
    if s == T :
        print(1)
        exit(0)
    if len(s) == len(T) :
        return
    
    make_string(s + 'A')
    make_string(s[::-1] + 'B')

make_string(S)
print(0)

