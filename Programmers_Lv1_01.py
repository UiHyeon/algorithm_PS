#소수를 판별하는 일종의 방법중에서 확인하려는 수의 제곱근 수 이하의 숫자가
#나눠떨어지는지를 확인하여 효율을 높일 수 있었다. 

from itertools import combinations

def solution(nums):
    answer = 0

    for item in combinations(nums, 3):
        check_num = sum(item)
        for i in range(2, int(check_num ** 0.5 + 1)):
            if check_num % i == 0:
                break
        else:
            answer += 1

    return answer