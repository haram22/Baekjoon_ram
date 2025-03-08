def solution(age):
    answer = ''
    str_age = str(age)
    for i in range(len(str_age)) :
        answer += chr(97 + int(str_age[i]))
    return answer