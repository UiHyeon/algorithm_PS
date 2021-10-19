def solution(s):
    check = []
    for item in s.split(' '):
        check.append(item.lower())
    
    for i in range(len(check)):
        if check[i] == '': 
            check[i] = ' ' 
            continue
        if check[i][0].isalpha:
            check[i] = check[i][0].upper() + check[i][1:] + ' '

    return ''.join(check)[:-1]