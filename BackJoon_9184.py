import sys

dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]

def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if dp[a][b][c]:
        return dp[a][b][c]

    if a < b and b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]

    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dp[a][b][c]

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1 and c == -1:
        break

    print('w(%d, %d, %d) = %d' %(a, b, c, w(a, b, c)))


#DP문제 풀이에 있어서 중요한 부분중 하나가 바로 메모이제이션이다. 
#중복 연산을 하지 않고 이미 계산한 결과를 따로 저장을하여 다른 계산을
#할 때 재사용을 하여 연산 처리시간을 단축시키는 것이다.
#즉, 메모리라는 비용을 사용하여 시간의 효율을 당겨오는 기법이다.