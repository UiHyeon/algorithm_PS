import sys
from collections import deque

temp = list(sys.stdin.readline().rstrip())
print(temp)
answer = 0

def check(temp):
    stack = []
    for item in temp:

        if item == ')':
            if not stack: return False
            if stack.pop() == '(':
                continue
            else:
                return False

        if item == ']':
            if not stack: return False
            if stack.pop() == '[':
                continue
            else:
                return False
        stack.append(item)

    if stack: return False

    return True

if check(temp): print('O')
else: print('x')



# stack = []
# for item in temp:
#     if item == ']':
#         check = stack.pop()
#         if check == '[':
#             continue
#         else:
#             print(0)
#             break
#     if item == ')':
#         check = stack.pop()
#         if check == '(':
#             answer += 2
#             continue
#         else:
#             print(0)
#             break

#     stack.append(item)

# if stack:
#     print(0)

