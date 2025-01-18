s = input()
order = []
order = list(set(s))
result = []
for i in range(len(order)) :
    for j in range(len(s)) :
        if order[i] == s[j] :
            result.append(s[j:])
result.sort()
for word in result :
    print(word)