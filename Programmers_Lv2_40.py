from itertools import permutations

def solution(k, dungeons):
    answer = -1
    combi = list(permutations(dungeons, len(dungeons)))
    
    for item in combi:
        fatigue = k
        count = 0
        for info in item:
            condition = info[0]
            use_fatigue = info[1]
            if fatigue >= condition:
                fatigue -= use_fatigue
                count += 1
        answer = max(answer, count)
        
    return answer