def solution(w,h):
    gcd_num = test(w,h)
    return w*h -(w+h-gcd_num)

def test(x,y):
    while y:
        temp = y
        y = x % y
        x = temp
    return x