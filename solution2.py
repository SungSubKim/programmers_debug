def solution(replies, n, k):
    answer = []
    for idx,reply in enumerate(replies):
        for start in range(len(reply)):
            for l in range(n,(len(reply)-start)//k+1):
                if reply[start:start+l]*k==reply[start:start+k*l]:
                    answer.append(0)
                    break
            if idx+1==len(answer): break
        if idx==len(answer):
            answer.append(1)
    return answer