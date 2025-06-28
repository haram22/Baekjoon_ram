from collections import Counter

def solution(k, tangerine):
    answer = 0
    counter = Counter(tangerine)
    counts = sorted(counter.values(), reverse=True)
    for i in range(len(counts)) :
        k -= counts[i]
        answer += 1
        if k <= 0 :
            break
    return answer