def solution(phone_book):
    phone_book.sort()  # 문자열 정렬
    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):  # 접두어 확인
            return False
    return True
