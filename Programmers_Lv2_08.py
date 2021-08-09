def solution(arr1, arr2):
    answer = [[] for i in range(len(arr1))]
    
    while arr1:
        target = arr1.pop()
        row = len(arr1)
        
        for c in range(len(arr2[0])):
            sum = 0
            for r in range(len(arr2)):
                sum += target[r] * arr2[r][c]
                
            answer[row].append(sum)
    
    return answer