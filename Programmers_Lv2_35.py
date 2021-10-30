from collections import deque

def solution(people, limit):
    answer = 0
    que = deque(sorted(people))
    
    while que:
        min_item = que.popleft()
        if not que:
            return answer + 1
        max_item = que.pop()
        if min_item + max_item > limit:
            que.appendleft(min_item)
        answer += 1
    
    return answer