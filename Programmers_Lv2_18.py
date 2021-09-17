def cal_minute(start, end):
    start_hour, start_min = list(map(int, start.split(':')))
    end_hour, end_min = list(map(int, end.split(':')))
    
    start_sum = (start_hour * 60) + start_min
    end_sum = (end_hour * 60) + end_min
    
    return end_sum - start_sum

def trans_note(notes):
    before = ['C#', 'D#', 'F#', 'G#', 'A#']
    after = ['c', 'd', 'f', 'g', 'a']
    for note in before:
        if note in notes:
            idx = before.index(note)
            notes = notes.replace(before[idx], after[idx])
    return notes

def solution(m, musicinfos):
    answer = []
    temp = []
    check = {}
    m = trans_note(m)
    
    for info in musicinfos:
        temp.append(info.split(','))
    
    for item in temp:
        time = cal_minute(item[0], item[1])
        real_song = trans_note(item[3])
        song_len = len(real_song)
        song = ''
        
        while time > song_len:
            song += real_song
            time -= song_len
            
        song += real_song[:time]
        
        if m in song:
            check[item[2]] = cal_minute(item[0], item[1])
    if len(check) == 0:
        return "(None)"
    
    max_time = max(check.values())
    
    for key in check.keys():
        if check[key] == max_time:
            answer.append(key)
    
    return answer[0]