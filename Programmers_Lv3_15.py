#투 포인터를 사용해야하는 풀이방식의 문제
#투 포인터 유형을 어떻게 접근하고 해결해야 하는지
#감을 잡을 수 있어서 유익하다.

def solution(gems):
    answer = []
    gem_len = len(set(gems))
    gem_dict = {}
    start, end = 0, 0
    gem_sect = len(gems) + 1
    
    while end < len(gems):
        if gems[end] not in gem_dict:
            gem_dict[gems[end]] = 1
        else:
            gem_dict[gems[end]] += 1
        
        end += 1
        
        if len(gem_dict) == gem_len:
            while start < end:
                if gem_dict[gems[start]] > 1:
                    gem_dict[gems[start]] -= 1
                    start += 1
                elif end - start < gem_sect:
                    gem_sect = end - start
                    answer = [start+1, end]
                    break
                else:
                    break
    
    return answer

# def solution(gems):
#     answer = [0, len(gems) + 1]
#     gem_len = len(set(gems))
#     gem_dict = {gems[0] : 1}
#     start, end = 0, 0
    
#     while start < len(gems) and end < len(gems):
#         if gem_len == len(gem_dict):
#             if end - start < answer[1] - answer[0]:
#                 answer = [start+1, end+1]
#             if gem_dict[gems[start]] == 1:
#                 del gem_dict[gems[start]]
#             else:
#                 gem_dict[gems[start]] -= 1
#             start += 1
            
#         else:
#             end += 1
#             if end == len(gems):
#                 break
#             if gems[end] not in gem_dict:
#                 gem_dict[gems[end]] = 1
#             else:
#                 gem_dict[gems[end]] += 1
    
#     return answer