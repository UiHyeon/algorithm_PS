import sys
N = int(sys.stdin.readline())
dp = [0] * 101
dp[1], dp[2], dp[3], dp[4] = 1, 1, 1, 2

for _ in range(N):
    num = int(sys.stdin.readline())
    for i in range(5, num+1):
        dp[i] = dp[i-2] + dp[i-3]

    print(dp[num])

#DP관련 문제를 연속적으로 3문제를 풀어보니 문제의 가장 작은
#조각부터 시작하여 일정한 패턴을 찾는 방법과 그 패턴을 통해
#얻은 값들을 메모이제이션을 통해 데이터재활용을 하여 빠른 연산을
#할 수 있도록 하는 접근법이 익숙해짐.