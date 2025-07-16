def solution(n, arr1, arr2):
    result = binary_num(arr1, arr2, n)
    answer = []
    
    for i in range(len(result)) :
        ans = ''
        for j in range(len(result[i])) :
            if result[i][j] == '1' :
                ans += "#"
            else :
                ans += " "
        answer.append(ans)
    print(answer)
    return answer
    
def binary_num(arr1, arr2, n) :
    result = []
    for a, b in zip(arr1, arr2) :
        binary = bin(a | b)[2:].zfill(n)
        result.append(binary)
    return result