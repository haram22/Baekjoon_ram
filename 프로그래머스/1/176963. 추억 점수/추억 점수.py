def solution(name, yearning, photo):
    answer = []
    for i in range(len(photo)) :
        ans = []
        for j in range(len(photo[i])) :
            for k in range(len(name)) :
                if photo[i][j] == name[k] :
                    ans.append(yearning[k])
        answer.append(sum(ans))
    return answer