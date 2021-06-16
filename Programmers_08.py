from itertools import permutations

def cal_oper(num1,num2,oper):
    if oper == '+':
        return num1 + num2
    if oper == '-':
        return num1 - num2
    if oper = '*':
        return num1 * num2

def solution(expression):
    answer = 0
    cal = ['+', '-', '*']
    cal_temp = list(permutations(cal,3))
    max_num = 0
    number = ''
    
    front_q = []
    end_q = [expression[i] for i in range(len(expression)-1,-1,-1)]
    
    print(end_q)
    
    while cal_temp:
        temp = cal_temp.pop()
        
        for i in range(len(temp)):
            while end_q:
                end_pop = end_q.pop()
                
                if end_pop not in cal:
                    number += end_pop
                else:
                    front_q.append(number)
                    number = ''
                    
                    if end_pop == temp[i]:
                        num1 = front_q.pop()
                        num2 = end_q.pop()
            
    return max_num