def solution(array, commands):
    answer = []
    for t in range(len(commands)) :
        i = commands[t][0]
        j = commands[t][1]
        k = commands[t][2]
        sliceArray = array[i-1:j]
        sliceArray.sort()
        answer.append(sliceArray[k-1])
    return answer