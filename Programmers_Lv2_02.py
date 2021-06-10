from itertools import combinations

def solution(orders, course):
    answer = []
    
    for course_num in course:
        course_dict = {}
        select = []
        
        for order in orders:
            select.extend(list(combinations(sorted(order), course_num)))
            
        for temp in select:
            combi = "".join(temp)
            if combi in course_dict:
                course_dict[combi] += 1
            else:
                course_dict[combi] = 1

        for key in course_dict:
            if course_dict[key] > 1 and course_dict[key] == max(course_dict.values()):
                answer.append(key)
                
    answer.sort()
        
    return answer