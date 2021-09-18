#2x2 사각형을 찾기 위한 함수
def find_rec(board, m, n):
    #해당하는 좌표의 중복을 없애기 위해 set 사용
    check_lst = set() 
    
    for r in range(m-1):
        for c in range(len(board[r]) -1):
            count = 0
            if board[r][c] != '_':
                #오른쪽
                if board[r][c] == board[r][c+1]:
                    count += 1
                #오른쪽 아래(대각선)
                if board[r][c] == board[r+1][c+1]:
                    count += 1
                #아래
                if board[r][c] == board[r+1][c]:
                    count += 1

                if count == 3:
                    check_lst.add((r,c))
                    check_lst.add((r,c+1))
                    check_lst.add((r+1,c+1))
                    check_lst.add((r+1,c))
                
    return check_lst

#제거되는 블록을 제거하고 그 빈자리에 '_'으로 채워주는 함수
def change_board(board, check, m, n):
    #블록 삭제
    for r, c in check:
        board[r].pop(c)
        
    #빈 자리 채우기
    for r in range(m):
        need = n - len(board[r])
        for i in range(need):
            board[r].append('_')
        
    return board

def solution(m, n, board):
    answer = 0
    # 90도 회전한 board를 담을 변수
    trans_board = [[] for _ in range(n)]
    #90도 회전 시켜 trans_board를 만든다.
    for r in reversed(range(n)):
        for c in reversed(range(m)):
            trans_board[r].append(board[c][r])
    
    m = len(trans_board)        #높이
    n = len(trans_board[0])     #폭
    
    while True:
        check = find_rec(trans_board, m, n)
        #발견되는 2x2 사각형이 없다면 중단
        if not check:
            break
        #위에 있는 것부터 제거해야됨으로 정렬
        check = sorted(check, key = lambda x:x[1], reverse = True)
        trans_board = change_board(trans_board, check, m, n)
    
    #빈 블록 수 구하기
    for r in range(m):
        for c in range(n):
            if trans_board[r][c] == '_':
                answer += 1
    
    return answer