#방향성을 가지는 길찾기 문제에서 양방향을 고려해줘야하는 것을 알게되었다.
#지나간 곳의 길이를 구하는 문제. -> 양방향성이 있기 때문에 출발한 지점과 
#도착한 지점을 둘다 생각해줘야한다. 그래야 지나간 길이라고 볼 수 있다.
#set을 이용해 방문한 경로를 중복없이 집합으로 저장할 수 있다.

def solution(dirs):
    dirs_dict = {'U': [-1, 0], 'D': [1 , 0], 'L': [0, -1], 'R': [0, 1]}
    visit = set()
    row, col = 0, 0
    for dir in dirs:
        new_r = row + dirs_dict[dir][0]
        new_c = col + dirs_dict[dir][1]
        
        if -6 < new_r < 6 and -6 < new_c < 6:
            visit.add((row, col, new_r, new_c))
            visit.add((new_r, new_c, row, col))
            row, col = new_r, new_c
    
    return len(visit) / 2