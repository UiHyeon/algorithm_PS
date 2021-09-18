# def solution(n):
#     answer = 0
#     temp = bin(n)[2:]
#     check = 0
#     for item in temp:
#         if item == '1':
#             check += 1
    
#     for i in range(n+1, 1000000):
#         count = 0
#         next_num = bin(i)[2:]
#         for num in next_num:
#             if num == '1':
#                 count += 1
        
#         if check == count:
#             answer = i
#             break
            
#     return answer

def solution(n):
    answer = 0
    n_count = bin(n).count('1')
    
    while True:
        n += 1
        if n_count == bin(n).count('1'):
            break
    return n