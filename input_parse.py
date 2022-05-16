T = int(input())
tc,expectation=[],[]
for _ in range(T):
    row = input().split('\t')
    tc.append('['+','.join(row[:-1])+']')
    expectation.append(row[-1])
print()
print('testcases = ['+','.join(tc)+']')
print('expectations = ['+','.join(expectation)+']')