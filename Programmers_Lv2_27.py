#코드 수가 많지만 아래 간결한 코드보다 효율성이 좋게 나온다.
def solution(land):
    answer = 0
    
    for row in range(1, len(land)):
        land[row][0] += max(land[row-1][1], land[row-1][2], land[row-1][3])
        land[row][1] += max(land[row-1][0], land[row-1][2], land[row-1][3])
        land[row][2] += max(land[row-1][0], land[row-1][1], land[row-1][3])
        land[row][3] += max(land[row-1][0], land[row-1][1], land[row-1][2])
        
    answer = max(land[-1])
    return answer

#간결하지만 2중 for문을 사용하기에 다소 효율성이 떨어진다.
# def solution(land):
#     for row in range(1, len(land)):
#         for cal in range(len(land[0])):
#             land[row][cal] += max(land[row-1][:cal] + land[row-1][cal+1:])
#     return max(land[-1])

#DP문제의 해결접근방법에 대한 좋은 배움의 문제.