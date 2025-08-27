def solution(numbers):
    answer_list = []
    answer = []
    for i in range(len(numbers)) :
        for j in range(i) :
            answer_list.append(numbers[i] + numbers[j])
    answer = list(set(answer_list))
    answer.sort()
    return list(answer)