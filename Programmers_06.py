import re

def solution(str1, str2):
    answer = 0
    
    result1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if str1[i:i+2].isalpha()]
    result2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if str2[i:i+2].isalpha()]
            
    gyo_num = 0
    
    for temp in result1:
        if temp in result2:
            gyo_num += 1
            result2.remove(temp)
            
    hap_num = len(result1) + len(result2)
            
    try:
        return int((gyo_num / hap_num) * 65536)
    except:
        return 65536