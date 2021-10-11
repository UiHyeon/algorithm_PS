import sys

def fibo(num):
    length = len(zero)
    if length <= num:
        for i in range(length, num+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])

    print('{} {}'.format(zero[num], one[num]))

zero = [1,0,1]
one = [0,1,1]

N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    num = int(sys.stdin.readline().rstrip())
    fibo(num)

#피보나치수열의 기본적인 이해도가 전반적으로 필요한 문제였다.
#피보나치의 f(n) = f(n-1) + f(n-2) 의 성질을 이용하는 것인데
#이 때 0과 1이 호출되는 횟수를 구하기 위해서도 위와 같은 성질을 응용한다.
#0, 1, 2의 수를 봣을 대 0과 1이 기본적으로 호출되는 구간을 구해 놓고
#성질을 이용해 이 나머지 0과 1도 같은 원리로 구할 수 있는 방법으로
#앞에서 구한 값을 재활용해 다시 계산에 사용하도록 하여 효율을 높이는
#동적계회법으로 문제를 푸는 것이다.

#이를 이해하는데 아직도 된듯 만듯하다. DP를 많이 풀어봐야 어떻게 접근을
#할 것인지 감을 잡을 수 있을 것 같다.