import sys

input = sys.stdin.readline

class node() :
    def __init__(self, key) :
        self.key = key
        self.p = None
        self.l = None
        self.r = None
    
    def preorder_travel(self) :
        if self.l != None :
            self.l.preorder_travel()
        if self.r != None :
            self.r.preorder_travel()
        print(self.key, end='')
            
    def postorder_travel(self) :
        if self.l != None :
            self.l.preorder_travel()
        if self.r != None :
            self.r.preorder_travel()
        print(self.key, end='')
    
    def inorder_travel(self) :
        if self.l != None :
            self.l.preorder_travel()
        print(self.key, end='')
        if self.r != None :
            self.r.preorder_travel()
        

class Tree() :
    def __init__(self, root=None) :
        self.root = root
        
    def root(self) :
        return self.rot
    
    def insert(self, key, l, r) :
        if self.root == None :
            v = node(key)
            self.root = v
        else :
            v = self.find(key, self.root)
        left = node(l)
        right = node(r)
        v.l = left
        v.r = right
        
n = int(input())
tree = Tree()
for _ in range(n) :
    a, b, c = map(lambda x: None if x == '.' else x, input().rstrip().split())
    tree.insert(a, b, c)

tree.root.preorder_travel()