import math

def solution(brown, yellow):
    answer = []
    
    for i in range(1, yellow+1):
        temp = yellow / i
        
        if ((temp*2) + (i*2) + 4) == brown :
            answer.extend([temp+2, i+2])
            return answer
        
    return answer