def solution(price):
    answer = 0
    if (price >= 100000 and price < 300000) :
        price -= price*0.05
    if (price >= 300000 and price < 500000) :
        price -= price*0.1
    if (price >= 500000):
        price -= price*0.2
    answer = int(price)
    
    return answer