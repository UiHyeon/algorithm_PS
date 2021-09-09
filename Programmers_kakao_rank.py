from itertools import combinations

def solution(info, query):
    answer = []
    info_dict = {}
    
    #info의 데이터를 dictionary로 가공.
    #지원자의 info를 query에서 나올 수 있는 경우의 수만큼 
    #가공해서 저장해놓는다.
    for item in info:
        item = item.split()
        info_key = item[:-1]
        info_score = int(item[-1])
        for i in range(5):
            for temp in combinations(info_key, i):
                temp_key = ''.join(temp)
                try:
                    info_dict[temp_key].append(info_score)
                except:
                    info_dict[temp_key] = [info_score]
    
    #Binary search를 하기위해 필수적인 데이터 정렬
    for key in info_dict.keys():
        info_dict[key].sort()
    
    #query의 데이터들을 하나씩 꺼내 info의 데이터와 부합하는
    #것이 있는지 검색 후 lower bound알고리즘을 이용해 
    #query의 score점수와 맞는 조건의 수를 구한다.
    for item in query:
        item = item.replace(' and', '')
        item = item.split()
        while '-' in item:
            item.remove('-')
            
        query_key = ''.join(item[:-1])
        query_score = int(item[-1])
        
        if query_key in info_dict:
            scores = info_dict[query_key]
            if len(scores) > 0:
                low, high = 0, len(scores)
                while low < high:
                    mid = (low + high) // 2
                    if scores[mid] >= query_score:
                        high = mid
                    else:
                        low = mid + 1
                answer.append(len(scores) - low)
        else:
            answer.append(0)
        
    return answer