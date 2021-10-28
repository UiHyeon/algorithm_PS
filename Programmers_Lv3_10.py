import math

def solution(n, stations, w):
    answer = 0
    check = []
    start, end = 1, 0
    W = w * 2 + 1

    for num in stations:
        end = num - w - 1
        check.append((start, end))
        start = num + w + 1
        
    if start <= n:
        check.append((start, n))
    
    for item in check:
        distance = item[1] - item[0] + 1
        answer += math.ceil(distance / W)
            
    return answer