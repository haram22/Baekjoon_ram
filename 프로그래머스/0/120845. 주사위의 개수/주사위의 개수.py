def solution(box, n):
    answer = 0
    x, y, z = box
    answer = (x//n) * (y//n) * (z//n)
    return answer