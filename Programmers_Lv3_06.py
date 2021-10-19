from collections import defaultdict

def solution(genres, plays):
    answer = []
    count = defaultdict(int)
    info = defaultdict(list)
    for item, num in zip(genres, plays):
        count[item] += num
        
    result = sorted(count.items(), key = lambda x : x[1], reverse = True) 
    cnt = 0
    for gen, num in zip(genres, plays):
        info[cnt] = [gen, num]
        cnt += 1
    
    for gen in result:
        check = []
        for key in info.keys():
            if gen[0] in info[key]:
                check.append([info[key][1], key])
                
        check = sorted(check, key = lambda x : (-x[0], x[1]))
        if len(check) == 1:
            answer.append(check[0][1])
        else:
            for i in range(2):
                answer.append(check[i][1])
    return answer