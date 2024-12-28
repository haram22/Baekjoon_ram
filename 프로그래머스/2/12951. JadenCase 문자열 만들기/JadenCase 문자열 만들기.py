def solution(s):
    answer = ''
    # answer = s.capitalize()
    # 리스트로 바꾸기
    # 각 리스트에 반복문으로 capitalize 적용하기

    s_list = list(s.split(" "))
    final = []
    for i in range(len(s_list)) :
        final.append(s_list[i].capitalize())
        print(final)
        
    answer = ' '.join(final)
    return answer