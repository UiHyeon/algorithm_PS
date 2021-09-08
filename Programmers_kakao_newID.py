import re

def solution(new_id):
    answer = ''
    
    #step 1,2
    answer = new_id.lower()
    convention = re.compile('[a-z0-9\.\-\_]')
    temp = convention.findall(answer)
    answer = ''.join(temp)
    
    #step 3
    while '..' in answer:
        answer = answer.replace('..','.')
        
    #step 4
    answer = answer.lstrip('.')
    answer = answer.rstrip('.')
        
    #step 5
    if answer == "":
        answer = 'a'
        
    #step 6
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer.rstrip('.')
            
    #step 7
    while len(answer) < 3:
        answer += answer[-1]
            
    return answer