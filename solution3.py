def solution(n, rooks):
    answer = 0
    pool = []
    for a in range(n):
        for a2 in range(2*a+1):
            b,c= a2//2, a-(a2+1)//2
            pool.append((a,b,c))
    # print(len(pool))
    banned=[False for _ in pool]
    selected=[]
    def dfs(i):
        nonlocal banned,answer
        if len(selected) ==rooks:
            # if not [1 for tmp in banned if not tmp] :
            answer+=1
            return
        for idx,v in enumerate(pool):
            if idx<=i or banned[idx]: continue
            p,q,r = v
            banned0 = list(banned)
            for i2 in range(len(banned)):
                if pool[i2][0]==p or pool[i2][1]==q or pool[i2][2]==r:
                    banned[i2]=True
            selected.append(v)
            dfs(idx)
            selected.pop()
            banned = banned0

    dfs(-1)
    return answer