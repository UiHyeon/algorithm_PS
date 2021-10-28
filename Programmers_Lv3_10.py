import math

def solution(n, stations, w):
    answer = 0

    apart = [False for _ in range(n)]
    for station in stations:
        station -= 1
        #맨 뒤
        if station == len(apart)-1:
            for i in range(station-w, station+1):
                apart[i] = True
        #맨 앞
        elif station == 0:
            for i in range(station, station+w):
                apart[i] = True
        else:
            for i in range(station-w, station+w+1):
                apart[i] = True
            
    cnt = 0
    result = []
    for check in apart:
        if not check:
            cnt += 1
        else:
            if cnt != 0:
                result.append(cnt)
            cnt = 0
    else:
        if cnt != 0:
            result.append(cnt)
    
    distance = w * 2 + 1
    for item in result:
        if math.ceil(item / distance) > 1:
            answer += math.ceil(item / distance)
        else:
            answer += 1
            
    return answer