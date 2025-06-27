def solution(people, limit):
    count = 0
    people.sort(reverse=True)
    print(people)
    for i in people :
        total = i
        if total+people[-1] <= limit :
            people.pop()
        count += 1
    return count
