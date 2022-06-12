def solution(n, plans, clients):
    answer = []
    dp={}
    for i in range(len(plans)):
        lst = list(map(int,plans[i].split()))
        plans[i]=(lst[0],i+1)
        for service in lst[1:]:
            dp[service] = lst[0]
    plans.sort()
    for client in clients:
        client = list(map(int,client.split()))
        escaped=False
        for i in range(1,len(client)):
            if client[i] in dp: client[i]=dp[client[i]]
            else: escaped=True
        if escaped:
            answer.append(0)
            continue
        need = max(client)
        s,e = 0,len(plans)-1
        while s<e:
            mid = (s+e)//2
            if need<=plans[mid][0]: e=mid
            else: s=mid+1
        if plans[s][0]<need:
            answer.append(0)
        else: answer.append(plans[s][1])
    return answer