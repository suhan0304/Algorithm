import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n = int(input())
inorder = list(map(int,input().rstrip().split()))
postorder = list(map(int,input().rstrip().split()))

position = [0] * (n+1)
for i in range(n) :
    position[inorder[i]] = i

def preorder(in_s, in_e, post_s, post_e) :
    if in_s > in_e or post_s > post_e :
        return
    
    root = postorder[post_e]

    left = position[root] - in_s
    right = in_e - position[root]

    print(root, end=' ')
    preorder(in_s, in_s+left-1, post_s, post_s+left-1) 
    preorder(in_e-right+1, in_e, post_e-right, post_e-1) 

preorder(0, n-1, 0, n-1)