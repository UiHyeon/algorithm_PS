def solution(n):
    answer = []
    temp = [[0] * i for i in range(1, n+1)]
    
    r, c = -1, 0
    num = 1
    
    for i in range(n):
        for k in range(i, n):
            #아래
            if i % 3 == 0:
                r += 1
            #오른쪽
            elif i % 3 == 1:
                c += 1
            #왼쪽 위
            else:
                r -= 1
                c -= 1
                
            temp[r][c] = num
            num += 1
            
    for item in temp:
        answer.extend(item)
    
    return answer

    # return sum(temp,[])
    #위 와 같이 리스트들을 한번에 모으는 기법이 
    #있는데 이는 기존에 extend를 사용해 리스트들을
    #합해주는 것보다 효율성이 떨어졌다.