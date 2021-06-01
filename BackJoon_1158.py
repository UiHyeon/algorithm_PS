# 요세푸스 문제는 다음과 같다.

# 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 
# 이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 
# 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 
# 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

# N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

import sys

a = sys.stdin.readline().rstrip()
N, K = map(int, a.split())
first_lst = []
number = K-1
answer = []
result = ''

for i in range(N):
    first_lst.append(i+1)

while first_lst:
    if number <= len(first_lst)-1:
        answer.append(first_lst.pop(number))
        number += K-1
    else:
        number = number % len(first_lst)
        answer.append(first_lst.pop(number))
        number += K-1

for i in answer:
    result += (str(i) +', ')

print('<' + result[0:-2] + '>')
