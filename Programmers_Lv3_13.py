BASE_TIME = 540

def time_to_minute(timetable):
    result = []
    for time in timetable:
        hour = int(time.split(':')[0])
        minute = int(time.split(':')[1])
        result.append(hour*60 + minute)
    return result

def minute_to_time(minutes):
    hour = str(minutes // 60).zfill(2)
    minute = str(minutes % 60).zfill(2)
    return hour + ':' + minute

def solution(n, t, m, timetable):
    answer = ''
    bus_time = []
    crew_time = []
    
    for i in range(n):
        bus_time.append(BASE_TIME + t*i)
    
    crew_time = sorted(time_to_minute(timetable))
    
    idx = 0
    for time in bus_time:
        crew_num = 0
        while crew_num < m and idx < len(crew_time) and crew_time[idx] <= time:
            crew_num += 1
            idx += 1
            
        if crew_num < m:
            answer = time
        else:
            answer = crew_time[idx-1] - 1
        
    return minute_to_time(answer)