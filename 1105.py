import sys

input = sys.stdin.readline

l, r = map(int, input().split())

sl = str(l)
sr = str(r)

if (
    sl.count("8") == 0
    or sr.count("8") == 0
    or len(sl) != len(sr)
    or len(sl) == len(sr)
    and sl[0] != sr[0]
):
    print(0)
    exit()

ans = 0
for i in range(len(sl)):
    if sl[i] == sr[i]:
        ans = i
        continue
    else:
        break
print(sl[: ans + 1].count("8"))
