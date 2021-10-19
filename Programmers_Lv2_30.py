def solution(s):
    answer = True
    stack = []
    
    for item in s:
        if item == ')':
            if not stack: return False
            if stack.pop() == '(':
                continue
            else:
                return False
        stack.append(item)
        
    if stack: return False

    return True