import sys

temp = list(sys.stdin.readline().rstrip())
answer = 0

def check(temp):
    check_stack = []
    for item in temp:

        if item == ')':
            if not check_stack: return False
            if check_stack.pop() == '(':
                continue
            else:
                return False

        if item == ']':
            if not check_stack: return False
            if check_stack.pop() == '[':
                continue
            else:
                return False
        check_stack.append(item)

    if check_stack: return False

    return True

if check(temp):
    stack = []
    for item in temp:
        if item == ']':
            temp = 0
            while stack:
                top = stack.pop()
                if top =='[':
                    if temp == 0:
                        stack.append(3)
                    else:
                        stack.append(temp*3)
                    break
                else:
                    if temp == 0:
                        temp = int(top)
                    else:
                        temp += int(top)
            
        elif item == ')':
            temp = 0
            while stack:
                top = stack.pop()
                if top =='(':
                    if temp == 0:
                        stack.append(2)
                    else:
                        stack.append(temp*2)
                    break
                else:
                    if temp == 0:
                        temp = int(top)
                    else:
                        temp += int(top)

        else:
            stack.append(item)

    for num in stack:
        answer += num

    print(answer)

else: print(0)