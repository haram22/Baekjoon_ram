import sys
from collections import Counter

# 입력 받기
N = int(sys.stdin.readline())
book = [sys.stdin.readline().strip() for _ in range(N)]

# 책 제목과 판매 횟수 세기
book_count = Counter(book)

# 가장 많이 팔린 책 찾기
max_count = max(book_count.values())
most_sold_books = [title for title, count in book_count.items() if count == max_count]

# 사전순으로 정렬하여 가장 앞선 제목 출력
print(sorted(most_sold_books)[0])
