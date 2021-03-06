# def solution(s):
#     answer = [0, 0]
    
#     while s != '1':
#         before_len = len(s)
#         s = s.replace('0', '')
#         after_len = len(s)
#         answer[1] += before_len - after_len
#         s = bin(len(s))[2:]
#         answer[0] += 1
        
#     return answer

def solution(s):
    answer = [0, 0]
    
    while s != '1':
        answer[0] += 1
        num = s.count('1')
        answer[1] += len(s) - num
        s = bin(num)[2:]
        
    return answer