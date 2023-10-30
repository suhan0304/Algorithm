def solution(MIN, MAX) :
    answer = MAX - MIN + 1
    check = [False] * answer
    i = 2
    while i*i <= MAX :
        square_n = i*i
        remain = 0 if MIN*square_n == 0 else 1
        j = MIN//square_n + remain
        while square_n * j <= MAX :
            if not check[square_n*j-MIN] :
                check[square_n*j-MIN]=True
                answer -= 1
            j += 1
        i += 1
    print(answer)


n_min, n_max = map(int, input().split())
solution(n_min, n_max)
