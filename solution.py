def solution(replies, n, k):
    answer = []
    for reply in replies:
        for l in range(3,len(reply)):
            set(reply[start:start+l] for start in range(len(reply)-l+1))
            if
    return answer