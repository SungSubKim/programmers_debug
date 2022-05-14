from solution import *
from time import time

##########코테 보기전 화장실
##########코테 보기전 화장실
##########코테 보기전 화장실
if __name__ == '__main__':
    testcases = [["02:03:55", "00:14:15",
                  ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29",
                   "01:37:44-02:02:30"]], ["99:59:59", "25:00:00",
                                           ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59",
                                            "11:00:00-31:00:00"]],
                 ["50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]],
                 ["99:59:59","00:00:05",["99:59:58-99:59:59" for _ in range(300000)]]
                 ]
    expectations = ["01:30:59", "01:00:00", "00:00:00","99:59:54"]
    cnt=0
    for i, tc in enumerate(testcases):
        start = time()
        real_val = solution(*tc)
        print('Testcase',end=' - ')
        print(i)
        print('{0:<10}'.format('Input'), end=': ')
        print(tc if len(str(tc))<=200 else 'bigger than 200')
        print('{0:<10}'.format('Real value'), end=': ')
        print(real_val)
        print('{0:<10}'.format('Expected'), end=': ')
        print(expectations[i])
        print('{0:<10}'.format('Result')+':', expectations[i]==real_val)
        print('{0:<10}'.format('Time')+':', int((time()-start)*1000),'ms')
        print()
        if expectations[i]==real_val: cnt+=1
    print('End\n{0:<10}: {1}/{2} '.format('Total result',cnt,len(testcases)))
    if cnt==len(testcases): print('All passed!')