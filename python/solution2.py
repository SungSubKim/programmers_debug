def solution(info, edges):
    max_sheep = 0
    N = len(info)
    adj = [[] for _ in range(N)]
    visited = [False for _ in range(N)]
    for parent, child in edges:
        adj[parent].append(child)
    def dfs(num,sheep,wolf,_move):
        nonlocal max_sheep
        if sheep>max_sheep:
            max_sheep=sheep
        visited[num]=True
        for _next in _move:
            if visited[_next]:
                continue
            next_sheep = sheep+(1-info[_next])
            next_wolf = wolf+(info[_next])
            if next_sheep-next_wolf>0:
                dfs(_next,next_sheep,next_wolf,list(_move+adj[_next]))
        visited[num]=False
    dfs(0,1,0,adj[0])
    return max_sheep