import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

meetings = []
for _ in range(N) :
    meetings.append(tuple(map(int,input().rstrip().split())))
sorted_meetings = sorted(meetings, key=lambda x: (x[1]))
print(sorted_meetings)

meeting_room = {i : 0 for i in range(1, K+1)}
answer = 0

for meeting in sorted_meetings :
    start_time, end_time = meeting

    for room in range(1, K+1) :
        if start_time >= meeting_room[room] :
            

