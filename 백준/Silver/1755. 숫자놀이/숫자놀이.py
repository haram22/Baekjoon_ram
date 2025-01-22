a, b = map(int, input(). split(' '))
def change(a) :
    alpha = {'0' : 'zero', '1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}
    strA = str(a)
    result = ''
    for num in strA :
        result += alpha[num]
    return result

final = []
finDict = {}
for i in range(a, b+1) :
    finDict.update({i : change(i)})
answer = dict(sorted(finDict.items(), key=lambda items : items[1]))
answerList = list(answer)

for i in range(len(answerList)) :
    print(answerList[i], end=' ')
    if (i+1) % 10 == 0 :
        print("")
print("")