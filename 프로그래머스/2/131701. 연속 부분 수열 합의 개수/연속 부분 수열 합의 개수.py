def solution(elements):
    fin_list = []
    fin_list += elements
    fin_list.append(sum(elements))
    
    for i in range(2, len(elements)) :
        fin_list += find_case(i, elements)
    return len(set(fin_list))

def find_case(n, elements) :
    cnt = len(elements)
    temp_e = elements.copy()
    sum_list = []
    for i in range(n-1) :
        temp_e.append(elements[i])
    for i in range(len(temp_e)-n+1):
        temp = temp_e[i:i+(n%cnt)]
        sum_list.append(sum(temp))
    return sum_list