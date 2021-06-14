def solution(n,a,b):
    answer = 0

    while a != b:
        a = (a+1) // 2
        b = (b+1) // 2
        answer += 1

    return answer

# 생각의 전환과 아이디어가 중요함을 느낀 문제