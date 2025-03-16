def solution(strings, n):
    answer = []
    strings.sort(key=lambda x: (x[n], x))
    for i in range(len(strings)) :
        answer.append(strings[i])
    return answer