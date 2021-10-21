# from collections import deque

# cache_hit = 1
# cache_miss = 5

# def solution(cacheSize, cities):
#     answer = 0
#     que = deque()
    
#     for city in cities:
#         city = city.lower()

#         if city in que:
#             que.remove(city)
#             que.append(city)
#             answer += cache_hit
#         else:
#             answer += cache_miss
#             if cacheSize != 0:
#                 if len(que) == cacheSize:
#                     que.popleft()
#                 que.append(city)
            
#     return answer

from collections import deque

def solution(cacheSize, cities):
    answer = 0
    que = deque(maxlen = cacheSize)
    
    for city in cities:
        city = city.lower()
        
        if city in que:
            answer += 1
            que.remove(city)
            que.append(city)
        else:
            answer += 5
            que.append(city)
            
    return answer