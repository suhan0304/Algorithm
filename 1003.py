result = [[1, 0], [0, 1], [1,1]]
for i in range(3, 41) :
    result.append([result[i-1][0]+result[i-2][0], result[i-1][1]+result[i-2][1]])
cnt = int(input())
for i in range(cnt) :
    n = int(input())
    print(result[n][0], result[n][1])
            
        
