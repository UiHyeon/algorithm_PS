from itertools import combinations

def solution(relation):
    key_num = len(relation[0])
    row = len(relation)
    #모든 가능한 키의 조합
    combi = []
    for i in range(1, key_num+1):
        combi.extend(combinations(range(key_num), i))
        
    #유일성을 만족하는 키의 조합
    unique = []
    for check in combi:
        temp = [tuple([item[i] for i in check])  for item in relation]
        if len(set(temp)) == row:
            unique.append(check)
            
    #최소성을 만족하는지 판별
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                answer.discard(unique[j])
    
    return len(answer)