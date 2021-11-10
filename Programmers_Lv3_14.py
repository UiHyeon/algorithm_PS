from itertools import permutations

def check_ban(combi, banned_id):
    for combi_id, ban_id in zip(combi, banned_id):
        if len(combi_id) != len(ban_id):
            return False
        for i in range(len(combi_id)):
            if ban_id[i] == "*":
                continue
            elif combi_id[i] != ban_id[i]:
                return False
    return True

def solution(user_id, banned_id):
    answer = 0
    result = []
    user_combi = list(permutations(user_id, len(banned_id)))
    
    for combi in user_combi:
        if not check_ban(combi, banned_id):
            continue
        else:
            combi = set(combi)
            if combi not in result:
                result.append(combi)

    answer = len(result)
        
    return answer