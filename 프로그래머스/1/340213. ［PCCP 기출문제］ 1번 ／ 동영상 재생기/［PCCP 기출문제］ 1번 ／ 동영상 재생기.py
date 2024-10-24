def cal_seconds(times) :
    minutes, seconds = map(int, times.split(':'))
    total_seconds = minutes * 60 + seconds
    return total_seconds

def solution(video_len, pos, op_start, op_end, commands):
    total_seconds = cal_seconds(video_len)
    pos_seconds = cal_seconds(pos)
    op_start_seconds = cal_seconds(op_start)
    op_end_seconds = cal_seconds(op_end)

    for command in commands :
        if op_start_seconds <= pos_seconds and pos_seconds <= op_end_seconds :
            pos_seconds = op_end_seconds
        if command == 'prev' :
            pos_seconds = pos_seconds - 10 if pos_seconds > 10 else 0
        elif command == 'next' :
            pos_seconds = pos_seconds + 10 if pos_seconds < total_seconds - 10 else total_seconds
    
    if op_start_seconds <= pos_seconds and pos_seconds <= op_end_seconds :
            pos_seconds = op_end_seconds

    answer = f"{pos_seconds // 60:02}:{pos_seconds % 60:02}"
    return answer