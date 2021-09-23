def solution(n):
    answer = 0
    
    for idx in range(1, n+1):
        sum_num = 0
        for num in range(idx, n+1):
            sum_num += num
            
            if sum_num == n:
                answer += 1
                break
            elif sum_num > n:
                break
    
    return answer