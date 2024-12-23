def solution(s):
    answer = ''
    asci_list = []
    for i in range(len(s)) :
        asci_list.append(ord(s[i]))
    asci_list.sort(reverse=True)
    for i in range(len(asci_list)) :
        answer += chr(asci_list[i])
    return answer