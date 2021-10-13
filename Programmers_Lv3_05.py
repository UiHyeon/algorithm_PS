from collections import defaultdict

def solution(n, results):
    answer = 0
    win, lose = defaultdict(set), defaultdict(set)
    #defaultdict은 인자로 주어진 객체가 딕셔너리의 초기값으로 설정되는 것.
    
    for A, B in results:
        win[A].add(B)
        lose[B].add(A)
    
    for i in range(1, n+1):
        # A에게 진 사람은 A를 이긴 모든 사람에게 진다.
        for loser in win[i]:
            lose[loser].update(lose[i])
        # A에게 이긴 사람은 A가 이긴 모든 사람에게 이긴다.
        for winner in lose[i]:
            win[winner].update(win[i])
    
    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n-1:
            answer += 1
    
    return answer