def solution(brown, yellow):
    answer = []
    mok = []
    pair = []
    
   # 전체 곱의 경우의 수 구하기
    for i in range(1, yellow+1) :
        if yellow % i == 0 :
            mok.append(i)
    # if int(len(mok)/2) + 1 > 0 :  
    #     for i in range(int(len(mok)/2)):
    #         pair.append([mok[i], yellow // mok[i]])
            
    for i in range(len(mok)):
        w = mok[i]
        h = yellow // w
        if w <= h:  # 항상 가로 ≥ 세로가 되게 만들기
            pair.append([h, w])  # 세로가 먼저
            
            
    # 2. 첫번째 경우부터 검사해서 brown의 합을 구하고, 입력된 값과 일치하는 것 찾기
    for i in range(len(pair)) :
        m = pair[i][0]*2
        n = pair[i][1]*2
        total = 0
        count = 0
        while(total <= brown) :
            count += 1
            total += (m + n + 4)
            if total == brown :
                answer.append(pair[i][0]+(count*2))
                answer.append(pair[i][1]+(count*2))
                break
            m = m * 2
            n = n * 2
        if len(answer) > 0 :
            break
            
    if len(answer) >= 2 and answer[0] < answer[1]:
            temp = answer[0]
            answer[0] = answer[1]
            answer[1] = temp
    return answer