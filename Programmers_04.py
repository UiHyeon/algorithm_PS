def solution(s):
    answer = -1
    stack = []
    
    for temp in s:
        if len(stack) == 0:
            stack.append(temp)
            continue
            
        first = stack.pop()
        
        if first == temp:
            continue
        else:
            stack.append(first)
            stack.append(temp)
            
    if len(stack) == 0:
        return 1
    else:
        return 0
        
    return answer