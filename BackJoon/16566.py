import sys
input = sys.stdin.readline

n, m, k = map(int, input().rstrip().split())

card = list(map(int,input().rstrip().split()))
card.sort()

parent = [0 for _ in range(n+1)]

def set_parent() :
    for i in range(len(card)-1) :
            parent[card[i]] = card[i+1]
    
    print(parent)
    return parent

set_parent()


