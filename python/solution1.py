#ctrl Y 행삭제 ctrl shift arrow 옮기기 ctrl D 행복제 ctrl C 행복사
def solution(board, skill):
    N,M = len(board), len(board[0])
    board = [[0 for _ in range(M+1)]]+[[0]+row for row in board]
    board2 = [[0 for _ in range(M+1)] for _ in range(N+1)]
    # padding 넣기
    # padding을 넣으면 케이스 처리가 줄어든다.
    for _type, r1,c1,r2,c2,degree in skill:
        if _type==1: degree*=-1
        r1,c1,r2,c2=r1+1,c1+1,r2+1,c2+1
        board2[r2][c2]+=degree
        board2[r1-1][c2]-=degree
        board2[r2][c1-1]-=degree
        board2[r1-1][c1-1]+=degree
    for i in range(1,N+1): # 1~ N
        for j in range(M-1,0,-1): # (M-1)~ 1
            board2[i][j]+= board2[i][j+1]
    for j in range(1,M+1):
        for i in range(N-1,0,-1):
            board2[i][j]+=board2[i+1][j]
    answer=0
    for i in range(1,N+1):
        for j in range(1,M+1):
            if board[i][j]+board2[i][j]>0:
                answer+=1
    return answer

