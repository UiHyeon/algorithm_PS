def solution(n, times):
    answer = 0
    start, end = 1, max(times) * n
    
    while start <= end:
        people = 0
        mid = (start + end) // 2
        for time in times:
            people += mid // time
            if people >= n:
                break
                
        if people >= n:
            end = mid -1
            answer = mid
        elif people < n:
            start = mid + 1
            
    return answer