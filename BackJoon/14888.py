import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

# + - * /
oper = list(map(int, input().split()))
max_ans = -10**9
min_ans = 10**9

def back_tracking(depth, used, s) :
    if depth == sum(oper) :
        global max_ans
        global min_ans
        max_ans = max(max_ans, s)
        min_ans = min(min_ans, s)
        return

    for i in range(4) :
        if used[i]+1 > oper[i] :
            continue

        used[i] += 1
        if i == 0 :
            back_tracking(depth+1, used, s + a[depth+1])
        if i == 1 :
            back_tracking(depth+1, used,  s - a[depth+1])
        if i == 2 :
            back_tracking(depth+1, used, s * a[depth+1])
        if i == 3 :
            if s < 0 :
                back_tracking(depth+1, used, -(-s // a[depth+1]))
            else :
                back_tracking(depth+1, used, s // a[depth+1])
        used[i] -= 1

used = [0,0,0,0]
back_tracking(0, used, a[0])

print(max_ans)
print(min_ans)