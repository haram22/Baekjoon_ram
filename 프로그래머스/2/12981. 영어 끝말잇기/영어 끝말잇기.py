def solution(n, words):
    answer = []
    idx = 0
    turn = 0
    p_id = 0
    idx = min(duplicate_word(n, words), not_correct(n, words))
    if idx != 101 :
        p_id, turn = find_num_turn(n, idx)
        answer = [p_id, turn]
    else :
        answer = [0,0]
    return answer

def duplicate_word(n, words) :
    said = []
    idx = 101
    for i in range(len(words)) :
        if words[i] in said :
                print(words[i])
                idx = i
                break
        said.append(words[i])
    return idx
    
def not_correct(n, words) :
    idx = 101
    for i in range(len(words)-1) :
        if words[i][-1] != words[i+1][0] :
            print(words[i+1])
            idx = i+1
            break
    return idx

def find_num_turn(n, idx) :
    p_id = (idx % n)+1
    turn = ((idx) // n)+1
    return p_id, turn
    
    
            
    