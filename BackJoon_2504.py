import sys
from collections import deque

temp = list(sys.stdin.readline().rstrip())
print(temp)
answer = 0

stack = []
for item in temp:
    if item == ']':
        check = stack.pop()
        if check == '[':
            continue
        else:
            print(0)
            break
    if item == ')':
        check = stack.pop()
        if check == '(':
            answer += 2
            continue
        else:
            print(0)
            break

    stack.append(item)

if stack:
    print(0)

