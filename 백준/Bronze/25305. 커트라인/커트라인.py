N, k = map(int, input().split(' '))
scores = []
scores += map(int, input().split(' '))
scores.sort(reverse=True)
print(scores[k-1])