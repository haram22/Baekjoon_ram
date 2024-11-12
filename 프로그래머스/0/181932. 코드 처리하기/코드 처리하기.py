def solution(code) :
    answer = ''
    ret = []
    mode = 0
    for i in range(len(code)):
        if (mode == 0):
            if (code[i] != '1'):
                if (i % 2 == 0):
                    ret+= code[i]
            else :
                mode = 1   
        else :
            if (code[i] != '1'):
                if (i % 2 != 0):
                    ret += code[i]
            else :
                mode = 0
    print(ret)
    answer = ''.join(str(x) for x in ret)
    if (answer == ''):
        answer = "EMPTY"
        
    return answer