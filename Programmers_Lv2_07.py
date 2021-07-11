import collections

def solution(clothes):
    answer = 1
    clothes_hash = {}
    
    for clothes, category in clothes:
        try: clothes_hash[category].append(clothes)
        except: clothes_hash[category] = [clothes]
            
    print(clothes_hash)
        
    for key in clothes_hash.keys():
        answer = answer * (len(clothes_hash[key])+1)
    
    
    return answer-1