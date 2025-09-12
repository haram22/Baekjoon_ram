def solution(clothes):
    all_clothes = {}
    answer = 1
    for i in range(len(clothes)) :
        all_clothes[clothes[i][1]] = all_clothes.get(clothes[i][1], 0) +1
    for v in all_clothes.values() :
        answer *= (v+1)
    return answer-1