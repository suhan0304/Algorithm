def solution(edges):
    answer = [0, 0, 0, 0]

    degrees = {}
    for start_node, end_node  in edges :
        if not degrees.get(start_node) :
            degrees[start_node] = [0, 0]
        if not degrees.get(end_node) :
            degrees[end_node] = [0, 0]
        
        degrees[start_node][0] += 1
        degrees[end_node][1] += 1

    for node, degree in degrees.items() :
        if degree[0] >= 2 and degree[1] == 0 :
            answer[0] = node
        
        elif degree[0] == 0 and degree[1] > 0 :
            answer[2] += 1
        elif degree[0] >= 2 and degree[1] >= 2 :
            answer[3] += 1

    answer[1] = (degrees[answer[0]][0] - answer[2] - answer[3])

    return answer