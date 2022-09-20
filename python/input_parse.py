T = int(input())
#테케 갯수를 넣어주세요!
tc,expectation=[],[]
for _ in range(T):
    row = input().split('\t')
    tc.append('['+','.join(row[:-1])+']')
    expectation.append(row[-1])
# 그후는 복사한값 입력
print()
print('testcases = ['+','.join(tc)+']')
print('expectations = ['+','.join(expectation)+']')