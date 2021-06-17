from itertools import permutations
import re

def cal_test(op, num1, num2):
    if op == '+':
        return num1 + num2
    if op == '-':
        return num1 - num2
    if op == '*':
        return num1 * num2

def solution(expression):
    answer = 0
    cal = ['+', '-', '*']
    cal_temp = list(permutations(cal,3))
    print(cal_temp)
    max_num = 0
    # expression 연산자 기준 쪼개기
    exp = re.findall("(\d+)([*+-]?)", expression)
    exp_temp = []
    for temp in exp:
        exp_temp.append(temp[0])
        exp_temp.append(temp[1])
    
    for oper in cal_temp:
        exp = exp_temp[:-1]
        exp.reverse()
        for i in range(len(oper)):
            result = []
            while exp:
                thing = exp.pop()
                if oper[i] == thing:
                    num1 = int(result.pop())
                    num2 = int(exp.pop())
                    op = oper[i]
                    cal_num = cal_test(op,num1,num2)
                    result.append(str(cal_num))
                else:
                    result.append(thing)
                    
            exp = result
            exp.reverse()
            
        if max_num < abs(int(exp[0])):
            max_num = abs(int(exp[0]))
        
    return max_num