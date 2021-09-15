# def solution(s):
#     answer = []
#     items = []
#     temp = s.split('},{')
#     for i in range(len(temp)):
#         items.append(list(map(int,temp[i].lstrip('{').rstrip('}').split(','))))
    
#     items.sort(key=len)
#     for item in items:
#         for check in item:
#             if check not in answer:
#                 answer.append(check)
        
#     return answer

import re
from collections import Counter

def solution(s):
    # 숫자만 찾아서 각 숫자의 counter값을 저장한다.
    s = Counter(re.findall('\d+', s))
    # s는 '숫자':개수 형식
    #Counter객체의 items()를 사용하면 '숫자',개수 형식으로 묶인다.
    #lambda표현식을 이용해 개수를 기준으로 정렬 후 많은 수의 '숫자'를 리스트에 int형으로 삽입.
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

