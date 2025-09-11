def solution(participant, completion):
    counts = {}
    for c in completion :
        counts[c] = counts.get(c, 0) +1
    for p in participant :
        if counts.get(p, 0) == 0 :
            return p
        else :
            counts[p] -= 1