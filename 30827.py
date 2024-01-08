import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

meeting = []
for _ in range(N) :
    meeting.append(tuple(map(int,input().rstrip().split())))

sorted_meeting = sorted(meeting, key=lambda x: (x[0], x[1]))

print(sorted_meeting)