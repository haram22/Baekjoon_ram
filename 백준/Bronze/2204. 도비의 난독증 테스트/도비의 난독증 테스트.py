N = 1
answer = []
while (1) :
    N = int(input())
    if N == 0 :
        break
    listDict = dict()
    wordList = []
    for i in range(N) :
        word = input()
        wordList.append(word)
        lowWord = word.lower()
        listDict.update({ i : lowWord})
    sortedDict = dict(sorted(listDict.items(), key=lambda item: item[1]))
    ans = list(sortedDict.keys())[0]
    answer.append(wordList[ans])

for word in answer :
    print(word)