def solution(numbers, direction):
    answer = []
    if direction == 'left' :
        for i in range(1, len(numbers)) :
            answer.append(numbers[i])
        answer.append(numbers[0])
        
    else :
        answer.append(numbers[-1])
        for i in range(len(numbers)-1) :
            answer.append(numbers[i])
        # answer.append(numbers[:-1])
    return answer