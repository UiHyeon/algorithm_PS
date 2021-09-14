def solution(nums):
    answer = 0
    
    choice = int(len(nums) / 2)
    items = set(nums)

    for num in items:
        if choice > answer:
            answer += 1
        
    return answer

# 한 줄 코딩
# def solution(nums):
#     return min(len(nums)/2, len(set(nums)))