from itertools import product

def solution(word):
    data_list = []
    
    for i in range(1, 6):
        data_list += list(map(list, product('AEIOU', repeat = i)))
        
    for i in range(len(data_list)):
        data_list[i] = ''.join(data_list[i])
    
    data_list.sort()
    
    return data_list.index(word) + 1