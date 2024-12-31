def solution(price, money, count):
    answer = -1
    pay = 0
    for i in range(1, count+1) :
        pay += (price * i)
    answer = pay - money
    if answer < 0 :
        answer = 0

    return answer