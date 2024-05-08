import sys
from itertools import combinations
input = sys.stdin.readline

n, s = map(int,input().rstrip().split())
a = list(map(int, input().rstrip().split()))

a1 = a[:n//2]
a2 = a[n//2:]
a1_sum = []
a2_sum = []

for i in range(len(a1) + 1) :
    for c in combinations(a1,i) :
        a1_sum.append(sum(c))
a1_sum.sort()

for i in range(len(a2) + 1) :
    for c in combinations(a2,i) :
        a2_sum.append(sum(c))
a2_sum.sort(reverse=True)

ans = 0

a1_pointer = 0
a2_pointer = 0
a1_len = len(a1_sum)
a2_len = len(a2_sum)

while a1_pointer < a1_len and a2_pointer < a2_len :
    tmp_s = a1_sum[a1_pointer] + a2_sum[a2_pointer]

    if s == tmp_s :
        a1_p_temp = a1_pointer
        a2_p_temp  = a2_pointer
        while a1_p_temp < a1_len and a1_sum[a1_p_temp] == a1_sum[a1_pointer] :
            a1_p_temp += 1
        while a2_p_temp < a2_len and a2_sum[a2_p_temp] == a2_sum[a2_pointer] :
            a2_p_temp += 1
        ans += (a1_p_temp - a1_pointer) * (a2_p_temp - a2_pointer)

        a1_pointer, a2_pointer = a1_p_temp, a2_p_temp

    elif s < tmp_s :
        a2_pointer += 1
    else :
        a1_pointer += 1

if s == 0 :
    print(ans-1)
else :
    print(ans)
 