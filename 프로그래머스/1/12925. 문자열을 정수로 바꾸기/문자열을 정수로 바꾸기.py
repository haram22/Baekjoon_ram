def solution(s):
    answer = 0
    list_s = list(s)
    if list_s[0] == "-" :
        list_s.remove(list_s[0])
        s.replace("-", "")
    return int(s)