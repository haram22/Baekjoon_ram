def solution(board, k):
    answer = 0
    value_sum = 0
    # k보다 합이 작은 것들 찾기
    # 찾으면 정답 변수에 더해주기
    for i in range(len(board)) :
        value_sum = 0
        for j in range(len(board[i])) :
            if (i+j <= k) :
                answer += board[i][j]
    return answer