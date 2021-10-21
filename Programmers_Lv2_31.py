from string import ascii_uppercase
from collections import defaultdict

def solution(msg):
    answer = []
    alpha = list(ascii_uppercase)
    alpha_dict = defaultdict(str)
    
    for i in range(1, len(alpha) +1):
        alpha_dict[alpha[i-1]] = i
    #위 같이 안쓰고 
    #alpha_dict = {chr(e + 64): e for e in range(1, 27)}
    #과 같이 ASCII코드를 사용해 dict을 구현할 수 있다.
    
    check = ''
    for i in range(1, len(msg) + 1):
        check += msg[i-1]

        if check in alpha_dict.keys():
            continue
        else:
            answer.append(alpha_dict[check[:-1]])
            alpha_dict[check] = len(alpha_dict) + 1
            check = check[-1]

    answer.append(alpha_dict[check])
    
    return answer