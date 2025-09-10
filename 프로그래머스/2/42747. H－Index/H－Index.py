def solution(citations):
    answer = 0
    max_idx = max(citations)
    for i in range(max_idx) :
        cnt = 0
        for j in range(len(citations)) :
            if citations[j] >= i :
                cnt += 1
        if cnt >= i :
            answer = i
    return answer
