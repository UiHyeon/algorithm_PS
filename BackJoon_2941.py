import sys

item = sys.stdin.readline().rstrip()
alpha_c = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for check in alpha_c:
    item = item.replace(check, '*')

print(len(item))