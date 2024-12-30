final_zero = 0
def solution(s):
    answer = []
    zero_count = 0
    final = recursions(s, zero_count)
    answer.append(recursions.counter)
    answer.append(final_zero)
    return answer

def recursions(s, zero_count) :
    newS = ''
    global final_zero
    for i in range(len(s)) :
        if s[i] != '0' :
            newS += s[i]
        else :
            zero_count += 1
    final_zero = zero_count
    bin_result = bin(len(newS)).replace('0b','')
    if bin_result != '1' :
        recursions(bin_result, zero_count)
        recursions.counter += 1
    return zero_count

recursions.counter = 1
