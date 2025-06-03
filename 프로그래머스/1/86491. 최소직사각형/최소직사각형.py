def solution(sizes):
    answer = 0
    a = []
    b = []
    for i in range(len(sizes)) :
        temp = 0
        if sizes[i][0] < sizes[i][1] :
            temp = sizes[i][0]
            sizes[i][0] = sizes[i][1]
            sizes[i][1] = temp
    for i in range(len(sizes)) :
        a.append(sizes[i][0])
        b.append(sizes[i][1])
    a.sort()
    b.sort()
    return a[-1] * b[-1]