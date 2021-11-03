#이 문제를 통해 배운점은 직접 구현을 통한 n진수 변환법이다.
#아래의 convert함수와 같이 n진수 변환을 할 수 있는
#방법은 꼭 기억해두면 좋을 것 같다. 다른 문제에서도 
#유용하게 사용가능 할 듯 하다.

def convert(num, base):
    temp = "0123456789ABCDEF"
    q, r = divmod(num, base)

    if q == 0:
        return temp[r]
    else:
        # q를 base로 변환
        # 즉, n진수의 다음 자리를 구함
        return convert(q, base) + temp[r]

def solution(n, t, m, p):
    answer = ''
    temp = ''
    for i in range(t*m):
        temp += convert(i,n)
    
    for i in range(p-1, len(temp), m):
        answer += temp[i]
        if len(answer) == t:
            break
            
    return answer