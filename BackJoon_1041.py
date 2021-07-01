# 주사위는 위와 같이 생겼다. 주사위의 여섯 면에는 수가 쓰여 있다. 위의 전개도를 수가 밖으로 나오게 접는다.
# A, B, C, D, E, F에 쓰여 있는 수가 주어진다.
# 지민이는 현재 동일한 주사위를 N3개 가지고 있다. 이 주사위를 적절히 회전시키고 쌓아서, N×N×N크기의 정육면체를 만들려고 한다. 
# 이 정육면체는 탁자위에 있으므로, 5개의 면만 보인다.
# N과 주사위에 쓰여 있는 수가 주어질 때, 보이는 5개의 면에 쓰여 있는 수의 합의 최솟값을 출력하는 프로그램을 작성하시오.

import sys

N = int(sys.stdin.readline().rstrip())
temp = sys.stdin.readline().rstrip().split()
num_lst = [int(num) for num in temp]
symmetry_lst =[]
sum_num = 0

if N == 1:
    max_num = max(num_lst)
    for num in num_lst:
        sum_num += num
    sum_num -= max_num

else:
    symmetry_lst.append(min(num_lst[0],num_lst[5]))
    symmetry_lst.append(min(num_lst[1],num_lst[4]))
    symmetry_lst.append(min(num_lst[2],num_lst[3]))

    symmetry_lst.sort()

    side1 = (N-2)*(N-2) + 4*(N-2)*(N-1)
    side2 = 4*(N-1) + 4*(N-2)
    side3 = 4

    sum_num += side1 * symmetry_lst[0] 
    sum_num += side2 * (sum(symmetry_lst[0:2])) 
    sum_num += side3 * (sum(symmetry_lst))

print(sum_num)
