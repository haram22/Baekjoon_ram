def solution(want, number, discount):
    answer = 0
    comp = []
    
    for i in range(len(discount) - 9) :
        comp = discount[i:i+10]
        save_count = []
        for j in range(len(want)) :
            save_count.append(comp.count(want[j]))
        if save_count == number :
            answer += 1
    return answer