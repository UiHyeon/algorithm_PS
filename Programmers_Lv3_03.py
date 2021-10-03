# import math

# def solution(enroll, referral, seller, amount):
#     answer = {}
#     graph = {}
    
#     answer['root'] = 0
#     graph['root'] = []
#     for name in enroll:
#         answer[name] = 0
#         graph[name] = []
    
#     for child, parent in zip(enroll, referral):
#         if parent == "-":
#             parent = 'root'
#         graph[child].append(parent)
#         graph[parent].append(child)
#     #여기까지 주어진 관계도의 그래프를 만듬.
    
#     for sell, pay in zip(seller, amount):
#         visit = []
#         stack = [sell]
#         pay = pay * 100
#         while stack:
#             node = stack.pop()
#             if node == 'root':
#                 # temp = math.floor(pay * 0.1)
#                 # now = pay - temp
#                 # pay -= now
#                 # answer[node] += now+temp
#                 # stack = []
#                 break
                
#             if node not in visit:
#                 temp = math.floor(pay * 0.1)
#                 now = pay - temp
#                 pay -= now
#                 visit.extend(graph[node][1:])
#                 stack.extend(graph[node])
                
#                 if temp <= 0:
#                     answer[node] += now
#                     break
#                 answer[node] += now
    
#     return list(answer.values())[1:]



def solution(enroll, referral, seller, amount):
    graph, answer = {},{name:0 for name in enroll}
    
    for child, parent in zip(enroll, referral):
        graph[child] = parent
        
    for name, money in zip(seller, amount):
        money = money * 100
        toss_money = money // 10
        answer[name] += money - toss_money
        next_name = graph[name]
        
        while next_name != "-":
            if toss_money == 0: break
            answer[next_name] += toss_money - toss_money // 10
            toss_money //= 10
            next_name = graph[next_name]
    return list(answer.values())