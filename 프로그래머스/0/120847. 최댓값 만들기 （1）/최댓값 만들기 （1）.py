def solution(numbers):
    answer = 0
    max1 = max(numbers)
    numbers.remove(max1)
    max2 = max(numbers)
    return max1*max2