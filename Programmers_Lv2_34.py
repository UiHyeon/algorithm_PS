def solution(n):
    ans = 0

    while True:
        if n == 0:
            break
        if n % 2 == 0 :
            n = n/2
        else:
            n -= 1
            ans += 1

    return ans

# def solution(n):
#     return bin(n)[2:].count('1')