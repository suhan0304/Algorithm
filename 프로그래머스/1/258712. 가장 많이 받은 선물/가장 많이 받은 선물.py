def solution(friends, gifts):
    
    friends_dict = {name:index  for index,name in enumerate(friends)}

    present = [[0] * len(friends) for _ in range(len(friends))]
    present_point = [0] * len(friends)

    for gift in gifts :
        give, get = gift.split()

        present[friends_dict[give]][friends_dict[get]] += 1
        present_point[friends_dict[give]] += 1
        present_point[friends_dict[get]] -= 1

    #test_print
    """ 
    for p in present :
        print(p) 
    print(present_point)
    """
    answer = 0

    for i in range(len(friends)) :
        temp_ans = 0
        for j in range(len(friends)) :
            if i == j :
                continue

            give_num = present[i][j]
            get_num = present[j][i]
            
            if give_num > get_num :
                temp_ans += 1
            elif give_num == get_num and present_point[i] > present_point[j] :
                temp_ans += 1
        if temp_ans > answer :
            answer = temp_ans

    return answer