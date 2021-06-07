def right(s):
    check = 0
    for i in s:
        if i == '(':
            check += 1
        else:
            check -= 1
            
        if check < 0 :
            return False
        return True

def reverse(s):
    result = ''
    for i in s:
        if i == '(':
            result += ')'
        else:
            result += '('
    return result

def solution(p):
    answer = ''
    check = 0
    
    if p == '':
        return ''
    
    for i in range(len(p)):
        if p[i] == '(':
            check += 1
        else:
            check -= 1
            
        if check == 0:
            u = p[:i+1]
            v = p[i+1:]
            break
        
    if right(u):
        return u + solution(v)
    else:
        return '(' + solution(v) + ')'+ reverse(u[1:-1])
    