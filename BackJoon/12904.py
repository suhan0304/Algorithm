import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()

# 반대로 올라가야됨 
def make_string(st) :
    if st == S :
        print(1)
        return

    if len(st) <= len(S) :
        print(0)
        return

    if st[-1] == 'A' :
        make_string(st[:-1])
    elif st[-1] == 'B' :
        make_string(st[:-1][::-1])
    
make_string(T)