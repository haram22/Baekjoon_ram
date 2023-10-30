# 1. 단어 입력받기 (대문자로 모두 바꾸기)
# 2. 입력받은 단어를 중복 없이 새로운 리스트에 저장하기
# 3. 저장한 리스트와 입력받은 단어를 비교해서, 같은 단어가 나오면 각 인덱스에 count++
# 4. count한 리스트 중 max 찾기
# 5. 만약 가장 큰 값이 2개 이상이면, ? 출력하기
    # max 찾고, 다시 count랑 비교해서 max가 두개 이상인지 확인

word = input().upper()
count = []
alphabet = list(set(word))
count_max = 0
index = 0

for i in range(len(alphabet)):
    count.append(0)

for i in range(len(word)):
    for j in range(len(alphabet)):
        if (word[i] == alphabet[j]):
            count[j] +=1

result = max(count)
for i in range(len(count)):
    if (count[i] == result):
        count_max +=1
        index = i

if (count_max == 1 ):
    print(alphabet[index])
else: 
    print("?")