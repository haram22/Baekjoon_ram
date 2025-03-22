import datetime
def solution(a, b):
    answer = ''
    week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    day = datetime.datetime(2016, a, b)
    answer = week[day.weekday()]
    return answer