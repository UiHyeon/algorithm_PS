def rotate_key(key):
    #key를 90도 회전
    result = [[0] * len(key) for _ in range(len(key))]
    for row in range(len(key)):
        for col in range(len(key)):
            result[col][len(key)-1-row] = key[row][col]
    return result

def open_check(key, lock, row, col, start, end, expend_size):
    # 자물쇠 확장 (key길이-1)*2 + lock길이의 크기로
    graph = [[0] * (expend_size) for _ in range(expend_size)]
    
    for r in range(row, row + len(key)):
        for c in range(col, col + len(key)):
            graph[r][c] += key[r-row][c-col]

    for r in range(start, end):
        for c in range(start, end):
            graph[r][c] += lock[r-start][c-start]
            if graph[r][c] != 1:
                return False
    return True

def solution(key, lock):
    start = len(key) -1
    end = start + len(lock)
    expend_size = start * 2 + len(lock)

    for _ in range(4):
        for row in range(end):
            for col in range(end):
                if open_check(key, lock, row, col, start, end, expend_size):
                    return True
                    
        key = rotate_key(key)
        
    return False