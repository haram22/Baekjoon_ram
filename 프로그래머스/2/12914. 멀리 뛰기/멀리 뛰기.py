def solution(n):
    return count_combinations(n) % 1234567

def count_combinations(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for num in [1, 2]:
            if i - num >= 0:
                dp[i] += dp[i - num]
    return dp[n]
