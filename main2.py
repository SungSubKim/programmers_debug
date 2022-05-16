from solution2 import *
from time import time

##########코테 보기전 화장실
##########코테 보기전 화장실
##########코테 보기전 화장실
if __name__ == '__main__':
    testcases = [[["AFFDEFDEFDEEC", "ABABABABBCCEF", "FFFFFFFFFFFFF", "FCBBBFCBBECBB"], 3, 2],
                 [["AFFDEFDEFDEEC", "ABABABABBCCEF", "FFFFFFFFFFFFF", "FCBBBFCBBECBB"], 2, 4],
                 [["FFCCAAFCCAAA", "AAAABBBBCCCC", "ABCABCABCABC"], 4, 2],
                 [["FFCCAAFCCAAA", "AAAABBBBCCCC", "ABCABCABCABC"], 3, 3]]
    expectations = [[0, 0, 0, 1], [1, 0, 0, 1], [0, 1, 0], [1, 1, 0]]
    cnt=0
    for i, tc in enumerate(testcases):
        start = time()
        print('Testcase',end=' - ')
        print(i)
        print('{0:<10}'.format('Input'), end=': ')
        print(*tc if len(str(tc))<=200 else 'bigger than 200',sep=' // ')
        print('{0:<10}'.format('Expected'), end=': ')
        print(expectations[i])
        real_val = solution(*tc)
        print('{0:<10}'.format('Real value'), end=': ')
        print(real_val)
        print('{0:<10}'.format('Result')+':', expectations[i]==real_val)
        print('{0:<10}'.format('Time')+':', int((time()-start)*1000),'ms')
        print()
        if expectations[i]==real_val: cnt+=1
    print('End\n{0:<10}: {1}/{2} '.format('Total result',cnt,len(testcases)))
    if cnt==len(testcases): print('All passed!')