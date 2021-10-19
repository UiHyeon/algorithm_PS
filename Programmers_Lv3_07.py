def solution(m, n, puddles):
    answer = 0
    dp = [[0] * (m+1) for _ in range(n+1)]
    puddles = [[b, a] for [a, b] in puddles]
    
    dp[1][1] = 1
    
    for r in range(1, n+1):
        for c in range(1, m+1):
            if r == 1 and c == 1: continue
            if [r, c] in puddles:
                dp[r][c] = 0
            else:
                dp[r][c] = (dp[r-1][c] + dp[r][c-1]) % 1000000007
    return dp[n][m]