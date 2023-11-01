import sys

# 입력 받기
N = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(N)]

# 정렬
numbers.sort()

# 출력
for num in numbers:
    sys.stdout.write(str(num) + '\n')