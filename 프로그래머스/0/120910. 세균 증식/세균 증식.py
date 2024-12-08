def solution(n, t):
    answer = n*2
    for i in range(t-1) :
        answer *= 2
    return answer

# 1  2  3  4  5  6  7  8  9  10
# 2  4  8  16  32  