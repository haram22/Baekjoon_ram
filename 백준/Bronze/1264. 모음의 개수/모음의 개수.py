# 모음을 검사할 함수
def is_vowel(char):
    return char in 'aeiouAEIOU'

# 입력 받기
while True:
    line = input()
    if line == '#':
        break

    # 모음 개수 세기
    vowel_count = sum(1 for char in line if is_vowel(char))

    # 결과 출력
    print(vowel_count)
