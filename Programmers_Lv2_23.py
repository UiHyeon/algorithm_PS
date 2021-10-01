# def get_zero(lottos):
#     count = 0
#     for num in lottos:
#         if num == 0 :
#             count += 1
#     return count

# def solution(lottos, win_nums):
#     answer = [0] * 2
#     check_nums = [0] * 2
#     rank = [6,5,4,3,2]
#     zero_cnt = get_zero(lottos)
    
#     for num in lottos:
#         if num in win_nums:
#             check_nums[0] += 1
#             check_nums[1] += 1
            
#     check_nums[0] += zero_cnt
    
#     for i in range(len(check_nums)):
#         try:
#             answer[i] = rank.index(check_nums[i]) + 1
#         except:
#             answer[i] = 6
    
#     return answer

def solution(lottos, win_nums):
    answer = 0
    zero_cnt = lottos.count(0)
    rank = [6,6,5,4,3,2,1]
    
    for num in lottos:
        if num in win_nums:
            answer += 1
    return rank[zero_cnt + answer], rank[answer]