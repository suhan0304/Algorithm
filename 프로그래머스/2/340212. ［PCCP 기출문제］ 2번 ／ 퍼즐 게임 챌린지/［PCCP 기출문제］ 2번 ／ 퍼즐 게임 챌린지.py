def puzzle_time(diffs, times, limit, level) :
    clear_time = 0
    for i in range(len(diffs)) :
        if diffs[i] <= level : clear_time += times[i]
        if diffs[i] > level : clear_time += (diffs[i]-level) * (times[i-1] + times[i]) + times[i]
        if clear_time > limit : return False
    return True
 
def solution(diffs, times, limit):
    left, right = 1, max(diffs)
    
    while left <= right :
        mid = (left+right) // 2

        if puzzle_time(diffs, times, limit, mid) : right = mid - 1
        else : left = mid + 1

    if puzzle_time(diffs, times, limit, mid) : return mid
    if puzzle_time(diffs, times, limit, mid+1) : return mid+1
    return mid-1
