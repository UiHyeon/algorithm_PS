def solution(prices):
    answer = [0] * len(prices)
    stack = []
    
    for idx, price in enumerate(prices):
        while stack and price < prices[stack[-1]] :
            check = stack.pop()
            answer[check] = idx - check
            
        stack.append(idx)
        
    while stack:
        check = stack.pop()
        answer[check] = len(prices) - 1 - check
    return answer