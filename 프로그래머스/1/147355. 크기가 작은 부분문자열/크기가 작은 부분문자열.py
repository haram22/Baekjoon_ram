def solution(t, p):
    count = 0
    for i in range(0, len(t)-len(p)+1) :
        s = ''
        for j in range(len(p)) :
            s += t[i+j]
        if int(p) >= int(s) :
            count += 1
    return count