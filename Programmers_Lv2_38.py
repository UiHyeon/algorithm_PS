import math

def find_num(x, y):
    return (x*y) // math.gcd(x,y)

def solution(arr):
    answer = 0
    
    while len(arr) > 1:
        arr.append(find_num(arr.pop(), arr.pop()))
        
    return arr[0]