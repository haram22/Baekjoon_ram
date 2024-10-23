def solution(arr, k):
    answer = []
    # 홀수
    if k%2 != 0 :
        for i in range(len(arr)):
            answer.append(int(arr[i])*k)
    else :
        for i in range(len(arr)):
            answer.append(int(arr[i])+k)
    return answer