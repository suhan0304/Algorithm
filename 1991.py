import sys

input = sys.stdin.readline

class node() :
    def __init__(self, key) :
        self.key = key
        self.p = None
        self.l = None
        self.r = None
        

class Tree() :
    def __init__(self, root=None) :
        self.root = root
        
    def root(self) :
        return self.rot
    
    def insert(self, key, l, r) :
        v = node(key)
        if self.root == None :
            self.root = v
        left = node(l)
        right = node(r)
        v.l = left
        v.r = right
        
n = int(input())
tree = Tree()
for _ in range(n) :
    a, b, c = map(lambda x: None if x == '.' else x, input().rstrip().split())
    tree.insert(a, b, c)
