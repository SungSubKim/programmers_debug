from collections import deque
def solution(grid, k):
    answer = -1
    n,m = len(grid),len(grid[0])
    visited=[[[False for k2 in range(k+1)] for j in range(m)] for i in range(n)]
    q=deque([(0,0,k,0)])
    q2=deque()
    while True:
        if not q:
            while q2: q.append(q2.popleft())
        if not q: break
        x,y,energy,cnt = q.popleft()
        if visited[x][y][energy]: continue
        visited[x][y][energy]=True
        if (x,y)==(n-1,m-1):
            return cnt
        for nx,ny in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
            if energy==0: break
            if not(-1<nx<n and -1<ny<m) or grid[nx][ny]=='#': continue
            q.append((nx, ny, energy-1, cnt))
        if grid[x][y] == '.' and energy<k:
            q2.append((x, y, k, cnt + 1))
    return answer