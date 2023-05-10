T = int(input())
for i in range(T) :
    N, K = map(int,input().split())
    time = [-1] + list(map(int, input().split()))

    worst_time = [-1]
    for i in range(1,len(time)) :
        worst_time.append(time[i])

    rules = list()
    for j in range(K) :
        X, Y = map(int, input().split())
        rules.append([X,Y])
    rules.sort()
    for j in range(K) :
        worst_time[rules[j][1]] = max(worst_time[rules[j][1]], worst_time[rules[j][0]] + time[rules[j][1]])
    
    print(worst_time)
    W = int(input())
    print(worst_time[W])
