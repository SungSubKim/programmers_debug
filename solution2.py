def solution(play_time, adv_time, logs):
    to_second = lambda part: int(part[:2])*3600+ int(part[3:5])*60+int(part[6:8])
    play_time,adv_time = to_second(play_time),to_second(adv_time)
    logs = [[  to_second(part) for part in log.split('-')] for log in logs]
    arr,arr2 =[ [0 for _ in range(play_time+1)] for _ in range(2)]
    for s,e in logs: arr[s]+=1;arr[e]-=1
    val,val2=0,0
    for i in range(play_time+1):
        val+=arr[i]
        val2+=val
        arr2[i]=val2
    optimal_start,_max=0,-1
    for start in range(play_time-adv_time+1):
        end = start+adv_time
        val = arr2[end-1]-(arr2[start-1] if start-1>-1 else 0)
        if _max<val: optimal_start = start;_max = val
    lst=[int(optimal_start//3600),int((optimal_start%3600)//60),optimal_start%60]
    return '{0:0>2}:{1:0>2}:{2:0>2}'.format(*lst)