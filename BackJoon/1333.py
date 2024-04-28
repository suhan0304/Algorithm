import sys

input = sys.stdin.readline

N, L, D = map(int,input().rstrip().split())

time = 0
for i in range(N) :
    time += L
    for j in range(time, time+5) :
        if j%D == 0 :
            print(j)
            exit()
    time += 5
while time%D != 0 :
    time += 1
print(time)
