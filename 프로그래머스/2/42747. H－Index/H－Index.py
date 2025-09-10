def solution(citations):
    answer = 0
    citations.sort()
    max_idx = max(citations)
    for i in range(max_idx) :
        cnt = 0
        cnt_ = 0
        for j in range(len(citations)) :
            if citations[j] >= i :
                cnt += 1
            else :
                cnt_ += 1
        if cnt >= i :
            answer = i
    return answer