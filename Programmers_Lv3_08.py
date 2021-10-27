# def solution(A, B):
#     answer = 0
#     A.sort()
#     B.sort()
#     a_idx, b_idx = 0, 0
#     while len(A) != a_idx and len(B) != b_idx:
#         if A[a_idx] < B[b_idx]:
#             a_idx += 1
#             b_idx += 1
#             answer += 1
#         else:
#             b_idx += 1
    
#     return answer

#투포인터 알고리즘의 개념을 학습할 수 있었다.

def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    j = 0
    for i in range(len(A)):
        if A[j] < B[i]:
            answer += 1
            j += 1
    
    return answer