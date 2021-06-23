def solution(n):
    pivo_lst = []
    
    for i in range(n+1):
        if i == 0: pivo_lst.append(0)
        elif i == 1 or i == 2: pivo_lst.append(1)
        else: pivo_lst.append((pivo_lst[i-1] + pivo_lst[i-2]) % 1234567)
            
    return pivo_lst[-1]