import sys
input = sys.stdin.readline

N, M = map(int,input().rstrip().split())

def proc(K):
    if K==0:
        return 0
    n=int((K.bit_length()-1)//1)
    return int((2**(n-1))*n) + proc(K-(2**n)) + K-((2**n)-1)

print(proc(M)-proc(N-1))