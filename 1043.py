import sys
input = sys.stdin.readline

n,m = map(int, input().rstrip().split())

member = set([i+1 for i in range(n)])
truth = set()
liar = set()

line = list(map(int, input().rstrip().split()))
for i in range(1, line[0]) :
    truth.add(line[i])
member = member - truth

for i in range(m) :
    line = list(map(int, input().rstrip().split()))
    for i in range(1, line[0]) :
        if line[i] in truth :
            