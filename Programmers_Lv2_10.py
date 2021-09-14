def solution(d, budget):
    answer = len(d)
    d.sort(reverse = True)
    d_sum = sum(d)
    
    for i in range(len(d)):
        if d_sum <= budget:
            return answer
        d_sum -= d[i]
        answer -= 1
        
    return answer