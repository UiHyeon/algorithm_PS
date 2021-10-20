from string import ascii_uppercase
from collections import defaultdict

def solution(msg):
    answer = []
    alpha = list(ascii_uppercase)
    alpha_dict = defaultdict(str)
    temp = ''
    
    for i in range(1, len(alpha) +1):
        alpha_dict[alpha[i-1]] = i
    
    for i in range(len(msg)):
        if i == (len(msg) -1):
            check = msg[i]
            answer.append(alpha_dict[check])
        if i == (len(temp)-1):
            continue
        check = msg[i]
        temp += msg[i]
        print("==========")
        print(check)
        
        for j in range(i+1, len(msg)):
            check += msg[j]
            temp += msg[j]
            print(check)
            #추가한 문자가 사전에 없으면
            if check not in alpha_dict.keys():
                #문자 추가하는 것을 멈춘다.
                print(check[:-1])
                answer.append(alpha_dict[check[:-1]])
                temp = temp[:-1]
                alpha_dict[check] = list(alpha_dict.values())[-1] + 1
                break
            
        
    print(answer)
    print(alpha_dict)
    
    
    return answer