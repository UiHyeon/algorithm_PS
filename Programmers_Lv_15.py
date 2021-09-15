#정확한 접근법을 통한 DP풀이
def solution(board):
    answer = 0
    #정사각형이 생성가능한 부분의 값을 쌓기 위한 dp 선언
    dp = [[0]* len(board[0]) for i in range(len(board))]
    #board의 가로 첫 줄과 세로 첫줄을 같도록 비교. 왜? (1,1)부터 
    #'위', '왼쪽위 대각선', '왼쪽'의 값을 비교하도록 한다
    #한 지점 마다 가능한 부분을 쌓아가는 것이다.
    dp[0] = board[0]
    for i in range(1, len(board)):
        dp[i][0] = board[i][0]
        
    # (1,1)부터 검사 시작.
    for r in range(1, len(board)):
        for c in range(1, len(board[0])):
            #해당 위치가 board상에서 1이여야 정사각형을 이룰 수 있는 한 변이 된다.
            if board[r][c] == 1:
                #해당 위치에서 가능한 지점을 쌓는 dp에서 위, 왼쪽위 대각선, 왼쪽의 지점이 가능한 길이의 최소값에서 +1한다.
                dp[r][c] = min(dp[r][c-1], dp[r-1][c-1], dp[r-1][c]) +1
                #가능한 최대 사각형의 길이를 알 수 있기 때문에.
    for check in dp:
        answer = max(answer, max(check))
    
    return answer**2


# 효율성을 통과하지 못한 코드

# def dp(board, root):
#     check_size = min((len(board)-root[0]), (len(board[0])-root[1]))
#     result = 0
    
#     for size in range(1, check_size+1):
#         flag = True
#         for r in range(root[0], root[0]+size):
#             for c in range(root[1], root[1]+size):
#                 if board[r][c] != 1:
#                     flag = False
#                     break
#             if not flag:
#                 break
#         if flag and result < size:
#             result = size
#     return result

# def solution(board):
#     answer = 1234
#     check = []
#     temp = 0
#     for i in range(len(board)):
#         for j in range(len(board[0])):
#             if board[i][j] == 1:
#                 check.append([i,j])
                
#     for r, c in check:
#         temp = max(temp, dp(board, [r,c]))
        
#     answer = temp * temp     
    
#     return answer