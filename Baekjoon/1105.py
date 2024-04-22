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
    # 1200009 1900009 이렇게 있다면
    # 1이 같다면 12 19를 빼면 뒷 부분을 8이 0으로 나오게 할 수 있다.
    # 2~9사이에는 8이 있을 수 있기 때문에 같은 자리수 다음 자리수까지는 확인해야함
    if sl[i] == sr[i]:
        ans = i
        continue
    else:
        break
print(sl[: ans + 1].count("8"))
