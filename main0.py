from time import time
def run_test(testcases,expectations,solution):
    cnt=0
    print_tc = lambda x: print(*x,sep=' // ') if len(str(x))<=200 else print('bigger than 200',sep=' // ')
    print_val = lambda x: (print(x) if type(x)==type([]) else print(x)) if len(str(x))<=200 \
        else print('bigger than 200',sep=' // ')
    for i, tc in enumerate(testcases):
        start = time()
        print('Testcase',end=' - ')
        print(i)
        print('{0:<10}'.format('Input'), end=': ')
        print_tc(tc)
        print('{0:<10}'.format('Expected'), end=': ')
        print_val(expectations[i])
        real_val = solution(*tc)
        print('{0:<10}'.format('Real value'), end=': ')
        print_val(real_val)
        print('{0:<10}'.format('Result')+':', expectations[i]==real_val)
        print('{0:<10}'.format('Time')+':', int((time()-start)*1000),'ms')
        print()
        if expectations[i]==real_val: cnt+=1
    print('End\n{0:<10}: {1}/{2} '.format('Total result',cnt,len(testcases)))
    if cnt==len(testcases): print('All passed!')