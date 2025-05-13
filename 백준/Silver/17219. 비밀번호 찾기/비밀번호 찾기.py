a, b = map(int, input().split())
pwDict = dict()
answer = [''] * b
for i in range(a) :
    s, p = map(str, input().split())
    pwDict[s] = p

for j in range(b) :
    f = input()
    answer[j] = pwDict[f]

for i in answer :
    print(i)