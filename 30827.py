import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

meetings = []
for _ in range(N) :
    meetings.append(tuple(map(int,input().rstrip().split())))
sorted_meetings = sorted(meetings, key=lambda x: (x[1], x[0]))
#print(sorted_meetings)

meeting_room = [0 for _ in range(K)]
answer = 0

for meeting in sorted_meetings :
    start_time, end_time = meeting

    meeting_room = sorted(meeting_room, reverse=True)
    for room in range(K) :
        if start_time > meeting_room[room] :
            meeting_room[room] = end_time
            answer += 1
            break

print(answer)