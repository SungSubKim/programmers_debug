from solution1 import *
from main0 import run_test

##########코테 보기전 화장실
if __name__ == '__main__':
    testcases = [
        [[[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
         ,[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]],
        [[[1,2,3],[4,5,6],[7,8,9]],
         [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]]
        ,
    ]
    expectations = [
        10,6
    ]
    run_test(testcases,expectations,solution)