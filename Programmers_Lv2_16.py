# def solution(n, words):
#     answer = []
#     check = [0] * n
#     check[1] = 1
#     used_words = [words[0]]
#     pre_word = words[0]
    
#     for i in range(1, len(words)):
#         real_num = i + 1
        
#         if words[i] not in used_words:
#             if pre_word[-1] == words[i][0]:
#                 used_words.append(words[i])
#                 check[real_num % n] += 1
#             else:
#                 check[real_num % n] += 1
#                 if real_num % n == 0:
#                     answer.append(n)
#                 else:
#                     answer.append(real_num % n)
#                 answer.append(check[real_num % n])
#                 break
#         else:
#             check[real_num % n] += 1
#             if real_num % n == 0:
#                 answer.append(n)
#             else:
#                 answer.append(real_num % n)
#             answer.append(check[real_num % n])
#             break
            
#         pre_word = words[i]
        
#     if len(used_words) == len(words):
#         answer.append(0)
#         answer.append(0)

#     return answer

def solution(n, words):
    answer = []
    used_words = [words[0]]
    user_idx = 0
    for idx in range(1, len(words)):
        if words[idx-1][-1] != words[idx][0]:
            user_idx = idx
            break
        if words[idx] in used_words:
            user_idx = idx
            break
            
        used_words.append(words[idx])
        user_idx = idx
        
    if len(used_words) == len(words):
        answer = [0,0]
    else:
        answer = [user_idx%n + 1, user_idx//n + 1]
    
    return answer