def solution(arr, queries):
    answer = []
    range_list = []
    
    for i in range(len(queries)) :
        for j in range(queries[i][0], queries[i][1]+1) :
            if arr[j] > queries[i][2] :
                range_list.append(arr[j])
        if (len(range_list) == 0) :
            range_list.append(-1)
        answer.append(min(range_list))
        range_list = []
    return answer