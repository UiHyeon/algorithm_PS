def solution(N, number):
    dp_case = [[]]
    
    for i in range(1,9):
        case = []
        case.append(int(str(N)*i))
        for j in range(1, i):
            for combi_i in dp_case[j]:
                for combi_j in dp_case[i-j]:
                    case.append(combi_j + combi_i)
                    case.append(combi_j * combi_i)
                    if combi_j - combi_i >= 0 :
                        case.append(combi_j - combi_i)
                    if combi_j != 0 and combi_i != 0:
                        case.append(combi_j // combi_i)
                        
        if number in case:
            return i
        dp_case.append(list(set(case)))
    return -1