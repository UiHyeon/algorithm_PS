import sys
N = int(sys.stdin.readline())
dp = [0] * 1000001
dp[1], dp[2] = 1, 2

for i in range(3, N+1):
    dp[i] = (dp[i-2] + dp[i-1]) % 15746

print(dp[N])

#DP문제를 풀 때 밑바닥 붙어 계산해 올라가다 보면
#특정 규칙성이 보일 때가 있다 이를 이용해 점화식으로
#만들어 메모이제이션을 응용해 앞에서 이루어진 결과값들을
#재사용함으로써 문제를 해결할 수 있다.