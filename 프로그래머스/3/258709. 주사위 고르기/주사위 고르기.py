from itertools import combinations, product

def solution(dice):
    dp = {}
    L = len(dice)

    for A_index_combi in combinations(range(L), L//2) :
        B_index_combi = [i for i in range(L) if i not in A_index_combi]

        A, B = [], []
        for order_dice in product(range(6), repeat=L//2) :
            A.append(sum(dice[i][j] for i, j in zip(A_index_combi, order_dice)))
            B.append(sum(dice[i][j] for i, j in zip(B_index_combi, order_dice)))

        B.sort()

        wins = 0
        for num in A :
            left, right = 0, len(B) - 1
            while left <= right :
                mid = (left + right) // 2
                if num <= B[mid] :
                    right = mid - 1
                else :
                    left = mid + 1
            wins += left

        dp[wins] = list(A_index_combi)

    max_key = max(dp.keys())

    return [x+1 for x in dp[max_key]]
