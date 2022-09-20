def solution(pfirst,pescape,pexit,data):
    answer=pfirst
    #먼저 앞에 first박기
    N=len(pescape)
    # pescape길이 N만큼 data를 나누어주자
    for i in range(0,len(data),N):
        # pescape길이 N만큼 data를 나누어주자
        block = data[i:i+N]
        # 나누었다.
        if block in (pfirst,pescape,pexit): answer+= pescape
        # 만약 이렇게 나눈 블럭이 저 세개 중 하나에 해당되면
        # 블럭앞에 pescape를 삽입
        answer+=block
        # 원래의 data인 block을 삽입
    return answer+pexit
        #exit 뒤에 삽입해주고 반환