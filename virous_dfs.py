import sys

a = sys.stdin.readline().rstrip()
dict_com = {}
for i in range(int(a)):
    dict_com[str(i+1)] = []
connect = int(sys.stdin.readline().rstrip())


visit = []
for i in range(connect):
    parent, child = map(str, sys.stdin.readline().rstrip().split())
    dict_com[parent].append(child)
    dict_com[child].append(parent)

stack = ['1']

while stack:
    node = stack.pop()
    if node not in visit:
        visit.append(node)
        stack.extend(dict_com[node])
        
print(len(visit)-1)