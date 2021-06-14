def solution(s):
    stack = []
    
    for temp in s:
        if len(stack) == 0: stack.append(temp)
        elif stack[-1] == temp: stack.pop()
        else: stack.append(temp)
            
    if len(stack) == 0 : 
        return 1
    else:
        return 0