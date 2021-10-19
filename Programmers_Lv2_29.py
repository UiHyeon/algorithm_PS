# def solution(files):
#     answer = []
#     for item in files:
#         head, number, tail = '', '', ''
#         num_check = False
        
#         for i in range(len(item)):
#             if item[i].isdigit():
#                 number += item[i]
#                 num_check = True
#             elif not num_check:
#                 head += item[i]
#             else:
#                 tail = item[i:]
#                 break
#         answer.append([head, number, tail])
        
#     result = sorted(answer, key = lambda x: (x[0].upper(), int(x[1])))
                
#     return [''.join(item) for item in result]

import re

def solution(files):
    answer = []
    
    order_digit = sorted(files, key = lambda file : int(re.findall('\d{1,5}', file)[0]))
    answer = sorted(order_digit, key = lambda file : re.findall('\D+', file)[0].upper())
    # answer = sorted(order_digit, key = lambda file : re.split('\d{1,5}', file)[0].upper())
    # 이것도 가능하다.

    return answer